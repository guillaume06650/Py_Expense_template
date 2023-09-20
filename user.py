from PyInquirer import prompt
from csv import writer

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New user -- Name:",
    },
]

def add_user():
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([infos['name']])
        f_object.close()
    print("User Added !")
    # This function should create a new user, asking for its name
    return