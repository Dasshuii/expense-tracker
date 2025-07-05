from storage.data_manager import load_expenses, write_expense

def main():
    expenses = load_expenses()
    print(expenses)
    write_expense()

if __name__ == '__main__':
    main()