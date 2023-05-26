import os
import csv

#creating path to csv file and defining it as dict reader, setting delimiter
election_data_csv = os.path.join("Resources", "election_data.csv")

csv_file = open(election_data_csv, 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file, delimiter=",")
csv_header = next(csv_file)

cand_dict = {}
cand_list = []
#total number of votes
total_vote_IDs = 0
for row in csv_reader:
    total_vote_IDs += 1
    if row[2] not in cand_list:
        cand_list.append(row[2])
        cand_dict [row[2]] = 0
    cand_dict [row[2]] += 1
#print(f"Total number of voter IDs in database: {total_vote_IDs} ")
#print(f"There are {len(cand_list)} candidates who received votes; they are {cand_list} ")
#print(f"votes per candidate: {cand_dict}")

#percentage of votes each candidate won
percentages = {key: round((val / total_vote_IDs) * 100,3) for key, val in cand_dict.items()}
#print(f"Votes won by percent: {percentages}")
#print(f"The winner based on popular votes is {max(cand_dict)}")

output1 = (
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total_vote_IDs}\n"
f"-------------------------\n")
output2 =""
for k, v in cand_dict.items():
    output2 += (f"{k}: {percentages[k]}% ({v})\n")


output3 = (f"-------------------------\n"
f"Winner: {max(cand_dict,key=cand_dict.get)}\n"
f"-------------------------")
output = output1 + output2 + output3
print(output)

output_file = open("Analysis/election_analysis.txt", 'wt')
output_file.write(output)