# user interaction with the system

# when program starts ask user for choice between loggin in, register
## after he is logged in for normal users show: his fine, and the books he has, and time on each book
## for librarian show options: rent a book, book return, search for user who have had books for long time

import datetime
import re

def menu_1():
    options = """
    Welcome to the Library Management System.
    please select an option to proceed:
    1. Login In
    2. Sign Up (normal user)
    3. Sign Up (librarian)
    4. exit program
    """
    print(options)
    choice = input('>>> ')
    return choice

def login_details():
    print('please input your email: ')
    email = input('>>> ')
    return email

def register():
    print('please provide your name and email to register.')
    print('Name:')
    name = input('>>> ')
    print('email:')
    email = input('>>> ')
    return name,email

def user_menu(name='mohamed'):
    print(f'welcome {name}.')
    options = """
    please select an option.
    1. view books
    2. show fine
    3. logout
    """
    print(options)
    choice = input('>>> ')
    return choice

def librarian_menu(name='librarian'):
    print(f'welcome {name} the Librarian.')
    options = """
    please select an option. b to go back to previous menu
    1. lend a book
    2. book returns
    3. calculate fines
    4. register a new book 
    """
    print(options)
    choice = input('>>> ')
    return choice

def book_registration():
    print('please provide:')
    name = input('Book name? ').strip()
    author = input('Book author? ')
    pub_company = input('Publishing company? ')
    return name,author,pub_company

def failed_login():
    print('Sorry it seems your are not registered!')
    print('Would you like to register now?')
    prompt_answer = input('Y/N: ')
    return prompt_answer

def success_registration():
    print ('You have been successfully registered!, please login')
    return

def redirection():
    print ('You will be redirected to the main menu, please select 2/3')
    return


# FUNCTIONS
#######################################
# function to take in date string from sqlite and give out datetime object of the string

def str_to_dt(string):
    '''
    par: string_date : in the form 'YYYY-MM-DD'
    returns: date_borrowed type: datetime format: YYYY-MM-DD
    '''
    str_list = string.split('-')
    int_list = [int(date) for date in str_list]
    date_borrowed = datetime.date(int_list[0],int_list[1],int_list[2])
    return date_borrowed

# function to calculate fine by calculating the diff between dates

def book_fine(borrowed_date):

    """
    par: takes in borrowed_date from sqlite : in the form 'YYYY-MM-DD'
    returns: fine type: int 
    """
    
    date_borrowed = str_to_dt(borrowed_date)
    fine = 0
    count = 0
    diff = datetime.date.today()-date_borrowed
    ##########
    diff = str(diff)
    print(diff)
    # use the compile class \d+ for a group of nums followed by a space
    reg = re.compile(r'(\d+) ')
    diff = reg.findall(diff)
    if len(diff)>0:
        diff = int(diff[0])
        ##########
        # diff = str(diff).split()[0]
        # diff = int(diff)
        if diff>20:
            for i in range(20,diff+1,5):
                print(i)
                count+=1
            print('n of 5days=',count-1)    
            print('5 days fine=',(count-1)*5)
            fine = 20+(count-1)*5
            print('total fine=',fine)
            if fine>0:
                return fine
            else:
                return None
        return 0
    return 0

#######################################