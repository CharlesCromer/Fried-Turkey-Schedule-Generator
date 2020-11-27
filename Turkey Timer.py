##Fried Turkey Schedule Generator
##
##(C) 2020 Charles Cromer, Panama City, Florida, USA
##Released under the GNU Public License (GPL)
##email charles.cromer@gmail.com

from datetime import datetime, time, timedelta


def main():
    welcome()
    runAgain = 'Y'

    #Various process time additions will accumulate here
    accumulatedTime = 0
    
    #Starts a loop allowing the user to modify their dinner parameters multiple times
    while runAgain.upper() == 'Y':

        #Creates a file object in which the generated schedule will be written to
        file = open("Turkey Timer.txt", 'w')
        serveTime = getMealTime()
        turkeyWeight = int(getTurkeyInfo())
        maxTurkeyFryTime = getMaxTurkeyFryTime(turkeyWeight)
        minTurkeyFryTime = getMinTurkeyFryTime(turkeyWeight)
        initialTime = removeFromFridge(serveTime, maxTurkeyFryTime)

        file.write("Fried Turkey Schedule Generator\n")
        file.write("Created by: Charles Cromer\n")
        file.write("Last modified: 11/24/2020\n")
        file.write("Please email charles.cromer@gmail.com with any feedback\n")

        
        print('\n\nRemove the Turkey from Refrigerator: ', displayAmPmTime(initialTime))
        file.write('\n\nRemove the Turkey from Refrigerator: '+ displayAmPmTime(initialTime))

        print('For 30 minutes, allow the turkey to come to room temperature and for preparation and seasoning.\n')
        file.write('\nFor 30 minutes, allow the turkey to come to room temperature and for preparation and seasoning.\n')
        accumulatedTime = accumulatedTime +30
        
        print('\nPrepare the Fryer and Oil: ', displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))
        file.write('\nPrepare the Fryer and Oil: '+ displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))

        print('For approx. 15 minutes prepare the fryer, and oil etc\n')
        file.write('\nFor approx. 15 minutes prepare the fryer, and oil etc\n')
        accumulatedTime = accumulatedTime + 15
        
        print('\nStart Heating Oil: ', displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))
        file.write('\nStart Heating Oil: ' + displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))

        print('Allow the oil to get to 350, approximately 60 minutes')
        file.write('\nAllow the oil to get to 350, approximately 60 minutes')
        accumulatedTime = accumulatedTime + 60
        
        print('\nPut Turkey in Oil: ', displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))
        file.write('\n\nPut Turkey in Oil: ' + displayAmPmTime(initialTime + timedelta(minutes = accumulatedTime)))

        print('Allow the bird to fry for the next: ' + str(minTurkeyFryTime) + ' minutes') 
        file.write('\nAllow the bird to fry for the next: ' + str(minTurkeyFryTime) + ' minutes') 
        
        print('\nTemperature Probe Turkey: ', displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + minTurkeyFryTime))))
        file.write('\n\nTemperature Probe Turkey: '+ displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + minTurkeyFryTime))))
        
        print('If the probe reads 160 F in the thickest part of the breast, remove the turkey from the oil and allow to rest for 30 minutes before carving ('+ (displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + 30 + minTurkeyFryTime))))+')')
        file.write('\nIf the probe reads 160 F in the thickest part of the breast, remove the turkey from the oil and allow to rest for 30 minutes before carving ('+ (displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + 30 + minTurkeyFryTime))))+')')

        print('Congrats! You are ahead of schedule! Simply keep bird hot by covering with foil.')
        file.write('\nCongrats! You are ahead of schedule! Simply keep bird hot by covering with foil.')

        print('IF NOT, resubmerge turkey in oil and continue to cook until: ' + displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))
        file.write('\nIF NOT, resubmerge turkey in oil and continue to cook until: ' + displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))

        print('\n\nIMPORTANT NOTE:')
        file.write('\n\nIMPORTANT NOTE:')

        print('Only the last two inches of the thermometer at the tip affect the reading')
        file.write('\nOnly the last two inches of the thermometer at the tip affect the reading')

        print('So push in only until you find the coldest part of the meat. When that reaches 160 degrees, you\'re done.')
        file.write('\nSo push in only until you find the coldest part of the meat. When that reaches 160 degrees, you\'re done.')

        print('USDA Guidelines state poultry is safe to eat at an internal temperature of 170 F')
        file.write('\nUSDA Guidelines state poultry is safe to eat at an internal temperature of 170 F')

        print('As your turkey rests it will continue to cook, and the internal temperature will rise by 10 F\n')
        file.write('\nAs your turkey rests it will continue to cook, and the internal temperature will rise by 10 F\n')

        print('\nRemove Turkey from Oil: ', displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))
        file.write('\nRemove Turkey from Oil: ' + displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))

        print('Allow the turkey to rest while lightly tented with foil for the next 20 minutes')
        file.write('\nAllow the turkey to rest while lightly tented with foil for the next 20 minutes')
        accumulatedTime = accumulatedTime + 20

        print('\nBegin Carving Turkey: ', displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))
        file.write('\n\nBegin Carving Turkey: '+ displayAmPmTime(initialTime + timedelta(minutes = (accumulatedTime + maxTurkeyFryTime))))


        print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A printable copy of this schedule is available in the same folder as this program under the title: Turkey Timer.txt')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        file.close()
        runAgain = input('Run Again? [y/n]: ')
        


