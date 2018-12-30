import gettext
import sys

# es = gettext.translation('main', localedir='locale', languages=['es'])
# es.install()

_ = gettext.gettext

clients = 'pablo,ricardo,'


def create_client(client_name):   
    global clients   

    if client_name in clients:
        print(_('Client already is in the client\'s list'))
    else:
        clients += client_name
        _add_comma()


def list_clients():    
    print(clients)
    

def _add_comma():
    global clients

    clients += ','



def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')        
    else:
        print(_('The client {} is not in client\'s list'.format(client_name)))


def update_client(client_name, new_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, new_client_name)
    else:
        print(_('The client {} is not in client\'s list'.format(client_name)))


def _print_welcome():
    print('*' * 50)
    print(_('WELCOME TO PLATZI VENTAS'))
    print('*' * 50)
    print(_('What would you like to do today?'))
    print(_('[C]reate client'))
    print(_('[L]ist clients'))
    print(_('[D]elete client'))
    print(_('[U]date client'))
    print(_('[E]xit'))



def print_options():
    print(_('Select an opction [C]reate [L]ist [U]pdate [D]elete [E]xit'))


def get_client_name():
    return input(_('What is the client name?  '))

if __name__ == '__main__':
    _print_welcome()
    
    command = ''

    while not command == 'E':
        command = input().upper()        
        if command == 'C':
            client_name = get_client_name()
            create_client(client_name)     
            list_clients()       
        elif command == 'L':
            list_clients()        
        elif command == 'D':
            client_name = get_client_name()
            delete_client(client_name)
            list_clients()          
        elif command == 'U':
            client_name = get_client_name()
            new_client_name = input(_('What is the new client name?  '))
            update_client(client_name, new_client_name)
            list_clients() 
        else:
            print(_('Invalid command...'))

        print_options()
            

    