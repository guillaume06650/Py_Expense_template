from PyInquirer import prompt, Separator
import csv
from collections import defaultdict

def show_status():
    expenses = []
    with open('expense_report.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)
    
    user_contributions = {}
    user_balances = {}
    
    for expense in expenses:
        amount = float(expense[0])
        spender = expense[2]
        involved_users = expense[3].split(', ')
        
        if spender not in user_contributions:
            user_contributions[spender] = 0
        user_contributions[spender] += amount
        
        for user in involved_users:
            if user not in user_contributions:
                user_contributions[user] = 0
            user_contributions[user] -= amount
    
    for user, contribution in user_contributions.items():
        user_balances[user] = contribution
    
    report = []
    for user1 in user_balances:
        for user2 in user_balances:
            if user1 != user2:
                balance = user_balances[user1] - user_balances[user2]
                if balance > 0:
                    print(f"{user1} owes {balance:.2f}€ to {user2}")
