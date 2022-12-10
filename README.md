# Tweebscores
COMM-751 final project

## Script execution order
1. 01-collect_userdata.py
   - Extracts PFP files as username.jpg and creates CSV file with user_id and username
2. 02-keywords.py
   - Finds keywords in profile text and designates users in CSV file as is_otaku TRUE/FALSE
3. 03-get_friends.py
   - Generates text files (new line delimited) friends (following) lists (user_ids only) for each user
4. 04-get_ids_with_phi.py
   - Retrieves user_ids for elites in Tweetscores elites file
5. 05-actual_compare.py
   - Compares friends lists of participants with Tweetscores elites file; adds had_match (TRUE/FALSE)
      to show if a friends list had a match in the elites file
