'''
Function to Convert GCode file into Stepper Motor Steps
'''

def gcode2Steps():

    #Variable Definitions
    endFlag = 0
    line = []
    
    xPos = 0
    yPos = 0
    zPos = 0
    
    xStepsPast = 0
    xStepsCurrent = 0
    yStepsPast = 0
    yStepsCurrent = 0
    zStepsPast = 0
    zStepsCurrent = 0
    stepCounter = 0
    
    stepsPerMm = 38
    
    # Read Lines in Tweet GCode and Write to Positions File
    f1 = open('tweet.gcode', 'r')
    line = str(f1.readline())
    f2 = open('positions.txt', 'w')
    
    #Iterate Through File
    while (endFlag == 0):

        # Stop Reading at End of File
        if line == '':
            endFlag = 1;

        # Read Only Move Lines
        if 'G0' in line:

            # Extract X
            if 'X' in line:
                xPos = float(line[(line.index('X')+1):(line.index('X')+7)])
            f2.write('%s\n' % (xPos))

            # Extract Y
            if 'Y' in line:
                yPos = float(line[(line.index('Y')+1):(line.index('Y')+7)])
            f2.write('%s\n' % (yPos))

            # Extract Z
            if 'Z' in line:
                
                # Raise or Lower Pen
                if 'Penetrate' in line:
                    zPos = 1 
                elif 'Z5.0000' in line:
                    zPos = 0
                    
            f2.write('%s\n' % (zPos))
            
        # Get New Line
        line = str(f1.readline())
    
    f1.close()
    f2.close()
    endFlag = 0

    # Read Lines in Positions File and Write to Steps File
    f2 = open('positions.txt', 'r')
    f3 = open('steps.txt', 'w')
    
    #Discard 1st Lines
    line = str(f2.readline())
    line = str(f2.readline())
    line = str(f2.readline())
    
    #Read 1st Positions
    line = str(f2.readline())
    xStepsPast = line
    
    line = str(f2.readline())
    yStepsPast = line

    line = str(f2.readline())
    zStepsPast = line
    
    line = str(f2.readline())
    xStepsCurrent = line
    
    line = str(f2.readline())
    yStepsCurrent = line

    line = str(f2.readline())
    zStepsCurrent = line
    
    #Iterate Through File
    while (endFlag == 0):
        
        # Take Difference Between Postions, Calculate Steps
        xSteps = int((float(xStepsCurrent)-float(xStepsPast)) * int(stepsPerMm))
        ySteps = int((float(yStepsCurrent)-float(yStepsPast)) * int(stepsPerMm))
        if zStepsCurrent < zStepsPast:
            zSteps = 0
        elif zStepsCurrent > zStepsPast:
            zSteps = 1

        #Write to Steps File
        f3.write('%s\n' % (xSteps))
        f3.write('%s\n' % (ySteps))
        f3.write('%s\n' % (zSteps))

        #Increment Variables
        xStepsPast = xStepsCurrent
        yStepsPast = yStepsCurrent
        zStepsPast = zStepsCurrent
        
        # Get New Lines
        line = str(f2.readline())
        xStepsCurrent = line

        line = str(f2.readline())
        yStepsCurrent = line

        line = str(f2.readline())
        zStepsCurrent = line

        stepCounter+=1

        # Stop Reading at End of File
        if line == '':
            endFlag = 1;
    
    f2.close()
    f3.close()
    
    return stepCounter