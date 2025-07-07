from storage.data_manager import load_expenses, write_expense
from models.expense import Expense
from manager.expense_manager import add, list_expenses, summary, delete
from cli import parser
import datetime
import sys


def main():
    opt = input('Option: ')

    match opt:
        case 'add':
            description = input('Description: ')
            amount = int(input('Amount: '))
            id = add(description, amount)
            print(f'Expense added successfully (ID: {id})')
        case 'list':
            list_expenses()
        case 'summary':
            months = {
                1 : 'January',
                2 : 'February',
                3 : 'March',
                4 : 'April',
                5 : 'May',
                6 : 'June',
                7 : 'July',
                8 : 'August',
                9 : 'September',
                10 : 'October',
                11 : 'November',
                12 : 'December'
            }

            month = int(input('Month: '))
            total = summary(month)
            print(f'Total expenses: ${total}' if not month else f'Total expenses for {months[month]}: ${total}')
        case 'delete':
            id = input('expense id: ')
            delete(id)
        case _:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    main()