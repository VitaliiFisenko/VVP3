#  ATM
class CurrencyMixin:
    # перевожу все в гривну

    def __init__(self, amount, USD_rate=27.8, EUR_rate=32.2):
        self.amount = amount
        self.USD_rate = USD_rate
        self.EUR_rate = EUR_rate

    def chosen_currency(self, USD_rate=27.8, EUR_rate=32.2):
        chosen_currency = input("Choose the currency to convert UAH: \n1)EUR \n2)USD \n3)UAH\n\n")

        if chosen_currency == "1":
            EUR_amount = round(float(input("How many EUR do you want to add/get?\n")))
            amount = EUR_amount * EUR_rate
            return amount

        elif chosen_currency == "2":
            USD_amount = round(float(input("How many USD do you want to add/get?\n")))
            amount = USD_amount * USD_rate
            return amount

        elif chosen_currency == "3":
            UAH_amount = round(float(input("How many UAH do you want to add/get??\n")))
            amount = UAH_amount
            return amount
        else:
            print("Error, please try again. \nEnter 1 for USD, 2 for RUB or 3 for GBP.")


class Account(CurrencyMixin):
    min_limit = 0
    max_limit = 100000000
    bank_name = 'Mono'

    def __init__(self, amount, balance=0):
        self.balance = balance
        super().__init__(amount)

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        self.balance -= amount

    def add_money(self, amount):
        self.balance += amount

    def __str__(self):
        return self.balance


def main():
    acc = Account(100, 10000)
    while True:
        print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

        selection = int(input("\nEnter your selection: "))
        if selection == 1:
            a = acc.balance
            print(f'Your balance is {a}')


        # Withdraw
        elif selection == 2:
            amount = acc.chosen_currency()
            acc.withdraw(amount)
            print("\nUpdated Balance: " + str(acc.balance) + " n")


        # Deposit
        elif selection == 3:
            amount = acc.chosen_currency()
            acc.add_money(amount)
            print("\nUpdated Balance: " + str(acc.balance) + " n")

        elif selection == 4:
            print("Transaction is now complete.")
            print("Thanks for choosing us as your bank")
            exit()

        # Any other choice
        else:
            print("That's an invalid choice.")


# COLOBOK


class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    pass


class Babka(Hero):
    def bake_colobok(self):
        return Colobok('Kolobok')


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None

    def babkin_dom(self):
        self.ded.tel_babka_about_colobok()
        self.colobok = self.babka.bake_colobok()

    def start(self):
        self.babkin_dom()


my_tail = Tale('L', ';')

my_tail.start()
