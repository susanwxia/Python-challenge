import csv
import os
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csv_budget = csv.reader(csvfile)
    csv_header = next(csv_budget)
    line_count = 0
    profit_sum = 0
    profit_change = []
    profit_date = []
    for row in csv_budget:
        line_count += 1
        if line_count == 1:
            profit_currmon = int(row[1])
        profit_sum += int(row[1])
        change_mon = int(row[1]) - profit_currmon
        profit_change.append(change_mon)
        profit_currmon = int(row[1])
        profit_date.append(row[0])
    print(f'Financial Analysis\n----------------------')
    print(f'Total number of months: {line_count}')
    print(f'Total profit: ${profit_sum}')
    profit_avg = round(sum(profit_change)/(line_count-1),2)
    print(f'Average change: ${profit_avg}')
    profit_max = max(profit_change)
    max_index = profit_change.index(profit_max)
    max_date = profit_date[max_index]
    print(f'Greatest Increase in Profits: {max_date} (${profit_max})')
    profit_min = min(profit_change)
    min_index = profit_change.index(profit_min)
    min_date = profit_date[min_index]
    print(f'Greatest Decrease in Profits: {min_date} (${profit_min})')
txt_output = os.path.join("Analysis", "Pybank_output.txt")
budget_result = open(txt_output,"w")
budget_result.write(f'Financial Analysis\n----------------------\n')
budget_result.write(f'Total number of months: {line_count}\n')
budget_result.write(f'Total profit: ${profit_sum}\n')
budget_result.write(f'Total profit: ${profit_sum}\n')
budget_result.write(f'Average change: ${profit_avg}\n')
budget_result.write(f'Greatest Increase in Profits: {max_date} (${profit_max})\n')
budget_result.write(f'Greatest Decrease in Profits: {min_date} (${profit_min})\n')
