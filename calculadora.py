def somar (a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def menu():
    a = int(input("primeiro valor: "))
    opcao = input("+ : somar\n- : subtrair\n* :  multiplicar\n/ : dividir\n")
    b = int(input("segundo valor: "))
    
    if opcao == '+':
        print(somar(a,b))
    elif opcao == '-':
        print(subtrair(a,b))
    elif opcao == '*':
        print(multiplicar(a,b))
    elif opcao == '/':
        print(dividir(a,b))
    else:
        print('operador inválido, tente novamente')
        menu()
        
menu()