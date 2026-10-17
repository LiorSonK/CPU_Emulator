import os

class file_handle:

    @staticmethod
    def get_files():
        files = []
        for file in os.listdir(os.chdir('../../programs')):
            f = open(file, 'r')
            files.append(f)
        return files

    @staticmethod
    def split_file(file):
        return file.read().split("\n")

    @staticmethod
    def handle_files():
        final = []
        files = file_handle.get_files()
        for file in files:
            final.append(file_handle.split_file(file))
        return final