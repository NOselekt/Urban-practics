import threading
from declarations import write_words, ReturningThread

FILES_NAMES_1 = {'example1.txt': 10, 'example2.txt': 30, 'example3.txt': 200, 'example4.txt': 100}
FILES_NAMES_2 = {'example5.txt': 10, 'example6.txt': 30, 'example7.txt': 200, 'example8.txt': 100}

if __name__ =='__main__':

#в один поток

    singlethread_time = sum(write_words(FILES_NAMES_1[name], name) for name in FILES_NAMES_1)

    print(f'Однопоточная программа работала: {round(singlethread_time, 4)} секунды')

#в несколько потоков

    threads = {}

    for name in FILES_NAMES_2:
        threads[name] = ReturningThread(target=write_words, args=(FILES_NAMES_2[name], name))
        threads[name].start()
    multithread_time = sum(threads[name].join() for name in FILES_NAMES_2)


    print(f'Однопоточная программа работала: {round(singlethread_time, 4)} секунды')
    print(f'Многопоточная программа работала: {round(multithread_time, 4)} секунды')
