import random

num_generator = [str(random.randint(0, 9)) for i in range(9)]



def generate_cpf():
        
    result_1 = 0
    result_2 = 0
    
    for i in range(9):
        digit = int(num_generator[i])
        result_1 += digit * (10 - i)
        
    check_digit = (result_1 * 10) % 11
    check_digit = 0 if check_digit == 10 else check_digit
    num_generator.append(check_digit)
    print(check_digit)
    
    for i in range(10):
        digit = int(num_generator[i])
        result_2 += digit * (11 - i)
        
    check_digit = (result_2 * 10) % 11
    check_digit = 0 if check_digit == 10 else check_digit
    print(check_digit)
    num_generator.append(check_digit)
    
    return num_generator
    
generate_cpf()

cpf = ''.join(map(str, num_generator))
print(cpf)