from clcrypto import check_password


class User:
    __id = None
    username = None
    __hashed_password = None
    email = None

    @staticmethod
    def get_user_by_email(email):
        return User()

    def save_to_db(self):
        pass

    def set_password(self, new_password):
        self.__hashed_password = new_password

    @property
    def hashed_password(self):
        return self.__hashed_password

    @staticmethod
    def get_all_users():
        return [User(), User()]


def create_user(email, password):
    user = User.get_user_by_email(email)
    if user:
        raise Exception("User Exists")
    else:
        user = User()
        user.email = email
        user.set_password(password)
        user.save_to_db()


def change_user_password(email, password, new_password):
    user = User.get_user_by_email(email)
    if user and check_password(password, user.hash_password) and len(new_password) > 8:
        user.set_password(new_password)
        user.save_to_db()


def delete_user(email, password):
    user = User.get_user_by_email(email)
    if user and check_password(password, user.hash_password):
        user.delete()


def display_all_user():
    user_list = User.get_all_users()
    for user in user_list:
        print(" %s %s " % (user.username, user.email))

