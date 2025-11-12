from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information for each submision
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {'title': response_dict['title'],
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key = itemgetter("comments"), reverse = True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict["comments"]}")

# =====================================================================================================
# Chat GPT SUMMARY
# =====================================================================================================
# Purpose:
#   - Fetches and displays the top Hacker News submissions using the Hacker News API.
# =====================================================================================================
# Core Functionality:
#   - Retrieves a list of top story IDs from the Hacker News API.
#   - Makes individual API requests for the first 5 stories.
#   - Extracts each story’s title, discussion link, and comment count.
#   - Sorts the stories by number of comments (descending).
# =====================================================================================================
# Output:
#   - Prints each story’s title, Hacker News link, and total comments.
#   - Displays HTTP status codes for API calls to verify successful requests.
# =====================================================================================================
