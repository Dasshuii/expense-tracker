from manager.expense_manager import add, list_expenses, summary, delete
from cli import parser
from tools.tools import months

def main():
    args = parser.parse_args()

    match args.action:
        case 'add':
            id = add(args.description, args.amount)
            print(f'Expense added successfully (ID: {id})')
        case 'list':
            list_expenses()
        case 'summary':
            total = summary(args.month)
            print(f'Total expenses: ${total}' if not args.month else f'Total expenses for {months[args.month]}: ${total}')
        case 'delete':
            delete(args.id)
        case _:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    main()