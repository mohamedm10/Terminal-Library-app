
# imports
from views import book_registration, delete_book_message, delete_book_prompt, delete_user_message, delete_user_prompt, failed_login, librarian_menu, login_details, menu_1, redirection, success_registration, user_menu, register, book_fine, edit_book, edit_user
from models import User, Book, create_tables, rent_book,return_book, connect_db
import time

# creates & connects the DB and creates tables
create_tables()
conn = connect_db()
 
user_input = None             
while True:     # keep looping 
    user_input = menu_1()
# login option 
    if user_input=='1':
        email = login_details()
        # gets back user object if user in database
        user = User.user_login(conn,email)
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
                        # update user details
                        # take an input of name and email
                        selected_user, new_name, new_email = edit_user(user.name)
                        # get the user
                        user = User.get_user(conn,selected_user)
                        # execute a model class method for updating the details
                        User.edit_user(conn,user.id, new_name, new_email)  
                        
                    elif choice == '3':
                        # go to main menu
                        pass
                    elif choice == '4':
                        # logged in user to delete his account
                        selection = delete_user_prompt(user.name)
                        if selection == 'y':
                            User.delete_user(conn,user.email)
                            delete_user_message()
                            break
                        else:
                            pass

                # LIBRARIAN menu
            elif user.user_type == 'librarian':
                lib_choice = ''
                while lib_choice !='b':
                    lib_choice = librarian_menu(user.name)
                    if lib_choice == '1': # when you are lending a book
                        Book.available_books(conn)
                        rent_book()
                    elif lib_choice == '2': # when a user returns book
                        return_book(conn)
                    elif lib_choice == '3': # calculate fines
                        # get all the books which are borrowed
                        books = Book.getall_books(conn)
                        # for each book get the rented_user_id, rented_date
                        for date,user_id in books: 
                            User.add_fine(conn,user_id,fine=book_fine(date))
                        # call the book_fine(rented_date) to get fine 
                        # add fine to the user by calling User.add_fine(fine=book_fine(),rented_user_id)
                        
                    elif lib_choice == '4': # for regsitering a new book
                        name,author,pub_company = book_registration()
                        Book.new_book(conn,name,author,pub_company)
                    elif lib_choice == '5':
                        # update book details author, publication company
                        selected_book, new_name, new_author, new_pub_company = edit_book()
                        # get book
                        book = Book.get_book(conn,selected_book)
                        # update book record
                        Book.edit_book(conn,book.id,new_name, new_author, new_pub_company)
                    elif lib_choice == '6':
                        # list all books that can be removed
                        Book.available_books(conn)
                        # delete a book from system
                        selected_book = delete_book_prompt()
                        Book.delete_book(conn,selected_book)
                        delete_book_message()
                        
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
        User.create_user(conn,name,email)
        success_registration()

# create a librarian user
    elif user_input =='3':
        name,email = register()
        User.create_librarian(conn,name,email)
        success_registration()
        
# terminate program
    elif user_input == '4':
        exit()





