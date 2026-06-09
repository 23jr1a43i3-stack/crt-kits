class Employee:
    def bonus(self):
        print("Bonus: ₹5000")

class Manager(Employee):
    def bonus(self):
        print("Bonus: ₹20000")

m = Manager()
m.bonus()