import gettext
import sys

# es = gettext.translation('main', localedir='locale', languages=['es'])
# es.install()

_ = gettext.gettext

clients = [
    {
        'name': 'Pablo               ',
        'company': 'Google              ',
        'email': 'pablo@google.com    ',
        'position': 'Software Engineer   ',
    },
    {
        'name': 'Ricardo             ',
        'company': 'Facebook            ',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer       ',
    },
]


def create_client(client):
    global clients

    if client in clients:
        print(_('Client already is in the client\'s list'))
    else:
        clients.append(client)


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print(_('The client {} is not in client\'s list'.format(client_name)))


def update_client(client_name, new_client_name):
    global clients

    if client_name in clients:
        clients[clients.index(client_name)] = new_client_name
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


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(_('What is the client {}? '.format(field_name)))

    return field


def _get_client():
    return {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }


if __name__ == '__main__':
    _print_welcome()

    command = ''

    while not command == 'E':
        command = input().upper()
        if command == 'C':
            create_client(_get_client())
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
