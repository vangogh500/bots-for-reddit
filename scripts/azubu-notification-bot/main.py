#!/usr/local/bin/python

# ---------------------------------------------------
# Azubu Notification Bot v1 for Reddit by Vangogh500
# ---------------------------------------------------


# import all necessary libraries
import praw
import time
from datetime import datetime
import urllib2

# the main variables
USERNAME = "CJEntus_Bot"
PASSWORD = ""
SUBREDDIT = "CJEntus"

channels = ["MadLife", "Shy", "Ambition", "CoCo", "Space"]

r = praw.Reddit("Azubu Stream announcer v1.1 by /u/vangogh500")
r.login(USERNAME, PASSWORD)

post = None
today = datetime.now()
date = "%s/%s/%s" %(today.month, today.day, today.year)

def scanIfOnline(channel):
	"""Returns if channel is live"""
	response = urllib2.urlopen('http://api.azubu.tv/public/channel/%s/info' %channel)
	html = response.read()
	if '"is_live":false' in html:
		return False
	elif '"is_live":true' in html:
		return True
	else:
		print ("Error with fetching channel")

def get_last_submission(reddit):
    """Returns the last submission with today's date in the title"""
    me = reddit.get_redditor("CJEntus_Bot")
    submissions = me.get_submitted()
    for submission in submissions:
        if date in str(submission):
            return submission
    return None

def get_were_online(channels,last_post):
    """Returns the a list of streamers that were online based on post"""
    were_online = []
    text = last_post.selftext
    for channel in channels:
        if channel in text:
            were_online.append(channel)
    return were_online

def get_curr_statuses(channels):
    """Returns a dictionary with the statuses of each streamer"""
    statuses = {}
    for channel in channels:
        statuses[channel] = scanIfOnline(channel)
    return statuses

def edit_post(statuses, date, were_online):
    print "editing post..."
    content = "**The following streams are now online:**\n\n---\n"
    for stream in statuses:
        if(statuses[stream]):
            link = "[stream](http://www.azubu.tv/%s)" %stream
            content = content + "* %s - %s\n" % (stream, link)
            were_online.remove(stream)
    if were_online:
        content = content + "\n\n**The following streams were online:**\n\n---\n"
        for stream in were_online:
            content = content + "* %s\n" % (stream)
    post.edit(text=content)
    post.set_flair(flair_css_class="live", flair_text="Live")
    post.sticky()

def make_post(statuses, date):
    title = "Streams for %s" % date
    content = "**The following streams are now online:**\n\n---\n"
    print "making post..."
    for stream in statuses:
        if(statuses[stream]):
            link = "[stream](http://www.azubu.tv/%s)" %stream
            content = content + "* %s - %s\n" % (stream, link)
    post = r.submit(SUBREDDIT, title, text=content)
    post.set_flair(flair_css_class="live", flair_text="Live")
    post.distinguish()
    post.sticky()

# Main body
post = get_last_submission(r)
statuses = get_curr_statuses(channels)
print statuses

if True in statuses.values():
    if(post != None):
        were_online = get_were_online(channels,post)
        edit_post(statuses,date,were_online)
    else:
        make_post(statuses,date)
else:
    if(post != None):
        were_online = get_were_online(channels,post)
        post.set_flair(flair_css_class="offline", flair_text="Offline")
        content = ""
        if were_online:
            content = content + "**The following streams were online:**\n---\n"
            for stream in were_online:
                content = content + "* %s\n" % (stream)
        post.edit(text=content)
        post.unsticky()