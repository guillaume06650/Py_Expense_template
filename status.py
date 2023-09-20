from PyInquirer import prompt
from csv import writer

def add_user():
    
    with open('users.csv', 'r') as file:
        names = [line.strip() for line in file]
    print(names)
    return