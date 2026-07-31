import re
import hashlib

class Account:
    def __init__(self, username: str, password: str, national_id: str, phone: str, email: str) -> None:
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.national_id = self.id_validation(national_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)

    def username_validation(self, username: str) -> str:
        pattern = r'^[a-zA-Z]+_[a-zA-Z]+$'

        if not re.match(pattern, username):
            raise ValueError("Invalid username.")

        return username

    def password_validation(self, password: str) -> str:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

        if re.match(pattern, password):
            hashed = hashlib.sha256(password.encode('utf_8')).hexdigest()

            return hashed

        else:
            raise ValueError("Invalid password.")
        

    def id_validation(self, id: str) -> str:
        sum = 0
        counter = 10
        avg = 0

        if len(id) == 10 and id.isdigit():
            ls = list(id)

            for i in range(9):
                sum += (int(ls[i]) * counter)
                counter -= 1

            avg = sum % 11

            if avg < 2:
                check = (avg == int(ls[9]))

            else:
                check = ((11 - avg) == int(ls[9]))

            if not check:
                raise ValueError("Invalid national id.")

            else:
                return id

        else:
            raise ValueError("Invalid national id.")

    def phone_validation(self, phone: str) -> str:
        if re.match(r'^09[0-9]{9}$', phone) or re.match(r'^\+989[0-9]{9}$', phone):
            ls = list(phone)

            if ls[0] == '0':
                return phone
            else:
                for _ in range(3):
                    ls.pop(0)
                ls.insert(0, '0')

                return ''.join(ls)
        else:
            raise ValueError("Invalid phone number.")

    def email_validation(self, email: str) -> str:
        pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,5}$'

        if re.match(pattern, email):
            return email
        else:
            raise ValueError("Invalid email.")

    def set_new_password(self, password: str) -> None:
        self.password = self.password_validation(password)

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

class Site:
    def __init__(self, url_address: str) -> None:
        self.url = url_address
        self.registered_users = []
        self.active_users = []

    def register(self, user: Account) -> str:
        if user in self.registered_users:
            raise ValueError("User already registered.")
        else:
            self.registered_users.append(user)
            return "Register successful."

    def login(self, username: str = None, email: str = None, password: str = None) -> str:
        hashed_password = hashlib.sha256(password.encode('utf_8')).hexdigest()

        for user in self.registered_users:
            match = False

            if email is None and username is not None:
                if user.username == username and user.password == hashed_password:
                    match = True
            elif email is not None and username is None:
                if user.email == email and user.password == hashed_password:
                    match = True
            elif email is not None and username is not None:
                if user.email == email and user.username == username and user.password == hashed_password:
                    match = True

            if match:
                if user in self.active_users:
                    return "User already logged in."
            
                self.active_users.append(user)
                return "Login successful."

        return "Invalid login."

    def logout(self, user) -> str:
        if user in self.active_users:
            self.active_users.remove(user)
            return "Logout successful."
        else:
            return "User is not logged in."

    def __repr__(self):
        return f"Website URL: {self.url}\nRegistered users: {self.registered_users}\nActive users: {self.active_users}"

    def __str__(self):
        return self.url



def show_welcome(func):

    def wrapper(user):
        username = user.username
        username = username.replace('_', ' ')
        username = username.title()
        if len(username) > 15:
            username = username[:15] + '...'

        return func(username)

    return wrapper



def verify_change_password(func):

    def verify(user, old_pass, new_pass):
        hashed_old_pass = hashlib.sha256(old_pass.encode('utf_8')).hexdigest()
        if user.password != hashed_old_pass:
            raise ValueError("Incorrect old password.")
        else:
            user.set_new_password(new_pass)

        return func(user, old_pass, new_pass)

    return verify


@show_welcome
def welcome(user):
    return f"Welcome to our website {user}!"


@verify_change_password
def change_password(user, old_pass, new_pass):
    return "Your password has been changed successfully."