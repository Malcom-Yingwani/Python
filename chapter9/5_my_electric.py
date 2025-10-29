# Import single class from module

from car_module import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()