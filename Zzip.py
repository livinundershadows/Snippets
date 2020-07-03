from zipfile import ZipFile
import zipfile
from rarfile import RarFile
import os

def modeOperation(ChoiceEx, file_path, file_extension):
    if ChoiceEx == "Z":
        expected_extension = input("enter zip ?")
        compressobj = compressor(expected_extension, file_path)
        compressobj.zip_this()

    elif ChoiceEx == "U":
        extractobj = extracter(file_extension, file_path)

        if file_extension == ".zip":
            extractobj.zip_extract()
        elif file_extension == ".rar":
            extractobj.rar_extract()

class compressor:
    def __init__(self, expected_extension, file_path):
        self.excepted_entension = expected_extension
        self.file_path = file_path
        namenewfile = input("Enter a file name: ")
        self.zipf = ZipFile(namenewfile+'.zip', 'w', zipfile.ZIP_DEFLATED)

    def zip_this(self):
        for root, dirs, files in os.walk('tmp/'):
            for file in files:
                self.ziph.write(os.path.join(root, file))
        self.zipf.close()
        print("Zip done")

class extracter:
    def __init__(self, file_extension, file_path):
        self.file_path = file_path
        self.file_extension = file_extension
    def zip_extract(self):
        with ZipFile(self.file_path, "r") as zip:
            zip.printdir()
            zip.extractall()
            print("Done")
    def rar_extract(self):
        with RarFile(self.file_path, "r") as rar:
            rar.printdir()
            rar.extractall()
            print("Done")


def main():
    ChoiceEx  = input("Zip(Z) / Unzip(U) only creation of .zip files supported?")
    file_path = input("Paste address of file : \n")
    filename, file_extension = os.path.splitext(file_path)
    modeOperation(ChoiceEx, file_path, file_extension)

if __name__ == "__main__":
    main()










