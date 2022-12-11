# Preparing Elite IDs and Scores for Checking User Following Lists

These CSVs and TSVs were taken from the [new-tweetscores](https://github.com/sdmccabe/new-tweetscores) and [twitter-ideology](https://github.com/pablobarbera/twitter_ideology) repos.

`phi-ideal-oints-201807.csv` was used as found except all columns but the phi score and the Twitter usernames were removed

For all others, all columns except party and twitter handle were removed. Search replace was used to turn party affiliation into a score:
```
-1.1 Green party
-1.0 Democratic party
 0.0 Independent
 1.0 Republican party
 1.1 Libertarian party
 1.2 Constitution party
```

Then, all rows (except from `phi-ideal-points-201807.csv`) were put into a single document and sorted, removing duplicates.

Final files (without ids) are: `raw_tweetscores/cleaned/compiled.csv` and `raw_tweetscores/cleaned/phi_ideal_points_cleaned.csv`

The Twitter API then was used to get the user ids for each handle, and both files were combined into `elites_ids_and_scores.csv` in the root directory.
