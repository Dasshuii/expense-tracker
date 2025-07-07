import datetime

class Expense():
    def __init__(self, id = None, description = None, amount = 0, date = None):
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        self.id = id
        self.date = date or now
        self.description = description
        self.amount = amount
    
    def to_csv(self):
        return [self.id, self.date, self.description, self.amount]
    
    @staticmethod
    def from_csv(data):
        return Expense(id = int(data[0]), date = data[1], description = data[2], amount = data[3])
    
    def __str__(self):
        return f'{self.id}  {self.date}  {self.description}  ${self.amount}'
