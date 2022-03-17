from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balances = [None] + balance
        self.naccounts = len(balance)

    def has_money(self, i, amount):
        return True if 1 <= i <= self.naccounts and self.balances[i] >= amount \
            else False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.has_money(account1, money) and self.has_money(account2, 0):
            self.balances[account1] -= money
            self.balances[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.has_money(account, 0):
            self.balances[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.has_money(account, money):
            self.balances[account] -= money
            return True
        return False