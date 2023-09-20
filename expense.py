from PyInquirer import prompt
from csv import writer

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },

]

main_option = {
        "type":"list",
        "name":"main_options",
        "message":"New Expense - Spender: ",
        "choices": []
    }

people_involved = {
        "type":"list",
        "name":"people_involved",
        "message":"New Expense - People involved: ",
        "choices": []
    }

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('users.csv', 'r') as file:
        names = [line.strip() for line in file]
    
    main_option['choices'] = names
    spender = prompt(main_option)

    names.append("Done")
    people_involved['choices'] = names
    involved_user = []
    while True:
        user = prompt(people_involved)
        if (user['people_involved']) == "Done":
            break

        selected_user = user['people_involved']
        names.remove(selected_user)

        involved_user.append(selected_user)



    amount = float(infos['amount'])
    if(len(involved_user) == 0):
        print("No user selected !")
        return False

    with open('event.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([amount, infos['label'], spender['main_options'], involved_user])
        f_object.close()
    print("Expense Added !")
    return True
