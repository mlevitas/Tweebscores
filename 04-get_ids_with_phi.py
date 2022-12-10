import tweepy
import csv

keys = json.load(open("keys.json"))
bearer_token = keys["API2"]["bearer_token"]

tweepy_client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# with open("raw_tweetscores/cleaned/phi_ideal_points_cleaned.csv", 'r') as ids:
with open("raw_tweetscores/cleaned/final/compiled.csv", 'r') as ids:
    with open("raw_tweetscores/compiled_with_ids.csv", 'w') as out:
        reader = csv.reader(ids)
        writer = csv.writer(out)
        for row in reader:
            user_name = row[0]
            score = row[1]
            try:
                user = tweepy_client.get_user(username=user_name)
                user_id = user.data.id
                print(f"{user_name} with {score} {user_id}")
                out.write(f"{user_name},{user_id},{score}\n")
            except Exception as e:
                print(f"{e}")
            continue