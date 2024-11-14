from queue import Queue
import threading
from random import randint
from time import sleep


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = [*tables]

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            is_guest_fed = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'Гость {guest.name} сел за стол №{table.number}')
                    is_guest_fed = True
                    break
            if not is_guest_fed:
                self.queue.put(item=guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        cafe_is_busy = True

        while cafe_is_busy:

            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал и ушел.')
                        print((f'{table.number} свободен.'))
                        table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел из очереди и сел за стол {table.number}')
                    table.guest.run()
            cafe_is_busy = False
            for table in self.tables:
                if table.guest is not None:
                    cafe_is_busy = True
        print('Все гости ушли.')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()