#Gets user input for the time that the meal will begin
def getMealTime():
    print('\nPlease enter the time you need to serve the turkey')
    serveTime = input('Please use the following format HH:MMam. (Example: 3:00pm): ')
    #serveTime=serveTime.lower()
    while serveTime.find(':') == -1 or (serveTime.lower().find('pm', -2,) == -1 and serveTime.lower().find('am', -2,) == -1):
        print('\nERROR: Please enter the time you need to serve the turkey')
        serveTime = input('Please use the following format HH:MMam. (Example: 3:00pm): ')
    serveTime = convertTo24Time(serveTime)
    return serveTime


#Gets user input for the weight of the turkey
def getTurkeyInfo():
    turkeyWeight = input('Please enter the weight of your turkey in pounds: ')

    #Validates that the turkey weight is a number, is greater than 5 pounds and less than 30 pounds
    while not turkeyWeight.isdigit() or int(turkeyWeight) < 5 or int(turkeyWeight) > 30:
        print('\nERROR: It appears you entered an invalid weight')
        if int(turkeyWeight) < 5:
            print('Are you sure this isn\'t a chicken?')
        else:
            print('Are you sure this isn\'t an Ostrich?')        
        turkeyWeight = input('Please enter the weight of your turkey in pounds: ')
    return turkeyWeight


#Determines the maximum time that the turkey should be fried
def getMaxTurkeyFryTime(weight):
    maxTime = int(3.5 * weight)
    return maxTime


#Determines the minimum time that the turkey should be fried
def getMinTurkeyFryTime(weight):
    minTime = int(3 * weight)
    return minTime


#Determines the time in which the turkey needs to be removed from the refrigerator
#Accepts two arguments:
#servetime, which is the user input of what time the meal will start
#and maxTime, which is the maximum time the turkey will need to be fried
#this function then subtracts the sum of the variable cook time and max accumulated time
#to get the initial start time
def removeFromFridge(serveTime, maxTime):
    initialTime = serveTime - timedelta(minutes = (maxTime + 140))
    #print('Remove the Turkey from Refrigerator: ', displayAmPmTime(initialTime))
    return initialTime


#Converts the user input for meal start time to a time object for manipulation    
def convertTo24Time(givenTime):

    #Saves the value of am or pm that the user enters for later calculation decisions    
    amPm = givenTime[-2:]

    #Saves the user input as a time object in HH:MM while disregarding the user input of am or pm
    timeObject = datetime.strptime(givenTime[:-2], '%I:%M')

    #Converts the 12 hour clock formatted input into 24 hour clock format for time calculations
    time1 = timedelta(hours = timeObject.hour, minutes = timeObject.minute)
    if amPm.lower() == 'pm':
        time2 = timedelta(hours = 12)
        time1 = time1 + time2
    return time1


#Generates a display of the time object in a user friendly format
def displayAmPmTime(time):

    #Since time will be coming in as a timedelta object, it converts it to a string
    time = str(time)
    
    #Once time is a string it can then be converted into a time object
    time = datetime.strptime(time, '%H:%M:%S')

    #Established when noon is, and converts noon to a timeobject for comparison
    afterNoon = '12:00:00'
    afterNoonTimeObject = datetime.strptime(afterNoon, '%H:%M:%S')

    #Established when 1pm is, and converts 1pm to a timeobject for comparison
    onePM = '13:00:00'
    onePMTimeObject = datetime.strptime(onePM, '%H:%M:%S')

    #Decision structure that will converts the 24 hour timeobject back
    #to a user friendly visual of HH:MM(am/pm)
    if time < afterNoonTimeObject:
        time = str(time)[:-3] + 'am'
    elif time < onePMTimeObject:
        time = str(time)[:-3] + 'pm'
    else:
        time = time - timedelta(hours = 12)
        time = str(time)[:-3] + 'pm'
    return time[11:]

def welcome():
    print("Fried Turkey Schedule Generator")
    print("Created by: Charles Cromer")
    print("Last modified: 11/27/2020")
    print("Please email charles.cromer@gmail.com with any feedback")
    print("\n\n               H A P P Y     T H A N K S G I V I N G")
    print("")
    print("                 T O   Y O U   A N D   Y O U R S !")
    print("")
    print("                                       ____")
    print("                                      :    :")
    print("                  ___                 :____:")
    print("          ___ ---\ ~~ /---___         :  []:")
    print("          \   \ ~ \~ /~~~/~~~/     ----,-------")
    print("        ,' \~~ \~~ \/ ~~/~~~/ `,     ,'  0 0 __")
    print("       -_~~ \   \,------,  / ~ _`    ;    _____\ ")
    print("      ;   - _ \,'^^^^^^^ ""`,_-  \   `, `--'; u")
    print("      ; ~~   ,'^^^^-----------   /   ,'`,,,'")
    print("      ;~ ---, ^^^,`__----,  ..`,/  ,'..,'")
    print("      `,  ~ ,^^ <_'__--__ `, .. `,/ .. `")
    print("       `,---` ^<________--  `, .. ..  ,'     ___ [] ___")
    print("        `,---` <__ -__ ___  ,' .. . ,`     _/   \)(/   \_")
    print("         `, --` <__ __ _  ,' ... _,`      /   /      \   \ ")
    print("          `--,___<___   ,'`-___,'       ,'   :   |        `, ")
    print("                  <___,'(||)            :             :    : ")
    print("                    ||   ||             :    :   |         ; ")
    print("                  __||_ _||_            \_            :   _/ ")
    print("                  // ;;\\ ;;\\             \_  \  |   /   _/ ")
    print("                ~~     ~~   ~~              \__________/ ")
    print("")
    print("")
    print("            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ")

def thankYou():
    print('Thank you for using the')
    print("Fried Turkey Schedule Generator\n")
    print("Created by: Charles Cromer\n")
    print("Last modified: 11/27/2020\n")
    print("Please email charles.cromer@gmail.com with any feedback\n")
  
main()
