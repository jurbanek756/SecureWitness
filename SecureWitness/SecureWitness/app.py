import requests
from SecureWitness import views
from requests.auth import HTTPBasicAuth
#from django.contrib.auth.models import Group
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required

def login():
    with requests.Session() as c:
        url = 'http://127.0.0.1:8000'
        username = input('Enter User: ')
        password = input('Enter Password ')
        c.get(url)
        csrftoken = c.cookies['csrftoken']
        payload = dict(csrfmiddlewaretoken=csrftoken, user=username, usrpass= password, Login='Login')
        c.post(url, data=payload)
        c.get(

        )
    # requests.get('http:/127.0.0.1:8000/Welcome', auth=HTTPBasicAuth('user', 'pass'))
    # if user is not None and user.is_active:
    #     print("Login Successful")
    #     return 1
    # else:
    #     print("Login Failed")
    #     choice = input("Enter L to attempt to login again or E to exit")
    #     if choice == 'L' or 'l':
    #         login()
    #     elif choice == 'E' or 'e':
    #         print("Exiting. Have a nice day")
    #         return 0
    #     else:
    #         print("Trying to be smart? Well I'm exiting anyway")
    #         return 0

if __name__ == '__main__':
    print("Please login before proceeding")
    login()


