import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().rstrip()
            if not line:
                break
            all_data.append(line)
    return all_data


start = time.time()
res1 = read_info('file 1.txt')
res2 = read_info('file 2.txt')
res3 = read_info('file 3.txt')
res4 = read_info('file 4.txt')
#print(res1, res2, res3, res4)
end = time.time()
print(end - start)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 4)]
        start_proc = time.time()
        pool.map(read_info, filenames)
        end_proc = time.time()
        print('время выполнения мульти:', end_proc - start_proc)

