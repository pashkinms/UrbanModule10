import multiprocessing
import  time

def read_info(name: str):
    all_data = []
    file_continue = True
    with open(name, 'r') as file:
        while file_continue:
            line = file.readline()
            if line == '':
                file_continue = False
                break
            all_data.append(line)


file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

'''
# Последовательный подход
time_start = time.time()
for file in file_list:
    read_info(file)
time_stop = time.time()

print(time_stop - time_start)
'''

# Многопроцессный подход
if __name__ == '__main__':
    time_start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, file_list)

    time_stop = time.time()
    print(time_stop - time_start)