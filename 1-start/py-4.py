from threading import Thread
import logging
from time import sleep


def example_work(params):
    sleep(params)
    logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    logging.debug('Start program')
    threads = []
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    logging.debug('End program')

"""
MainThread Start program
Thread-1 Wake up!
Thread-2 Wake up!
Thread-3 Wake up!
Thread-4 Wake up!
Thread-5 Wake up!
MainThread End program
"""