# 1
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_car_info(self):
#         return f" the make of this car is: {self.make} the model of the car is: {self.model} The year it was created {self.year}"
    
# car1 = Car("Toyota", "Corola", 2019)
# print(car1.make, car1.model, car1.year)

# print(car1.get_car_info())

# car1.color = "blue"
# print(car1.color)

# del car1.color
# print(car1.color)


# 2
# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0.0):
#         self.holder = account_holder
#         self.balance = initial_balance

#     def transfer_founds(self, other_account, amount):
#         if amount <= 0:
#             print("trasfer failed: the amount must be positive number")
#             return
#         if self.balance >= amount:
#             self.balance -= amount
#             other_account.balance += amount
#             print(f"Transfer successful! {amount:.2f} transferred from {self.holder} to {other_account.holder}.")
#         else:
#             print(f"Transfer failed: {self.holder} has an insufficient balance.")  

#     def __str__(self):
#         return f"Acounts Holder: {self.holder}, Current Balance: {self.balance}"

# acount1 = BankAccount("shlomo", 1000.0)
# acount2 = BankAccount("ben", 500.0)
# print(acount1)
# print(acount2)

# transfer_amount = 250.00
# acount1.transfer_founds(acount2, transfer_amount)
# print("acount status after trensfer:")
# print(acount1)
# print(acount2)

# 3
# class Point:
#     count = 0
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1

#     def __del__(self):
#         Point.count -= 1
    
#     def show(self):
#         print(f"({self.x}, {self.y})")
    

# if __name__ == '__main__':    
#     p1 = Point(10, 20)
#     p1.show()
#     print("there are", Point.count, "points")
#     p2 = Point(44, 50)
#     p2.show()
#     print("there are", Point.count, "points")
#     p3 = p2
#     print("there are", Point.count, "points")

#     del p1
#     print("there are", Point.count, "points")
#     del p2
#     print("there are", Point.count, "points")

    # @staticmethod
    # def distance(p1, p2):
    #     dx = p1.x - p2.x
    #     dy = p1.y - p2.y
    #     return (dx**2 + dy**2) ** 0.5
    
# if __name__ == '__main__':
#     p1 = Point(10, 20)
#     p2 = Point(13, 24)
#     d = Point.distance(p1, p2)
#     print("Distance between points:", d)

    # @classmethod
    # def how_many(cls):
    #     print("There are", cls.count, "points")

# if __name__ =='__main__':
#     p1 = Point(10, 20)
#     p1.show
#     Point.how_many()
#     p2 = Point(44, 55)
#     p2.show
#     p2.how_many()

# class Line:
#     count = 0
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
    
#     def show(self):
#         print(f"({self.a}, {self.b})")

# p1 = Point(10, 20)
# p2 = Point(30, 40)
# distance1 = Point.distance(p1, p2)
# print(distance1)
# p1.show()
# p2.show()
    # def __count__(self):
    #     Line.count += 1

    # @classmethod
    # def how_many(cls):
    #     print("There are", cls.count, "Lines")

    # @staticmethod
    # def is_horizontal(line1, line2):
    #     return line1.y == line2.y

# line1 = Point(1, 4)
# line2 = Point(3, 5)
# print(Line.is_horizontal(line1, line2))

#     @staticmethod
#     def is_vertical(line1, line2):
#         return line1.x == line2.x
    
# line1 = Point(1, 4)
# line2 = Point(1, 7)
# print(Line.is_vertical(line1, line2))
