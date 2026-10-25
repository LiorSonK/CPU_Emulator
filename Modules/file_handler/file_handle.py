import os

class file_handle:

    @staticmethod
    def get_files():
        files = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dir_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'programs'))
        for file in os.listdir(dir_path):
            filepath = os.path.join(dir_path, file)
            f = open(filepath, 'r')
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
