This project is a simple expense tracking system created in python using object oriented programming principles. it allow users to add, remove, and update their expenses. it was developed using the object-oriented programming principles, it has two classes for Expense and ExpenseDatabase. 
the attributes for class Expense: include 
id: A unique identifier generated as a UUID string. 
title: A string representing the title of the expense. 
amount: A float representing the amount of the expense. 
created_at: A timestamp indicating when the expense was created (UTC). 
updated_at: A timestamp indicating the last time the expense was updated (UTC). 
Method used for class Expense: 
init: Initializes the attributes. 
update: Allows updating the title and/or amount, 
updating the updated_at timestamp. 
to_dict: Returns a dictionary representation of the expense. 
Method used for class ExpenseDatabase: 
init: Initializes the list. add_expense: 
Adds an expense. remove_expense: 
Removes an expense. get_expense_by_id: 
Retrieves an expense by ID. 
get_expense_by_title: Retrieves expenses by title. 
to_dict: Returns a list of dictionaries representing expenses.

To use this project, clone my repository on https://github.com/Uju24/First_Project.git and run the expense.py file
