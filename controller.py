# this is where the whole app is going to be connected sending stuff to db and back, calling display funcs and input funcs, giving logic to the app.

# imports
from views import book_registration, failed_login, librarian_menu, login_details, menu_1, redirection, success_registration, user_menu, register, book_fine
from models import User, Book, create_tables, rent_book,return_book
import time

# creates & connects the DB and creates tables
create_tables()
 
user_input = None             
while True:     # keep looping 
    user_input = menu_1()
# login option 
    if user_input=='1':
        email = login_details()
        # gets back user object if user in database
        user = User.user_login(email)
        # print(user)
        if user:
            # USER menu
            if user.user_type == 'user':
                choice = None
                while choice not in ['1','2','3']: # loop until you get one of the options
                    choice = user_menu(user.name)
                    if choice == '1':
                        # list all books that the user has borrowed
                        pass
                    elif choice == '2':
                        # show the user how much fine he has on his account
                        pass
                    elif choice == '3':
                        # go to main menu
                        pass
                    
                # LIBRARIAN menu
            elif user.user_type == 'librarian':
                lib_choice = ''
                while lib_choice !='b':
                    lib_choice = librarian_menu(user.name)
                    if lib_choice == '1': # when you are lending a book
                        Book.available_books()
                        rent_book()
                    elif lib_choice == '2': # when a user returns book
                        return_book()
                    elif lib_choice == '3': # calculate fines
                        pass
                        # get all the books which are borrowed
                        books = Book.getall_books()
                        # for each book get the rented_user_id, rented_date
                        for date,user_id in books: 
                            User.add_fine(user_id,fine=book_fine(date))
                        # call the book_fine(rented_date) to get fine 
                        # add fine to the user by calling User.add_fine(fine=book_fine(),rented_user_id)
                        
                    elif lib_choice == '4': # for regsitering a new book
                        name,author,pub_company = book_registration()
                        Book.new_book(name,author,pub_company)

        # if user is not in database               
        else:
            ans = ''
            while ans != 'Y' or ans !='N':
                ans = failed_login()
                if ans == 'Y':
                    redirection()
                    time.sleep(2)
                    break
                elif ans =='N':
                    exit()

# create a normal user
    elif user_input=='2':
        name,email = register()
        User.create_user(name,email)
        success_registration()

# create a librarian user
    elif user_input =='3':
        name,email = register()
        User.create_librarian(name,email)
        success_registration()
        
# terminate program
    elif user_input == '4':
        exit()





