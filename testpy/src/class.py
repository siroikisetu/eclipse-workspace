#coding=utf-8

class Person:
    def SayHello(self):
        print("hello world,I'm {name}".format(name=self.__name))
    def __init__(self,name):
        self.__name = name

a=Person("blessing")
a.SayHello()

