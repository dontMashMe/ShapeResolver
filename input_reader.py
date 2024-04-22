class InputReader:
    def __init__(self, file_name: str):
        self.file_name: str = file_name

    input_root = "input"

    def load_file(self) -> str:
        file_to_load = f"{self.input_root}/{self.file_name}"
        out = ""
        with open(file_to_load, 'r') as f_read:
            for line in f_read:
                out += line
        return out
