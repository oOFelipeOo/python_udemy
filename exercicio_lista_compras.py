import os

buy_list = []



def insert_item():
    buy_list.append(input('Adicione: '))
    
    
    
def remove_item():
    item= input('Remova o item: ').strip()
    if not item:
        print('Nenhum item informado.')
        return
    try:
        idx = int(item)
        remove = buy_list.pop(idx)
    except ValueError:
        print('Digite um número válido.')
    except IndexError:
        print('Item não existe na lista.')
    else:
        print('Removido:', remove)      
    
    

def show_list():
    for idx, item in enumerate(buy_list):
        print(idx, item)



while True:
    show_list()
    print('Selecione uma opção')
    enter = input("[i]nserir    [a]pagar    [s]air: ")
    if enter == 'i' or enter == 'I':
         insert_item()
    elif enter == 'a' or enter == 'A':
        remove_item()  
    elif enter == 's' or enter == 'S':
        print('Saindo...')
        break  
    else:
        print('Digite i, a ou s apenas')
        
        
print('Obrigado por usar a lista de compras!')