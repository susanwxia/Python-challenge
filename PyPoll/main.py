import csv
import os
csvpath = os.path.join("Resources", "election_data.csv")
txt_output = os.path.join("Analysis", "Pypoll_output.txt")
election_result = open(txt_output,"w")

with open(csvpath) as csvfile:
    csv_election = csv.reader(csvfile, delimiter=',')
    csv_header1 = next(csv_election)
    data_vote = list(csv_election)
    line_count = 0
    name_list = []
    can_vote = []
    
    for row in data_vote:
        line_count += 1
        if line_count == 1:
            name_list.append(row[2])
        elif (row[2] not in name_list):
            name_list.append(row[2])
    print("Election Results\n--------------------------------")
    print(f'Total Votes: {line_count}\n--------------------------------')
    election_result.write("Election Results\n--------------------------------\n")
    election_result.write(f'Total Votes: {line_count}\n--------------------------------\n')

    for i in range(len(name_list)):
        can_total = 0
        for candidate in data_vote:
            if candidate[2] == name_list[i]:
                can_total += 1    
        can_vote.append(can_total)
        can_percentage = can_total/line_count
        print(f'{name_list[i]}: {round((can_percentage)*100)}.000% ({can_total})')
        election_result.write(f'{name_list[i]}: {round((can_percentage)*100)}.000% ({can_total})\n')

    winner_index = can_vote.index(max(can_vote))
    print("--------------------------------")
    print(f'Winner: {name_list[winner_index]}')
    election_result.write("--------------------------------\n")
    election_result.write(f'Winner: {name_list[winner_index]}')