import csv
import os

id_file = open("elites_ids_and_scores.csv", 'r')
reader = csv.reader(id_file)

elites = {}

# Our "elites" refers to the Twitter users other follow that might
# indicate someone's leaning. Get them all into a dict so they're
# easy to look up. (Using user_id because that's what we get from
# the API in the friends list.)
# Negative number == left leaning
# Positive number == right leaning
# 0 == Independent
# This is not quite as accurate as I'd like...
for row in reader:
    elites[int(row[1])] = float(row[2])

# This is where we'll put our results
results = open("results/friend_list_scores.csv", 'w')

# Each user we care about has a file with a friends list in the
# `user_friends` directory
# Friends list is an integer array delimited by newlines, so one
# file per user we are investigating
for filename in os.listdir("user_friends"):
    # Get the path for the current file
    f = os.path.join("user_friends", filename)
    # Make sure it's actually a file (since iterating a directory
    # might give us `.` or `..`)
    if os.path.isfile(f):
        # Open the file to read
        with open(f, 'r') as friends:
            # Default score, we'll add all the scores we find in
            # the id_and_scores csv
            score = 0
            # This reads in the full file and splits on newlines
            # to give us an array of integers
            friend_list = friends.read().splitlines()
            try:
                # Because we read it from a file, all our integers
                # are actually strings, so turn them into integers
                # and put them into an array
                id_list = [int(n) for n in friend_list]
                # Debugging, but it's fun to see stuff working
                print(id_list)
                # At the end of this loop, a 0 could be either no
                # matches *OR* independent. So keep track of whether
                # or not we had matches
                found_match = False
                # Now, check each id and see if it's in our elites dict
                for item in id_list:
                    # If it is, add it to the total score and indicate
                    # we found a match
                    if item in elites:
                        score += elites[item]
                        found_match = True
                # Printing for debugging
                print(f"{filename}: {score}")
                # Write it to a file
                results.write(f"{filename},{score},{found_match}\n")
            except ValueError:
                # If we got here, it's because the fine did not contain
                # an integer when we tried to get the list of follows.
                # This happens when the Account we're investigating
                # was protected or suspended or otherwise not available.
                results.write(f"{filename},N/A,N/A\n")

