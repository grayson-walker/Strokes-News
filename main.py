# Import the email modules we'll need
import sys
import praw
from sendEmail import sendEmail
import time

# Initialize PRAW (Reddit API wrapper) with a custom User-Agent
#r = connection to reddit
r = praw.Reddit(
        client_id='',
        client_secret='',
        password='',
        user_agent='',
        username='')

strokesNews = []   # to avoid duplicates
posts = r.subreddit('theStrokes').comments(limit= 400)
for comment in posts:
    post = comment.body.lower()
    if (post.find("strokes") != -1 and post.find("new") != -1) or (post.find("strokes") != -1 and post.find("tour") != -1):
        strokesNews.append(post)
        time.sleep(2)   # Sleep for 2 seconds



print("The new strokes news is: ")
print('----------------------------------------------------------------------------------------')
print(len(strokesNews))

#Judge 3 instances of "new" Strokes comments to be worthy of emailing
if len(strokesNews)>3:
    sendEmail(strokesNews)




