class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for file in file_names:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        punc_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for char in punc_chars:
                    content = content.replace(char, '')
                words = content.split()
                all_words[file] = words
        return all_words


    def find(self, word):
        search_result = {}
        for name, words in self.get_all_words().items():
            position = words.index(word.lower()) + 1
            search_result[name] = position
        return search_result

    def count(self, word):
        count_result = {}
        for name, words in self.get_all_words().items():
            count_result[name] = words.count(word.lower())
        return count_result                    


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
