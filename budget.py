class Budget:
    def __init__(self, category: str):
        self.category = category
        self.amount = 0

    def deposit(self):
        amount = int(input('How much do you want to deposit?\n'))

        print(f'You have successfully deposited {amount}')

        self.amount += amount

    def withdraw(self):
        amount = int(input('How much do you want to withdraw?\n'))

        print(f'You have successfully withdrawn {amount}')

        self.amount -= amount

    def check_balance(self):
        print(f'Your current balance for {self.category} is {self.amount}')

    def transfer(self):
        amount = int(input('How much do you want to transfer?\n'))
        budget = input('Where do you want to transfer to?\n').lower()

        self.withdraw(amount)
        budget.deposit(amount)
        print(f'You have successfully transferred {amount} from {self.category} to {budget.category}')

clothing = Budget('Clothing')
food = Budget('Food')
entertainment = Budget('Entertainment')


