from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        title = "CS50 Shirtificate"
        self.set_font("helvetica", "B", 30)
        self.cell(200, 100, title, align="C")

    def shirtificate(self, content):
        self.set_auto_page_break(True)
        self.set_y(180)
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, content, align="C")

if __name__ == "__main__":
    pdf = Shirtificate()
    pdf.add_page()

    pdf.image("shirtificate.png", w=pdf.w - 10, h=180, x=5, y=100)
    pdf.shirtificate(f"{input("Name: ").title()} took CS50")

    pdf.output("shirtificate.pdf")
