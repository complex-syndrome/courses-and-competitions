package main

import (
	"bufio"
	"bytes"
	"compress/gzip"
	"flag"
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"slices"
	"strconv"
	"strings"
)

type HTTPRequest struct {
	Method  string
	Path    string
	Version string
	Headers map[string][]string // can be duplicate, thus use map[string][]string
	Body    []byte
}

type HTTPStatus struct {
	Code    int
	Message string
}

type HTTPResponse struct {
	Version string
	Status  HTTPStatus
	Headers map[string]string
	Body    []byte
}

var (
	// IP and Port
	IP_PORT = "0.0.0.0:4221"
	CRLF    = "\r\n"

	// Errors
	ERROR_CODES = map[int]string{
		1: "Connection Error",
		2: "Flag Error",
		3: "Request Read Error",
	}

	// Flags
	FILES_DIRECTORY string

	// Formats
	SUPPORTED_ENCODINGS = []string{"gzip"}

	// Methods
	METHOD_GET    = "GET"
	METHOD_PUT    = "PUT"
	METHOD_POST   = "POST"
	METHOD_DELETE = "DELETE"

	// Statuses
	STATUS_OK                    = HTTPStatus{http.StatusOK, "OK"}
	STATUS_CREATED               = HTTPStatus{http.StatusCreated, "Created"}
	STATUS_BAD_REQUEST           = HTTPStatus{http.StatusBadRequest, "Bad Request"}
	STATUS_UNAUTHORIZED          = HTTPStatus{http.StatusUnauthorized, "Unauthorized"}
	STATUS_NOT_FOUND             = HTTPStatus{http.StatusNotFound, "Not Found"}
	STATUS_INTERNAL_SERVER_ERROR = HTTPStatus{http.StatusInternalServerError, "Internal Server Error"}

	// Commands
	RootDir             = "/"
	CommandEcho         = "/echo/"
	CommandGetUserAgent = "/user-agent"
	CommandFiles        = "/files/"
)

func main() {
	addDirectoryFlag() // Add flag to bind to folder

	fmt.Printf("Starting TCP server at %s...\n", IP_PORT)

	// Listen on port 4221
	l, err := net.Listen("tcp", IP_PORT)
	if err != nil {
		fmt.Println("Failed to bind to port 4221")
		os.Exit(1)
	}
	defer l.Close() // Future close

	// Get connection (multiple)
	for {
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err.Error())
			os.Exit(1)
		}
		// Starts goroutine for handling connections (concurrent)
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	fmt.Println("Connection accepted from:", conn.LocalAddr()) // Accepted
	defer conn.Close()                                         // Future close

	for {
		// Parse request
		request := readRequest(conn)
		if request == nil {
			break
		}

		// Handle request
		response := generateResponse(request) // request is already a pointer, deference it

		// Send Logs
		logRequest(request)   // Request too big, pointer it
		logResponse(response) // Can send many responses, no need shared ownership
		
		// Send back response
		conn.Write(httpResponseToByte(response))
		
		// Close connection
		if r, ok := request.Headers["Connection"]; ok && strings.ToLower(r[0]) == "close" {
			break
		}
	}
}

func readRequest(conn net.Conn) *HTTPRequest {
	// Sequential read
	reader := bufio.NewReader(conn)

	// Request Line (GET /index.html HTTP/1.1\r\n)
	requestLine, err := reader.ReadString('\n')
	if err == io.EOF {
		return nil
	}
	if err != nil {
		fmt.Println("Error reading request line: ", err.Error())
		os.Exit(3)
	}

	// Initialize request
	parts := strings.Split(requestLine, " ")
	rq := &HTTPRequest{
		Method:  strings.TrimSpace(parts[0]),
		Path:    strings.TrimSpace(parts[1]),
		Version: strings.TrimSpace(parts[2]),
		Headers: make(map[string][]string),
	}

	// Request Headers (Host: localhost:4221\r\nUser-Agent: curl/7.64.1\r\nAccept: */*\r\n\r\n)
	for {
		headerLine, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading request header:", err.Error())
			os.Exit(3)
		}

		headerLine = strings.TrimSpace(headerLine)
		if headerLine == CRLF || headerLine == "" { // Headers done
			break
		}

		headerParts := strings.SplitN(headerLine, ": ", 2)
		if len(headerParts) != 2 { // Malformed header
			continue
		}

		key := headerParts[0]
		values := strings.Split(headerParts[1], ", ")

		for _, value := range values { // Auto enumeration (i, v)
			rq.Headers[key] = append(rq.Headers[key], strings.TrimSpace(value))
		}
	}

	if value, ok := rq.Headers["Content-Length"]; ok {
		bufSize, err := strconv.Atoi(value[0])
		if err != nil {
			fmt.Println("Invalid Content-Length value", err)
			os.Exit(3)
		}
		buf := make([]byte, bufSize)
		reader.Read(buf)
		rq.Body = buf
	}
	return rq
}

func generateResponse(request *HTTPRequest) *HTTPResponse {
	response := &HTTPResponse{
		Version: request.Version,
		Headers: make(map[string]string),
	}

	switch request.Method {
	case METHOD_GET:
		GetMethods(request, response)

	case METHOD_POST:
		PostMethods(request, response)

	default:
		buildResponse(request, response, STATUS_NOT_FOUND, "", "")
	}
	return response
}

