class Awtobus:
    def __init__(self, speed, capacity, maxSpeed, passengers_names, hasEmptySeats, passengers):
        self.speed = speed
        self.capacity = capacity
        self.passengers = passengers
        self.maxSpeed = maxSpeed
        self.passengers = passengers

    def kogo_visadit(self, passengers, hasEmptySeats):
        print('Сколько людей убрать')
        gets_passengers = int(input())
        if gets_passengers > self.passengers:
            print('no')
            self.hasEmptySeats = True
        else:
            self.passengers -= gets_passengers


    def posadit_passagirov(self, passengers, capacity):
        print('Взять кого-нибудь?')
        print('Да/нет')
        choice = str(input())
        if choice.lower() == 'да':
            print('Сколько нужно добавить пассажиров?')
            pass_new = int(input())
            if  self.capacity - self.passengers == 0:
                print('Нет мест')
                self.hasEmptySeats = False
            else:
                self.passengers += pass_new
                self.hasEmptySeats = True
        else:
            print('Едем далее')

    def navalit_speed(self, speed):
        if self.speed == self.maxSpeed:
            print('Куда наваливаете, сбавьте обороты')
        else:
            print('Навалить:')
            novai_speed = int(input())
            if self.speed + novai_speed <= self.maxSpeed:
                self.speed += novai_speed
            else:
                print('Невозможно')

    def sbavet_speed(self, speed):
        print('На сколько сбросить скорость?')
        visaqe = int(input())
        self.speed -= visaqe
        if self.speed < 0:
            print('Начните движение, пассажиры ждут')
            self.speed += 1


    def main():
        awtobus = Awtobus(9, 134, 2456, 130)
        navalit_speed()
        sbavet_speed()
        posadit_passagirov()
        kogo_visadit()
        print(awtobus.speed)

main()