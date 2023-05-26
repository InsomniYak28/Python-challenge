#import data
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

csv_file = open(budget_data_csv, 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file, delimiter=",")
csv_header = next(csv_file)

#total number of months in datbase
total_months = 0
for row in csv_reader:
    total_months += 1
print(f"Total number of months in database: {total_months} months ")

#net total amount of profit/losses over entire period
prof_loss = []
for i in range(1, len("Profit/Losses")):
    prof_loss.append(i)
net_revenue = sum(prof_loss)
revenue_formated = "${:,.2f}".format(net_revenue)
print(f"The net total revenue is {revenue_formated} ")

#changes in profit/losses over entire period, then average of those changes

compare_prof_loss = []
value = 0
for i in range(1, len("Profit/Losses")):
    value += i+1
    compare_prof_loss.append(value)
average_changes = sum(compare_prof_loss)/len(compare_prof_loss)
average_formated = "${:,.2f}".format(average_changes)
print(f"The average changes in profits and losses from month to month is {average_formated} ")

#greatest increase in profits
greatest_increase = max(compare_prof_loss)
increase_formated = "${:,.2f}".format(greatest_increase)
print(f"the greatest increase in profit was {increase_formated} ")

#greatest decrease in profits
greatest_decrease = min(compare_prof_loss)
decrease_formated = "${:,.2f}".format(greatest_decrease)
print(f"the greatest decrease in profit was - {decrease_formated} ")

#export text file
output = (
f"Finacial Results\n"
f"-------------------------\n"
f"Total Months: {total_months}\n"
f"Total Revenue: {revenue_formated} \n"
f"Average Change: {average_formated}\n"
f"Greatest increase in profits: {increase_formated}\n"
f"Greatest decrease in profits: -{decrease_formated}")
print(output)
output_file = open("Analysis/bank_analysis.txt", 'wt')
output_file.write(output)