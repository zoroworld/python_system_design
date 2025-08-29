from models.file_type import FileType
from models.file import PdfFile, TxtFile, XlsFile
class FileFactory:
    @staticmethod
    def get_file(filename, type:FileType):

        if type == FileType.TXT:
            name = f"{filename}.txt"
            return  TxtFile(name)
        elif type == FileType.PDF:
            name = f"{filename}.pdf"
            return  PdfFile(name)
        elif type == FileType.XLS:
            name = f"{filename}.xls"
            return XlsFile(name)
        else:
            print("Not valid type...")
