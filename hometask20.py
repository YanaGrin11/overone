# 14.7
class House:

    def __init__(self, flat):
        self.flat = flat

    def hiring(self):
        print(f'A janitor is hired in this house')

# 14.8
class Salon:
    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time

    def manicure(self):
        pass

    def hairstyle(self):
        pass

# 14.9
    def salon_opening_hours(self, now_time):
        if now_time < self.open_time or now_time > self.close_time:
            print(f'The shop is closed')
        else:
            print(f'The shop is open')

class HouseWithSalon (Salon, House):
    def __init__(self, flat, open_time, close_time):
        super(HouseWithSalon, self).__init__(open_time, close_time)

if __name__ == '__main__':
    hws = HouseWithSalon(124, 10, 21)
    print(hws.__dict__)
    now_time = int(input('Enter the time: '))
    hws.salon_opening_hours(now_time)
