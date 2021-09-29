
from os import getcwd
from tkinter import filedialog


class WordOrder:
    def __init__(self, document):
        self.document = document

    def process_document(self):
        try:
            with open(self.document) as document:
                document_content = document.readlines()

            list_word = []
            for line in document_content:
                list_word.append(line.strip())

            list_word.pop(0)

            frequency_words = {line: list_word.count(line) for line in list_word}
            total_words = len(frequency_words)
            frequency_words = list(frequency_words.values())
            result_frequency = ' '.join(map(str,frequency_words))
            document.close()

            document = open('words_order.txt', 'w')

            document.write(f"{total_words}\n{result_frequency}")
            document.close()
            path = getcwd()
            print(f"Ubicación del archivo {path}/{document.name}")

        except:
            print('Error')


def open_document():
    document = filedialog.askopenfilename(initialdir="", title="Por Favor seleccione un archivo")

    if document:
        return document
    else:
        print('Por Favor seleccione un archivo')


def main():
    document = open_document()
    word_order = WordOrder(document)
    word_order.process_document()

if __name__ == '__main__':
    main()
