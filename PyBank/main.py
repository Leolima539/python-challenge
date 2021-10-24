import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

# Set Variables
month_count = 0
total_amount = 0
amount_difference = []
month_index = []

# Open File
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Remove header  
    csv_header = next(csv_reader)

    # Use next again to gather first month information
    first_row = next(csv_reader)
    # Set first month values.
    total_amount += int(first_row[1])
    last_month = int(first_row[1])
    # count the first month
    month_count += 1
    
    for row in csv_reader:

        # Set Column 2 as Integer
        this_month = int(row[1])
        # Count month
        month_count += 1
        # Sum Revenue to total amount
        total_amount += this_month
        # Find change between month and previous
        month_difference = this_month - last_month
        # Save difference to list
        amount_difference += [month_difference]
        # Set column 2 value as last amount for next iteration
        last_month = this_month
        # Keep Track of months
        month_index += [row[0]]
    


    # Sum all values from change list to find total change
    total_change = sum(amount_difference)
    # Find average change 
    average_change = round(total_change / month_count,2)
    # index the best and worst month
    best_month = month_index[amount_difference.index(max(amount_difference))]
    worst_month = month_index[amount_difference.index(min(amount_difference))]

    # Write new file
with open('analysis/Bank_analysis.txt', 'w') as f:

    f.write("Financial Analysis\n")
    f.write("-------------------\n")
    f.write(f"total months: {month_count}\n")
    f.write(f"Total: ${total_amount}\n")
    f.write(f"Average change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {best_month} ${max(amount_difference)}\n")
    f.write(f"Greatest Loss in Profits: {worst_month} ${min(amount_difference)}\n")

# Print Everything!
print("Financial Analysis")
print("-------------------")
print(f"total months: {month_count}")
print(f"Total: ${total_amount}")
print(f"Average change: ${average_change}")
print(f"Greatest Increase in Profits: {best_month} ${max(amount_difference)}")
print(f"Greatest Loss in Profits: {worst_month} ${min(amount_difference)}")

