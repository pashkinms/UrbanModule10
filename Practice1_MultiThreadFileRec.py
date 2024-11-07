from time import sleep, time
import threading


def write_words(word_count: int, file_name: str):
    file = open(file_name, 'a')
    for i in range(1, word_count + 1):
        file.write(f'Some word № {i}')
        sleep(0.05)
    file.close()
    print(f"Func stopped writing file {file_name}")

time_start = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = time()

print(f'Time elapsed (sec): {time_stop - time_start}')

thread1 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

time_start2 = time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_stop2 = time()

print(f'Time elapsed (sec): {time_stop2 - time_start2}')