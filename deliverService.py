from os import system
system('clear')
import random


class Dish:
    menu = dict()

    def __init__(self, name, price ):
        self.name = name
        self.price = price
        # Dish.menu.update({self.name: self.price})

    def __add_food(self):
        self.menu.update({self.name: self.price})

    def __str__(self):      # menu ni ko'rish uchun
        for dish, price in self.menu.items():
            print(f"{dish} - ${price}")



class Order:
    order = []
    def __init__(self, meal, piece ):
        self.meal = meal
        self.piece = piece
        self.meal_id = random.randint(1000, 10_000)
        if self.meal in Dish.menu.keys():
            Order.order.append({self.meal: self.piece})
        else: raise Exception('Sorry, We dont have such meal!!!')
        # def make_report():
        #     return f"You ordered {self.piece} of {self.meal}. You charged ${self.piece * Dish.menu[self.meal]}"
        # print(make_report())

    def accept_order(self):
        return f"You ordered {self.piece} of {self.meal}. You charged ${self.piece * Dish.menu[self.meal]}"

    def __str__(self):
        return f"{self.meal} - {self.piece} piece"


class Customer:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel
        self.orders = []

    def __str__(self):
        return f"{self.name}\n{self.tel}\nOrdered: {[meal  if self.orders else None for meal in self.orders]}"

    def make_order(self, meal, piece):
        tempo_order = Order(meal, piece)
        self.orders.append({meal: f"{piece} piece"})
        print(tempo_order.accept_order())
        return f"Your orders: {[order for order in self.orders]}"


class DeliveryPerson:
    def __init__(self, name, vehicle_num):
        self.name = name
        self.vehicle_num = vehicle_num

    def __str__(self):
        return f"Name: {self.name}\nVehicle Number: {self.vehicle_num}"


class DeliverySystem:

    def take_order(self, customer):
        meal = input('Add meal: ')
        piece = int(input('How much you want: '))
        global order
        order = Order(meal, piece)

        customer.orders.append({meal: f"{piece} piece"} )
        return order.accept_order()

    def deliver_order(self, delivery_person):
        return (f"Your order is being delevered\n"
                f"Your order: {order}\n"
                f"your delivery person:\n"
                f"{delivery_person}")







dish1 = Dish('Burger', 13)
dish2 = Dish('Pizza', 25)
dish3 = Dish('Sandwich', 9)
dish4 = Dish('Cake', 45)
dish_list =  [dish2, dish1, dish3, dish4]

for dish in dish_list:
    dish._Dish__add_food()
#print(dish1)    # __str__

order1 = Order('Pizza', 2)
# print(order1.accept_order())
# print(order1.order)

customer = Customer('Alex', 998_99_123_45_67)
customer2 = Customer('Sherzod', 998941234567)
# print(customer.make_order('Pizza', 2))

delivery_person = DeliveryPerson('Miko', 'VN120M')
delivery_person2 = DeliveryPerson('Mario', 'M120TT')

sys = DeliverySystem()

print(sys.take_order(customer2))   # Deliverysystem class oqali buyurtma berish
print(customer2.orders)

print(sys.deliver_order(delivery_person2))




