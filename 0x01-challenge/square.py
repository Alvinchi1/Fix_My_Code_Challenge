#!/usr/bin/python3

""" Module for Sqaure Class """

class Square():
    """ Square class """
    width = 0
    height = 0

    def _init_(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)


    def area_of_my_square(self):
        """ Area of the sqaure """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Periimeter of my square """
        return(self.idh * 2) + (self.height * 2)

    def _str_(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)



    if _name_ == "_main_":
        """ Create a square object """
        s = Sqaure(width=12, height=9)
        print(s)
        print(s.area_of_my_square())
        print(s.peremiter_of_my_square())
