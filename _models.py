# all the data will be saved and queried from here
# tables in class forms, attributes = data , classmethod for user, classmethod for librarian, method for getting user name.
# i can use the attributes to get back user data as object attibutes eg: user_1.name 
## to do that i can save the query tuple to the object: name,contact,user_type = ('mahamed','0702070202','user')


class Users:
    def __init__(self,name,contact,user_type):
        self.name = name
        self.contact = contact
        self.user_type = user_type

    # create an instant normal user
    @classmethod
    def new_user(cls,name,contact,user_type='user'):
        return cls(name,contact,user_type)

    # create an instant librarian user
    @classmethod
    def new_librarian(cls,name,contact,user_type='librarian'):
        return cls(name,contact,user_type)

    def get_user(self,logged_in):
        pass
        # user = cur.execute('select name from user where name=? ;',(logged_in))
        # return user

