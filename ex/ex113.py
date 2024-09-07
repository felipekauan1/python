def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except ValueError:
            print('\033[31mERRO: Digite um número INTEIRO!\033[0m')
        except KeyboardInterrupt:
            print('\033[33mO usuário preferiu não digitar esse número!\033[0m')
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except Exception as erro:
            print(f'\033[31m{erro.__class__}: Digite um número REAL!\033[0m')
        except KeyboardInterrupt:
            print('\033[33mO usuário preferiu não digitar esse número!\033[0m')
        else:
            return real


print(f'O número INTEIRO digitado foi {leiaInt('Digite um Inteiro: ')} e o REAL foi {leiaFloat('Digite um Real: ')}')
