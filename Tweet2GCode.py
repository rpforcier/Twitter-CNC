def Tweet2Svg():
    from twython import Twython
    import re

    #Twitter Dev Keys
	

    #Twitter Object
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    #Variables
    charFlag = 0
    endFlag = 0
    twitterName = '@bobatl' #@realDonaldTrump ,kanyewest, @bobatl
    tweetText = ''

    #Pull Recent Tweets
    tweets=twitter.get_user_timeline(screen_name= twitterName, count = 500)

    #Filter Tweets
    for tweet in tweets:
        #Filter Out Tweets with Retweets, Media, Emoticons, Etc.
        if 'RT' not in tweet['text'] and 'http' not in tweet['text']:
            for c in tweet['text']: 
                if c > '\uFFFF':
                    charFlag = 1
                    
            if charFlag == 0 and endFlag == 0:        
                tweetText = tweet['text']
                endFlag = 1

    #Convert Tweet into SVG File
    svgIn = open('blank.svg', 'r')
    svgOut = open('tweet.svg', 'w')
    for line in svgIn:
        svgOut.write(re.sub(r'flowPara\d{1,5}”>(.*?)','rflowPara16″>Kanye', line))
    svgIn.close()
    svgOut.close()

Tweet2Svg()
print(tweetText)

'''
#Convert SVG File to GCode
import subprocess
import time

c1 = ‘inkscape’
c2 = ‘tweet.svg’
c3 = ‘–verb’
c4 = ‘EditSelectAll’
c5 = ‘–verb’
c6 = ‘ObjectToPath’
c7 = ‘–verb’
c8 = ‘EditDeselect’
c9 = ‘–verb’
c10 = ‘ru.cnc-club.filter.gcodetools_orientation_no_options_no_preferences.noprefs’
c11 = ‘–verb’
c12 = ‘ru.cnc-club.filter.gcodetools_tools_library_no_options_no_preferences.noprefs’
c13 = ‘–verb’
c14 = ‘EditSelectAll’
c15 = ‘–verb’
c16 = ‘ru.cnc-club.filter.gcodetools_ptg.noprefs’
c17 = ‘–verb’
c18 = ‘FileSave’
c19 = ‘–verb’
c20 = ‘FileQuit’

process = subprocess.Popen([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16])
time.sleep(30)
process.kill()

#Convert GCode to Steps
global xyzPos
xyzPos = []
xyzSteps = []
stepsPerMm = 10
'''
'''
def Gcode2Steps():
endFlag = 0
line = []
xPos = 0
yPos = 0
zPos = 0
xSteps = 0
ySteps = 0

f = open(‘tweet_0001.gcode’ , ‘r’)
line = str(f.readline())

while (endFlag == 0):

#Stop Reading at End of File
if line == ”:
endFlag = 1;

#Read Only Move Lines
if ‘G0’ in line:
#print(line, end=”)

#Extract X
if ‘X’ in line:
xPos = float(line[(line.index(‘X’)+1):(line.index(‘X’)+7)])
xyzPos.append(xPos)
else:
xyzPos.append(xPos)

#Extract Y
if ‘Y’ in line:
yPos = float(line[(line.index(‘Y’)+1):(line.index(‘Y’)+7)])
xyzPos.append(yPos)
else:
xyzPos.append(yPos)

#Extract Z
if ‘Z’ in line:
if float(line[(line.index(‘Z’)+1):(line.index(‘Z’)+4)]) > 0:
zPos = 0
elif float(line[(line.index(‘Z’)+1):(line.index(‘Z’)+4)]) 0:
zPos = 0
elif float(line[(line.index(‘Z’)+1):(line.index(‘Z’)+4)]) 0:
motorDirectionX = Adafruit_MotorHAT.FORWARD
else:
motorDirectionX = Adafruit_MotorHAT.BACKWARD

if ySteps > 0:
motorDirectionY = Adafruit_MotorHAT.FORWARD
else:
motorDirectionY = Adafruit_MotorHAT.BACKWARD

st1 = threading.Thread(target=stepper_worker, args=(myStepper1, abs(xSteps), motorDirectionX, motorStepping))
st1.start()
print(“Thread 1 Started”)
st2 = threading.Thread(target=stepper_worker, args=(myStepper2, abs(ySteps), motorDirectionY, motorStepping))
st2.start()
print(“Thread 2 Started”)

while (xDeadFlag == 0 or yDeadFlag == 0):
if not st1.isAlive():
xDeadFlag = 1
print(“Dead Flag 1 Raised”)
if not st2.isAlive():
yDeadFlag = 1
print (“Dead Flag 2 Raised”)
time.sleep(0.1)

print(“Out of While Loop!”)

#Reset Flags
xDeadFlag = 0
yDeadFlag = 0

#Pause Between Steps
time.sleep(0.3)

Gcode2Steps()
print(“Positions”)
print(xyzPos)
print(“Steps”)
print(xyzSteps)
Steps2Motion()
'''
