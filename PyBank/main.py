# Print statement
print("Financial Analysis")
print("---------------------------")

# Import the os module
import os
# Module for reading CSV files
import csv

# Set path for file
budget_data = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'budget_result.txt')

# Define variables
number_of_months = 0
total = 0
column_name = 'Profit/Losses'
total_change = 0
previous_amount = None
difference = []
max_increase = 0
max_increase_date = ""
previous_profit = None
max_decrease = 0
max_decrease_date = ""
previous_loss = None

# Reading using CSV module
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # Defining the variable by using the length of the list
    number_of_months = len(list(csvreader))
    # Print statment of f-string of variable as an interger
    print(f"Total number of months: {int(number_of_months)}")

# Reading using CSV module
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Total = converting string numbers into floating in the second row of dataset, remove commas from the string
        total += float(row [1].replace(',',''))
    # Print statment of f-string of variable as an interger
    print(f"Total: ${int(total)}")

# Reading using CSV module
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Define variable as interger in row 1
        current_amount = int(row[1])
        # Conditional of variable is an integer
        if previous_amount is not None:
            # Calculating differece of variables with previously defined variables as interger
            subtraction = current_amount - previous_amount
            # Adding the difference to the end of the list
            difference.append(subtraction)
        # Defining previous amount is now the new current amount as the loop keeps going
        previous_amount = current_amount

# Using conditionals to find the average of the sum of the difference divided by the length of the diffecence list
if difference:
    average_differences = sum(difference)/len(difference)
    # Print statment of f-string of the average and rounding to the second decminal point
    print(f"Average change: ${round(average_differences, 2)}")

# Reading using CSV module
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Defining the variable as first column or position zero 
        date = row[0]
        # Defining the variable as second column or position one as an interger
        profit = int(row[1])
        # Conditional of variable is an integer
        if previous_profit is not None:
            # Defining variable as diffecent between previously defined variables
            increase = profit - previous_profit
            # Conditional statement if increase is greater than maximum increase 
            if increase > max_increase:
                # And the maximum increase equals to the increase
                max_increase = increase
                # Then that date corresponds to the maximum increase
                max_increase_date = date
        # Variable defined as new variable as the it loops through the data
        previous_profit = profit
    # Print statment of f-string of date corresponding to the greatest increase
    print(f"Greatest increase in profits: {max_increase_date}, ${max_increase}")   

# Reading using CSV module
with open(budget_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # For Loop loop through the contents
    for row in csvreader:
        # Defining the variable as first column or position zero
        date = row[0]
        # Defining the variable as second column or position one as an interger
        loss = int(row[1])
        # Conditional of variable is an integer
        if previous_loss is not None:
            # Defining variable as diffecent between previously defined variables
            decrease = loss - previous_loss
            # Conditional statement if decrease is greater than biggest decrease
            if decrease < max_decrease:
                # And the biggest decrease equals to the decrease
                max_decrease = decrease
                # Then that date corresponds to the biggest decrease 
                max_decrease_date = date
        # Variable defined as new variable as the it loops through the data
        previous_loss = loss
    # Print statment of f-string of date corresponding to the biggest decrease
    print(f"Greatest decrease in profits: {max_decrease_date}, ${max_decrease}")     

# Open the file using "write" mode. Specify the variable to hold the contents in an output file
with open(output_path, 'w') as output_file:
    
    # Print statment for the output file in text format
    print("Financial Analysis", file = output_file)
    print("---------------------------", file = output_file)
    print(f"Total number of months: {int(number_of_months)}", file = output_file)
    print(f"Total: ${int(total)}", file = output_file)
    print(f"Average change: ${round(average_differences, 2)}", file = output_file)
    print(f"Greatest increase in profits: {max_increase_date}, ${max_increase}", file = output_file) 
    print(f"Greatest decrease in profits: {max_decrease_date}, ${max_decrease}", file = output_file)  