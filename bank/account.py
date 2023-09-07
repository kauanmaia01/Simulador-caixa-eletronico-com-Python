from bank.action import Operation
import time
import os

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_accounts(self, name, number_account, opening_balance=0.0):
        if number_account not in self.accounts:
            new_account = Operation(name, number_account, opening_balance)
            self.accounts[number_account] = new_account
            print()
            print(f"Conta {number_account} criada para {name}.")
        else:
            print()
            print("Está conta já existe!")
    
    def initial_operations(self):
        os.system('clear')
        while True:
            print("\nEscolha uma opção:")
            print("1. Criar conta")
            print("2. Acessar conta")
            print("3. Sair")

            try:
                user_choice = int(input("Opção: "))

                if user_choice == 1:
                    user_name = input("Nome do titular: ")
                    user_account = input("Número da conta: ")
                    user_balance = float(input("Saldo inicial: ").replace('.', ''))
                    self.create_accounts(user_name, user_account, user_balance)

                elif user_choice == 2:
                    numbers_account = input("Número da conta: ")
                    if numbers_account in self.accounts:
                        self.access_account(numbers_account)
                    else:
                        print("Conta não encontrada.")

                elif user_choice == 3:
                    print()
                    print("Saindo do simulador de banco.")
                    break

                else:
                    print("Opção inválida.")
                    
            except ValueError:
                print("Por favor, insira um número válido.")    
    
    def access_account(self, number_account):
        os.system('clear')
        account = self.accounts[number_account]
        print()
        print(f"Acessando conta {number_account} de {account.name}.")

        while True:
            print("\nEscolha uma operação:")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Consultar saldo")
            print("4. Voltar")

            try:
                user_option = int(input("> "))

                if user_option == 1:
                    value = float(input("Valor a depositar: ").replace('.', '').replace(',', ''))
                    if value != " ":
                        account.deposit(value)  

                elif user_option == 2:
                    value = float(input("Valor do saque: ").replace('.', '').replace(',', ''))
                    if value != " ":
                        account.withdraw(value)
                
                elif user_option == 3:
                    account.view_balance()
                
                elif user_option == 4:
                    print()
                    print("Voltando para o menu principal.")
                    time.sleep(1)
                    os.system('clear')
                    break

                else: 
                    print("Operação inválida.")

            except ValueError:
                    print("Por favor, insira um número válido.")
            
