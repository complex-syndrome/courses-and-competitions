def ext(v):
    match v:
        case "gif":
            return "image/gif"

        case "png":
            return "image/png"

        case "jpg":
            return "image/jpeg"

        case "jpeg":
            return "image/jpeg"

        case "bin":
            return "application/octet-stream"

        case "pdf":
            return "application/pdf"

        case "txt":
            return "text/plain"

        case "zip":
            return "application/zip"
        
        case _:
            return "application/octet-stream"


print(ext(input("File name: ").strip().lower().split(".")[-1]))
