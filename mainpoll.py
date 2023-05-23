import os
import csv
from csv import DictReader

#creating path to csv file and defining it as dict reader, setting delimiter
election_data_csv = os.path.join("Resources", "election_data.csv")

csv_file = open(election_data_csv, 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file, delimiter=",")
csv_header = next(csv_file)

#total number of votes
total_vote_IDs = 0
for row in csv_reader:
    total_vote_IDs += 1
print(f"Total number of voter IDs in database: {total_vote_IDs} ")

#list of candidates who received votes
runnersup = []
candidate = 0
#create empty list for runners up, find each unique value in "Candidate" column, print list
for candidate in range(2, row("Candidate")):
    runnersup.append(candidate)
print(f"There are (len{runnersup}) candidates who received votes; they are {runnersup} ")

#total number of votes each candidate won
#loop through rows to count how many times each candidates name is listed

count = 0
#for balet in range(0, row("ballot ID"))
#while ballot = runnersup[0]:
#count += ballot
#elseif end

#percentage of votes each candidate won

#winner of election based on popular vote
#print candidate w highest percent

#export text file w results