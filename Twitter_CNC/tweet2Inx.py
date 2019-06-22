'''
Function to Pass Tweet Info to an Inkscape Inx File
'''

def tweet2Inx():
    
    from twython import Twython
    import random
    import string
    import textwrap 

    # Twitter Dev Keys
    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''

    # Twitter Object
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    # Control Variables
    charFlag = 0
    endFlag = 0

    # Choose Random Twitter User from List
    nameList = ['@realDonaldTrump','kanyewest','@bobatl','@katyperry','@justinbieber',\
                '@taylorswift13', '@BarackObama', '@ArianaGrande', \
                '@selenagomez', '@KimKardashian']
    
    twitterName = random.choice(nameList)
    print(twitterName)
    
    # Pull Recent Tweets
    tweets=twitter.get_user_timeline(screen_name= twitterName, count = 100)
    
    # Select 1st Tweet without Retweets, Media Links, Emoticons, Etc.
    tweetCounter = 0
    
    while(endFlag == 0):
        tweet = tweets[tweetCounter]
        print(tweet['text'])
        if 'http' not in tweet['text'] and len(tweet['text']) < 125:
            for c in tweet['text']:
                if ord(c) > 128:
                    charFlag = 1
                    
            if charFlag == 0:      
                tweetText = tweet['text']
                tweetText=tweetText.replace('RT','')
                tweetUser = tweet['user']['screen_name']
                tweetDateRough = tweet['created_at']
                endFlag = 1
            else:
                charFlag = 0
        
        tweetCounter += 1
    
    # Parse Tweet Date
    tweetDate = tweetDateRough[4:10] + tweetDateRough[-5:]
    tweetDate = tweetDate[:6] + ',' + tweetDate[6:]
    monthDict = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr" : "April", \
                 "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", \
                 "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
    tweetDate = tweetDate.replace(tweetDate[0:3],monthDict[tweetDate[0:3]])
    
    # Split Tweet Text into Lines
    tweetText1 = tweetText2 = tweetText3 = tweetText4 = tweetText5 = ''
	
    #Text Wrapper
    wrapper = textwrap.TextWrapper(width=30) 
    wordList = wrapper.wrap(text=tweetText)
    print(len(wordList))
    print(wordList[0])
    
    # Split Text Based on Size of WordList    
    if len(wordList)-1 == 0:
        tweetText1 = wordList[0]
    elif len(wordList)-1 == 1:
        tweetText1 = wordList[0]
        tweetText2 = wordList[1]
    elif len(wordList)-1 == 2:    
        tweetText1 = wordList[0]
        tweetText2 = wordList[1]
        tweetText3 = wordList[2]
    elif len(wordList)-1 == 3:  
        tweetText1 = wordList[0]
        tweetText2 = wordList[1]
        tweetText3 = wordList[2]
        tweetText4 = wordList[3]
    else:    
        tweetText1 = wordList[0]
        tweetText2 = wordList[1]
        tweetText3 = wordList[2]
        tweetText4 = wordList[3]
        tweetText5 = wordList[4]
    
    # Printing
    print('-----')
    print('Tweet #%d of 100' %  (tweetCounter))
    print(tweetText1)
    print(tweetText2)
    print(tweetText3)
    print(tweetText4)
    print(tweetText5)
    print(tweetUser,'\n',tweetDate)
    
    # Write Tweet into Inx File
    inxIn = open('blank.inx', 'r')
    inxOut = open('twitterCNC.inx', 'w')
    for line in inxIn:
        inxOut.write(line.replace('dateText',tweetDate).replace('nameText', tweetUser)\
        .replace('bodyText1', tweetText1).replace('bodyText2',tweetText2)\
        .replace('bodyText3', tweetText3).replace('bodyText4', tweetText4)\
        .replace('bodyText5', tweetText5))

    inxIn.close()
    inxOut.close()
    
    # Move Inx File to Extension Folder
    import subprocess
    import time
    
    c1 = 'cp'
    c2 = '-r'
    c3 = 'twitterCNC.inx'
    c4 ='/home/pi/.config/inkscape/extensions'
    
    process = subprocess.Popen([c1, c2, c3, c4])
    
