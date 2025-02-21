import uuid
from datetime import datetime, timezone

# Define a class to represent an expense and initialize it with the required attributes
class Expense:
    def __init__(self, title, amount):
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

# Update the title and amount of the expense
    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

# Convert the expense object to a dictionary
    def to_dict(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "amount" : self.amount,
            "created_at" : self.created_at.isoformat(),
            "updated_at" : self.updated_at.isoformat()
        }

# Define a class to manage a database of expenses
class ExpenseDatabase:
    def __init__(self):

# Create an empty list to store expenses
        self.expenses = []
# Add an expense to the database
    def add_expense(self,expense):
        self.expenses.append(expense)

# Remove an expense from the database
    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
            break

# Get an expense by its Id
    def get_expense_by_id(self, expense_id):
        return next((expense for expense in self.expenses if expense.id == expense_id), None)

# Get all expenses with  given title
    def get_expenses_by_title(self, title):
        result = []
        for expense in self.expenses:
            if expense.title == title:
                result.append(expense)
        return result
    
# Convert the database to a list of dictionaries
    def to_dict(self):
        result =[]
        for expense in self.expenses:
            result.append(expense.to_dict())
        return result
    




# Applying the above code with examples

db = ExpenseDatabase()
expense1 = Expense("clothes", 10000.0)
expense2 = Expense("Perfume", 12000.0)

db.add_expense(expense1)
db.add_expense(expense2)

print(db.to_dict())

expense1.update(title="New clothes")

print(db.to_dict())

db.remove_expense(expense2.id)
print(db.to_dict())

next_expense = db.get_expense_by_id(expense1.id)
print(next_expense.to_dict())

expenses = db.get_expenses_by_title("New clothes")
print([expense.to_dict() for expense in expenses])
