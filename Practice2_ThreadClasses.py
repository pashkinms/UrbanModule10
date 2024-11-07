import threading
import time
class Knight(threading.Thread):
    ARMY_COUNT = 100
    TIME_DELAY = 1
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        army = self.ARMY_COUNT
        day = 0
        print(f'{self.name}! We are under attack!!!')
        while army > 0:
            time.sleep(self.TIME_DELAY)
            day += 1
            army -= self.power
            print(f'{self.name} is fighting for {day} days. There is {army} of invaders left.\n')
        print(f'{self.name} has got victory after {day} days!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Gavant", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('All battles are finished')