import argparse

parser = argparse.ArgumentParser(
    prog = 'expense-tracker',
    description = 'Keep track of all your expenses!'
)

# Subparsers
subparsers = parser.add_subparsers(dest = 'action', required = True)

# add parser
parser_add = subparsers.add_parser('add', help = 'Add an expense.')
parser_add.add_argument('-d', '--description', help = 'Expense description.', type = str)
parser_add.add_argument('-a', '--amount', help = 'Expense amount.', type = int)

# list parser
parser_list = subparsers.add_parser('list', help = 'List all expenses.')

# Summary parser
parser_summary = subparsers.add_parser('summary', help = 'Total expenses.')
parser_summary.add_argument('-m', '--month', type = int, choices = range(1, 13), help = 'Specific month summary')

# Delete subparser
parser_delete = subparsers.add_parser('delete', help = 'Delete an expense.')
parser_delete.add_argument('-i', '--id', type = int, help = 'Expense id.')



