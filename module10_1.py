from threading import Thread
from datetime import datetime
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time_multi_flow = time.time()

first = Thread(target=write_words, args=(10, 'example10_1.txt'))
second = Thread(target=write_words, args=(30, 'example10_2.txt'))
third = Thread(target=write_words, args=(200, 'example10_3.txt'))
forth = Thread(target=write_words, args=(100, 'example10_4.txt'))

first.start()
second.start()
third.start()
forth.start()

first.join()
second.join()
third.join()
forth.join()
end_time_multi_flow = time.time()
elapsed_time_multi_flow = round(end_time_multi_flow - start_time_multi_flow, 2)
print(f'Работа потоков {elapsed_time_multi_flow} секунд(ы)')

start_time_func = datetime.now()
write_words(10, 'example10_1.txt')
write_words(30, 'example10_2.txt')
write_words(200, 'example10_3.txt')
write_words(100, 'example10_4.txt')

end_time_func = datetime.now()
elapsed_time_func = end_time_func - start_time_func
print(f'Работа потоков {elapsed_time_func}')
