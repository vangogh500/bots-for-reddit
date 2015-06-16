# Custom Bots for Reddit by Vangogh500

##Overview
reddit-bots contains custom reddit bots

##Change Log
* Added Azubu notification bot

##Provided
### Azubu Notification Bot
[Source](scripts/azubu-notification-bot/main.py) - [Profile](http://www.reddit.com/user/CJEntus_Bot)

Azubu Notification Bot is a custom script used by rCJEntus_Bot on /r/CJEntus.
The script checks a list of streams on Azubu.tv to see if they are currently live.
Depending on the statuses of these streams and the bot's submission history, the script will make a post on a given subreddit with the information.

####Dependencies
* Python - 2.7.9
* Python Reddit API Wrapper (PRAW)

##Installing
To use this script, download main.py file and any dependencies for the appropriate bot. Using cron job, windows task scheduler, etc run the script at any frequency which suits you. Personally, I am using a scheduler on heroku to run the script every 10 minutes.

##License
The code is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)
