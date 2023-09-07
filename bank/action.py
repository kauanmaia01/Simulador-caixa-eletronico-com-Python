from datetime import datetime
import os

class Operation:
    def __init__(self, name, number_account, opening_balance=0.0):
        self.name = name
        self.number = number_account
        self.balance = opening_balance

    def view_balance(self):
        os.system('clear')
        print()
        print(f"{'='* 16} EXTRATO CONTA BANCO XYC {'=' *16}")
        print()
        print(f"CONSULTA                 {datetime.now()}")
        print("CONTA:", self.number)
        print("TITULAR:", self.name)
        print()
        print(f"SALDO ATUAL:............ R${self.balance:,.2f}")

    def deposit(self, value):
        self.balance += value
        os.system('clear')
        print()
        print(f"Depósito de R${value:.2f} realizado. Saldo atual: R${self.balance:.2f}")

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            os.system('clear')
            print()
            print(f"Saque de {value} realizado. Saldo atual: {self.balance}")
        else:
            os.system('clear')
            print()
            print(f"Saldo insuficiente para saque. Seu saldo atual é de R${self.balance:.2f}")
    
    def __str__(self):
        return f"Conta: {self.number} | Titular: {self.name} | Saldo: R${self.balance}"