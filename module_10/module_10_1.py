from datetime import datetime
from operator import imod
from threading import Thread
from time import sleep
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range (word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    return f'Завершилась запись в файл {file_name}'


def start_without_thread():
    time_start = datetime.now()
    print(write_words(10, 'example1.txt'))
    print(write_words(30, 'example2.txt'))
    print(write_words(200, 'example3.txt'))
    print(write_words(100, 'example4.txt'))
    time_end = datetime.now()
    print(time_end - time_start)

def start_with_thread():
    thd_first = Thread(target=write_words, args=(10, 'example5.txt'))
    thd_second = Thread(target=write_words, args=(30, 'example6.txt'))
    thd_third = Thread(target=write_words, args=(200, 'example7.txt'))
    thd_forth = Thread(target=write_words, args=(100, 'example8.txt'))

    time_start = datetime.now()
    thd_first.start()
    thd_second.start()
    thd_third.start()
    thd_forth.start()
    time_end = datetime.now()
    print(time_end - time_start)


def main():
    start_without_thread()
    start_with_thread()

main()