func buildResponse(req *HTTPRequest, res *HTTPResponse, stat HTTPStatus, contentType, body string) {
	res.Status = stat
	bodyBytes := []byte(body)

	// Encoding data and set headers
	if encodingList, ok := req.Headers["Accept-Encoding"]; ok {
		for _, enc := range encodingList {
			enc = strings.TrimSpace(enc)

			if enc == "gzip" && slices.Contains(SUPPORTED_ENCODINGS, enc) {
				if compressed := gzipCompress(body); compressed != nil {
					bodyBytes = compressed
					res.Headers["Content-Encoding"] = enc
				}
			}
		}
	}

	// Set normal headers
	if len(bodyBytes) > 0 {
		res.Headers["Content-Type"] = contentType
		res.Headers["Content-Length"] = fmt.Sprintf("%d", len(bodyBytes))
	}
	
	// Close connection
	if r, ok := req.Headers["Connection"]; ok && strings.ToLower(r[0]) == "close" {
		res.Headers["Connection"] = "close"
	}

	res.Body = bodyBytes
}

func httpResponseToByte(response *HTTPResponse) []byte {
	statusLine := fmt.Sprintf("%s %d %s", response.Version, response.Status.Code, response.Status.Message)
	statusHeader := ""
	for k, v := range response.Headers {
		statusHeader += fmt.Sprintf("%s: %s%s", k, v, CRLF)
	}
	return append([]byte(statusLine+CRLF+statusHeader+CRLF), response.Body...)
}

func logRequest(r *HTTPRequest) {
	fmt.Println("\n=======================================")
	fmt.Println("Incoming Request:")
	fmt.Printf("%s %s %s\n", r.Method, r.Path, r.Version)

	fmt.Println("\n--------------- Headers ---------------")
	for k, v := range r.Headers {
		fmt.Printf("%s: %s\n", k, v)
	}

	if r.Body != nil {
		fmt.Println("\n---------------- Body -----------------")
		fmt.Println(string(r.Body))
	}
	fmt.Println("\n=======================================")
}

func logResponse(r *HTTPResponse) {
	fmt.Println("Outgoing Response:")
	fmt.Printf("%s %d %s\n", r.Version, r.Status.Code, r.Status.Message)
	fmt.Print("______________________________________\n\n")
}

func addDirectoryFlag() {
	flag.StringVar(&FILES_DIRECTORY, "directory", "", "Directory to serve files from")
	flag.Parse()

	if FILES_DIRECTORY != "" { // GO expects flag followed by value, will fail for you
		if _, err := os.Stat(FILES_DIRECTORY); os.IsNotExist(err) {
			fmt.Println("Error: Directory does not exist.")
			os.Exit(2)
		}
		fmt.Println("Serving files from directory:" + FILES_DIRECTORY)
	}
}

func CheckFileIsValid(filePath string) bool {
	if info, err := os.Stat(filePath); os.IsNotExist(err) {
		return false
	} else {
		return !info.IsDir()
	}
}

func GetMethods(request *HTTPRequest, response *HTTPResponse) {
	if request.Path == RootDir { // Connection alive
		buildResponse(request, response, STATUS_OK, "", "")

	} else if request.Path == CommandGetUserAgent { // Get User Agent
		if userAgent, ok := request.Headers["User-Agent"]; ok {
			buildResponse(request, response, STATUS_OK, "text/plain", userAgent[0])
		} else {
			buildResponse(request, response, STATUS_NOT_FOUND, "", "")
		}

	} else if strings.HasPrefix(request.Path, CommandEcho) { // Echo something
		buildResponse(request, response, STATUS_OK, "text/plain", strings.TrimPrefix(request.Path, CommandEcho))

	} else if strings.HasPrefix(request.Path, CommandFiles) { // File operations
		if FILES_DIRECTORY == "" {
			buildResponse(request, response, STATUS_BAD_REQUEST, "", "")
		}

		filePath := FILES_DIRECTORY + "/" + strings.TrimPrefix(request.Path, CommandFiles)

		if CheckFileIsValid(filePath) {
			fileContents, err := os.ReadFile(filePath)
			if err != nil {
				buildResponse(request, response, STATUS_INTERNAL_SERVER_ERROR, "", "")
			}
			buildResponse(request, response, STATUS_OK, "application/octet-stream", string(fileContents))

		} else {
			buildResponse(request, response, STATUS_NOT_FOUND, "", "")
		}

	} else { // Not Found
		buildResponse(request, response, STATUS_NOT_FOUND, "", "")
	}

}

func PostMethods(request *HTTPRequest, response *HTTPResponse) {
	if strings.HasPrefix(request.Path, CommandFiles) {
		fileName := strings.TrimPrefix(request.Path, CommandFiles)

		if FILES_DIRECTORY != "" && fileName != "" {
			file, err := os.OpenFile(FILES_DIRECTORY+"/"+fileName, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
			if err != nil {
				buildResponse(request, response, STATUS_INTERNAL_SERVER_ERROR, "", "")
				return
			}
			defer file.Close()
			file.Write(request.Body)

			buildResponse(request, response, STATUS_CREATED, "", "")

		} else {
			buildResponse(request, response, STATUS_BAD_REQUEST, "", "")
		}

	} else {
		buildResponse(request, response, STATUS_NOT_FOUND, "", "")
	}
}

func gzipCompress(message string) []byte {
	var buffer bytes.Buffer
	gzWriter := gzip.NewWriter(&buffer)

	// Number of bytes returned
	if _, err := gzWriter.Write([]byte(message)); err != nil {
		return nil
	}
	_ = gzWriter.Close() // (release internal buffers)
	return buffer.Bytes()
}
