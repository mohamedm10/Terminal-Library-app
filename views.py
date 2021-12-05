# user interaction with the system

# when program starts ask user for choice between loggin in, register
## after he is logged in for normal users show: his fine, and the books he has, and time on each book
## for librarian show options: rent a book, book return, search for user who have had books for long time


def menu_1():
    options = """
    Welcome to the Library Management System.
    please select an option to proceed:
    1. Login In
    2. Sign Up
    """
    print(options)
    choice = input('>>> ')
    return choice

def register():
    print('please provide your name and contact to register.')
    print('Name:')
    name = input('>>> ')
    print('Contact details:')
    contact = input('>>> ')
    return name,contact

def user_menu(name='mohamed'):
    print(f'welcome {name}')
    options = """
    please select an option.
    1. view books
    2. show fine 
    """
    print(options)
    choice = input('>>> ')
    return choice

def librarian_menu(name='librarian'):
    print(f'welcome {name}')
    options = """
    please select an option.
    1. lend a book
    2. book returns
    3. books report(with time) 
    """
    print(options)
    choice = input('>>> ')
    return choice

if __name__ == '__main__':
    menu_1()
    register()