# Import the email modules we'll need
import sys
import praw
from sendEmail import sendEmail
import time

# Initialize PRAW (Reddit API wrapper) with a custom User-Agent. 
# Insert your own reddit client information here
# r = connection to reddit
r = praw.Reddit(
        client_id='',
        client_secret='',
        password='',
        user_agent='',
        username='')

strokes_news = [] 
# Get the last 400 comments in the r/theStrokes subreddit
posts = r.subreddit('theStrokes').comments(limit= 400)
for comment in posts:
    post = comment.body.lower()
    if (post.find("strokes") != -1 and post.find("new") != -1) or (post.find("strokes") != -1 and post.find("tour") != -1):
        strokes_news.append(post)
        time.sleep(2)   # Sleep for 2 seconds



print("The new Strokes news is: ")
print('----------------------------------------------------------------------------------------')
print(strokes_news)

# Judge 3 instances of "new" Strokes comments to be worthy of emailing
if len(strokes_news)>3:
    sendEmail(strokes_news)




