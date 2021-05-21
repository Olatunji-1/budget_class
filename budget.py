class Budget:
    def __init__(self, category: str, amount: float):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        print(f'You have successfully deposited {amount}')
        self.amount += amount

    def withdraw(self, amount):
        print(f'You have successfully withdrawn {amount}')
        self.amount -= amount

    def check_balance(self):
        print(f'Your current balance for {self.category} is {self.amount}')

    def transfer(self, obj, amount):
        self.withdraw(amount)
        obj.deposit(amount)
        print(f'You have successfully transferred {amount} from {self.category} to {obj.category}')


Food = Budget("Food", 90)
Clothes = Budget("Clothes", 10)

Food.transfer(Clothes, 9)
print("Food amount:",Food.amount)
print("Clothes amount:",Clothes.amount)
