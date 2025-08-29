from factory.file_factory import FileFactory
from models.file_type import FileType
from models.text import TxtfText, XlsText, PdfText


def main():
    print("""
    Choose the file Type
    1. TXT
    2. PDF
    3. XLS
    """)

    choose = int(input("Choose the type: "))
    name = input("Enter file name: ")

    file = None

    if choose == 1:  # TXT
        file = FileFactory.get_file(name, FileType.TXT)
        print("TXT file created:", file)

        text = input("Enter text: ")
        t = TxtfText(text, file)
        t.addText()
        t.readText()

    elif choose == 2:  # PDF
        file = FileFactory.get_file(name, FileType.PDF)
        print("PDF file created:", file)

        content = input("Enter PDF content: ")
        text = input("Enter PDF text: ")
        sign = input("Enter signature: ")

        t = PdfText(content, text, sign, file)
        t.addText()
        t.readText()

    elif choose == 3:  # XLS
        file = FileFactory.get_file(name, FileType.XLS)
        print("XLS file created:", file)

        cell = input("Enter cell (e.g., A1): ")
        value = input("Enter value: ")

        t = XlsText(file)
        t.addText(cell, value)
        t.readText()

    else:
        print("Invalid choice !!")


if __name__ == "__main__":
    main()
