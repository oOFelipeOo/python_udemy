import re

enter_cpf = input('Digite o CPF: ').strip().replace('.', '').replace('-', '')

print('CPF informado:', enter_cpf)
    

def val_cpf():

    if len(enter_cpf) != 11:
        return print('CPF invalido')
    if enter_cpf == enter_cpf[0] * len(enter_cpf):
        return print('CPF invalido')
    if check_cpf(1, enter_cpf) == False:
        return print('CPF invalido')
    if check_cpf(2, enter_cpf) == False:
        return print('CPF invalido')
    print('CPF valido')
    

def check_cpf(num, cpf):
    
    if num != 1 and num != 2:
        return False
    
    result = 0
    r_9_10 = 9 if num == 1 else 10
    count_10_11 = 10 if num == 1 else 11
    
    for i in range(r_9_10):
        digit = int(cpf[i])
        result += digit * (count_10_11 - i)
        
    check_digit = (result * 10) % 11
    check_digit = 0 if check_digit == 10 else check_digit
    print(check_digit)
    
    if check_digit != int(cpf[r_9_10]):
        return False
    return True

val_cpf()