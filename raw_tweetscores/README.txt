These CSVs and TSVs were taken from the new-tweetscores and twitter-ideology repos.

phi-ideal-oints-201807.csv was used as found except all columns but the phi score and the twitter handles were removed

For all others, all columns except party and twitter handle were removed. Search replace was used to turn party affiliation into a score:
-1.1 Green party
-1.0 Democratic party
0.0 Independent
1.0 Republican party
1.1 Libertarian party
1.2 Constitution party

All rows were put into a single document and sorted, removing duplicates.

The Twiter API was used to get the user ids for each handle.

Final file is: ids_and_scores/ids_and_scores.csv