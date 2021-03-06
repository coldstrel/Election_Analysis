# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Initialize a county list
county_options = []
county_votes = {}
# Step two, initialize variables
largest_turnout_county = 0
votes_lt_county = 0
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # Get the county name from each row
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # If county name is not in the list, add the county name to the list
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for county_name in county_votes:
        c_votes = county_votes[county_name]
        cv_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {cv_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        # Determine which county won
        if(c_votes > votes_lt_county):
            largest_turnout_county = county_name
            votes_lt_county = c_votes
    county_summary = (
        f"-------------------------\n"
        f"County with more votes: {largest_turnout_county}\n"
        f"County percentage: {float(votes_lt_county) / float(total_votes) *100 :.1f}%\n"
        f"County number of votes: {votes_lt_county:,}\n"
        f"-------------------------\n")
    print(county_summary)
    txt_file.write(county_summary)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    