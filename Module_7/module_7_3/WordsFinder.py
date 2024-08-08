PUNCTUATION_MARKS = [',', '.', ' ', '=', '?', '!', ';', ':', '*', '/', ' - ', '<', '>']

class WordsFinder:

    def __init__(self, *files_names: str):
        self.files_names = [file_name for file_name in files_names]
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.files_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_viscera = file.read()
                for mark in PUNCTUATION_MARKS:
                    file_viscera = file_viscera.replace(mark, ' ')
                self.all_words[file_name] = file_viscera.split()

                for i in range(len(self.all_words[file_name])):
                    self.all_words[file_name][i] = self.all_words[file_name][i].lower()

        return self.all_words

    def find(self, word_to_find: str):
        word_to_find = word_to_find.lower()
        result = {}
        for key in self.all_words.keys():
            position = 0
            for word in self.all_words[key]:
                position += 1
                if word == word_to_find:
                    result[key] = position
                    break
        return result

    def count(self, word_to_find: str):
        word_to_find = word_to_find.lower()
        result = {}

        for key in self.all_words.keys():
            counter = 0
            for word in self.all_words[key]:
                if word == word_to_find:
                    counter += 1
            result[key] = counter
        return result


