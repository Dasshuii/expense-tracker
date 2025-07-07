from models.expense import Expense
from storage.data_manager import load_expenses, write_expense, write_expenses
import datetime

expenses = [Expense.from_csv(expense) for expense in load_expenses()]

def add(description, amount):
    id = _get_next_id()
    write_expense(Expense(id, description, amount, datetime.datetime.now().strftime('%Y-%m-%d')).to_csv())
    return id


def _get_next_id():
    return max((expense.id for expense in expenses), default = -1) + 1

def list_expenses():
    print('ID  Date  Description  Amount')
    for expense in expenses:
        print(expense)

def summary(month = None):
    sum = 0
    if not month:
        for expense in expenses:
            sum += int(expense.amount)
    else:
        month = '0' + str(month) if month < 10 else str(month)
        for expense in expenses:
            if expense.date.split('-')[1] == month:
                sum += int(expense.amount)
    return sum

def delete(id):
    for expense in expenses:
        if expense.id == int(id):
            expenses.remove(expense)
            break
    
    new_expenses_csv = [expense.to_csv() for expense in expenses]
    write_expenses(new_expenses_csv)
