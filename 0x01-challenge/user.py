#!/usr/bin/python3
""" User Class """




class User():
    """ Documentation """

    def _init_(self):
        """ Documentation """
        self._email = None


    @property
    def email(self):
        """ Docmentation """
        return self._email


    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be string")
        self._email = value



if _name_ == "_main_":

    u = user()
    u.email = "john@snow.com"
    print(u.email)
