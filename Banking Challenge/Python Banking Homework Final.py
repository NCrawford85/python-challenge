

import os
import csv
#import csv file
csv_path = os.path.join('budget_data.csv')
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    next(csvreader)
    
    #create variable for profit
    profit = 0
    
    #create list variables to count months, profit, and profit change
    month_count = []
    profit_count = []
    profit_change = []

    #add the month and profit row values to populate the lists
    for row in (csvreader):
    
        month_count.append(str(row[0]))
    
        profit_count.append(int(row[1]))

    #find total months and total profit
    total_profit = sum(profit_count)
    total_months = len(month_count)
    
    #make an i loop to populate list for profit change
    for i in range(1,len(profit_count)):
        profit_change.append(profit_count[i] - profit_count[i-1])
        
    #determine average change, greatest profit, and greatest change
        greatest_profit = max(profit_change)
        greatest_loss = min(profit_change)
        average_change = sum(profit_change)/len(profit_change)
        average_change = round(average_change, 2)
    #make variables for months
    greatest_month = ""
    loss_month = ""
    #make a loop to find months for greatest loss and profit
    for j in range(len(profit_change)):
        if profit_change[j] == greatest_profit:
            greatest_month = month_count[j+1]
        if profit_change[j] ==greatest_loss:
            loss_month = month_count[j+1]
    
    print(f'Financial Analysis')
    print(f'-------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase In Profits: {greatest_month} (${greatest_profit})')
    print(f'Greatest Decrease In Profits: {loss_month} (${greatest_loss})')   
    
with open("Financial Analysis.txt","w") as text_file:
    print(f'Financial Analysis',file=text_file)
    print(f'-------------------')
    print(f'Total Months: {total_months}',file=text_file)
    print(f'Total: ${total_profit}',file=text_file)
    print(f'Average Change: ${average_change}',file=text_file)
    print(f'Greatest Increase In Profits: {greatest_month} (${greatest_profit})',file=text_file)
    print(f'Greatest Decrease In Profits: {loss_month} (${greatest_loss})',file=text_file)  
text_file.close()

   
