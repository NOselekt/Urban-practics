import threading
from declarations import write_words, ReturningThread

FILES_NAMES = {'example1.txt': 10, 'example2.txt': 30, 'example3.txt': 200, 'example4.txt': 100}

if __name__ =='__main__':

#в один поток

    singlethread_time = sum(write_words(FILES_NAMES[name], name) for name in FILES_NAMES)

    print(f'Однопоточная программа работала: {round(singlethread_time, 4)} секунды')

#в несколько потоков

    threads = {}

    for name in FILES_NAMES:
        threads[name] = ReturningThread(target=write_words, args=(FILES_NAMES[name], name))
        threads[name].start()
    multithread_time = sum(threads[name].join() for name in FILES_NAMES)


    print(f'Однопоточная программа работала: {round(singlethread_time, 4)} секунды')
    print(f'Многопоточная программа работала: {round(multithread_time, 4)} секунды')
