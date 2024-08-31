import datetime
import multiprocessing

FILES_NAMES = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        string_ = file.readline()[:-1]
        while string_:
            all_data.append(string_)
            string_ = file.readline()[:-1]

if '__main__' == __name__:
    start = datetime.datetime.now()

    for i in FILES_NAMES:
        read_info(i)

    end = datetime.datetime.now()

    print(end - start)


    start = datetime.datetime.now()

    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, FILES_NAMES)

    end = datetime.datetime.now()

    print(end - start)