####################################################################################

class Vetyfication:

    def __init__(self, login, passwrd):
        self.login = login
        self.passwrd = passwrd
        self.__len_true()

    def save_pswd(self):
        with open('users.txt', 'a') as file:
            file.write(f' * Login:{self.login} Password:{self.passwrd} *' + '\n')

    def format_db(self, resh):
        self.resh = resh
        if resh == 'Yes':
            open('users.txt', 'w').close()

    def __len_true(self):
        if len(self.passwrd) < 8:
            raise ValueError('Слишком короткий пароль')

##########################################################################################