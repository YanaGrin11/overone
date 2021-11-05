# 14.1
class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def characteristic(self, jump, run, bark):
        print(f' The dog jumps {jump} meters')
        print(f' The dog runs {run} kilometers')
        print(f' The dog barks {bark} loudly')


if __name__ == '__main__':
    dog_1 = Dog(65, 7, 'Shark', 5)
    dog_1.characteristic(3, 2, 'wof')

print(dog_1.__dict__)


# 14.2

def change_name(self, new_name):
    self.new_name = new_name


new_name = input('New name for your dog ').title()
if __name__ == '__main__':
    dog_1 = Dog(65, 7, new_name, 5)

print(dog_1.__dict__)
