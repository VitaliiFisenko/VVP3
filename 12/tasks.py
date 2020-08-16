

"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.

Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.

"""
from dataclasses import dataclass


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 0
    max_limit = 0
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.currency = 'UAH'
        self.curr_map = {'USD': 27.8}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, valoe):
        self.initial_amount += money

    def withdraw(self, amount):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        self.initial_amount -= amount
        return amount
