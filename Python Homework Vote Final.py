import os
import csv
csv_path = os.path.join('election_data.csv')
with open(csv_path, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #keep header columns
    header = next(csvreader)
    
    #set candidate votes list variable
    candidate_list = [] 
    candidate_votes = []
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Otooley_votes = 0

    #count candidate votes
    for row in csvreader:

        candidate_votes.append(str(row[2]))
    candidate_list = set(candidate_votes)
    candidates = list(candidate_list)

    #determine candidates from cadidate list
    #print(candidates)
    
    for i in range(1,len(candidate_votes)):
        if candidate_votes[i] == 'Khan':
            Khan_votes = Khan_votes + 1
        elif candidate_votes[i] == 'Correy':
            Correy_votes = Correy_votes + 1
        elif candidate_votes[i] == 'Li':
            Li_votes = Li_votes + 1
        elif candidate_votes[i] == "O'Tooley":
            Otooley_votes = Otooley_votes + 1
    total_votes = len(candidate_votes)
    
    #determine candidate vote percentages
    Khan_percent = (Khan_votes/total_votes)*100
    Khan_percent = round(Khan_percent,4)
    Li_percent = (Li_votes/total_votes)*100
    Li_percent = round(Li_percent, 4)
    Correy_percent = (Correy_votes/total_votes)*100
    Correy_percent = round(Correy_percent, 4)
    Otooley_percent = (Otooley_votes/total_votes)*100
    Otooley_percent = round(Otooley_percent,4)
    
    #Determine election winner
    winner_count = {'Khan':Khan_votes, 'Correy': Correy_votes, "Li": Li_votes, "O'Tooley": Otooley_votes}
    election_winner = max(winner_count, key = winner_count.get)
    
    print(f'Election Results')
    print(f'----------------')
    print(f'Total Votes: {total_votes}')
    print(f'----------------')
    print(f'Khan: {Khan_percent}% ({Khan_votes})')
    print(f'Correy: {Correy_percent}% ({Correy_votes})')
    print(f'Li: {Li_percent}% ({Li_votes})')
    print(f"O'tooley: {Otooley_percent}% ({Otooley_votes})")
    print(f'Winner: {election_winner}')
    
with open("Election Results.txt","w") as text_file:
    print(f'Election Results',file=text_file)
    print(f'----------------',file=text_file)
    print(f'Total Votes: {total_votes}',file=text_file)
    print(f'----------------',file=text_file)
    print(f'Khan: {Khan_percent}% ({Khan_votes})',file=text_file)
    print(f'Correy: {Correy_percent}% ({Correy_votes})',file=text_file)
    print(f'Li: {Li_percent}% ({Li_votes})',file=text_file)
    print(f"O'tooley: {Otooley_percent}% ({Otooley_votes})",file=text_file)
    print(f'Winner: {election_winner}',file=text_file)   
text_file.close()