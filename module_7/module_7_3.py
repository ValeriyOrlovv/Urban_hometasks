import string


class WordFinder:
    def __init__(self, *file_names) -> None:
        self.file_names = file_names

    def get_all_word(self) -> dict:
        res_dict = {}
        all_words = []
        separator = ',|.|=|!|?|;|:| - '
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for word in line:
                
                
