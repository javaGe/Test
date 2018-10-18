# coding=utf-8
# import requests
#
# params = {'username':'15813081353'}
# rsp = requests.get("http://14.23.86.58:8444/access/rest/v200/user/get", params=params)
# rsp.encoding = 'utf-8'
# print(rsp.json())

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hi, my name is', self.name)

if __name__ == '__main__':
    person = Person('ggf')
    person.say_hi()
