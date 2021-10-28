import praw
import time
reddit = praw.Reddit(client_id='Ku_eoUy2Tl2_QIS3ZXKIHg',
                      client_secret='opNzwCStqi5PWChRxxRJ88Zghen5rA',
                     user_agent='a reddit instance',
                    username='Right_Swing396',
                     password='sosinfo212')


import random
import time
def karma():
  try:
    messages = ["Upvoted, upvote in return?", "Great post, care to share the upvotes!"]
    """
    for i in range(5):
        reddit.subreddit("test").submit(random.randint(1,100), random.randint(1,100000000))
        time.sleep(3)"""
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
  except:
    time.sleep(300)
    karma()
karma()
