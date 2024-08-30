import queue
import random
import threading
import time


class Table:
    def __init__(self, number: int):
        self._number = number
        self.guest = None

    def get_number(self):
        return self._number

class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def run(self):
        super().run()
        time.sleep(random.randint(3, 10))

    def get_name(self):
        return self._name

class Cafe:
    def __init__(self, *Tables: Table):
        self.tables = tuple(table for table in Tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.get_number()}')
                    guest = None
                    break
            if guest:
                self.queue.put(guest)
                print(f'{guest.get_name()} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.get_name()} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол №{table.get_number()} свободен')
                if not self.queue.empty() and not table.guest:
                    table.guest = self.queue.get()
                    print(f"{table.guest.get_name()} вышел(-ла) из очереди и сел(-а) за стол номер {table.get_number()}")
                    table.guest.start()
                    table.guest.join()


