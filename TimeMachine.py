# Super Party Time with Marty The Applet Part II Electric Bugaloo Time Machine
# Rue,Caroline, Camila, Lindsey
# Project for Intermediate Python
# October 5, 2021

#import necessary packages
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import *
from dateutil.parser import parse
import time
import json
import re
from bs4 import BeautifulSoup

# Main method
def main():
    timeMachine()

# Program  to run the interactive program with UI and support functions
def timeMachine():

   #BOOTUP
    print("\nBooting Up", end="")
    for i in range(10):
        print(".", end="")
        time.sleep(0.25)
    print("\n\n")
    
    #IMAGE
    img = mpimg.imread("PartyMarty.png")
    fig = plt.imshow(img)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()
    
    #WELCOME
    linestring = "\n______________________________________\n"
    welcomestring = "♥ ♥ ♥ ♥ ♥ ♥ WELCOME MARTY ♥ ♥ ♥ ♥ ♥ ♥\n\n☺ ☺ ☺ ☺ ☺ I'm your computer ☺ ☺ ☺ ☺ ☺\n"
    print(linestring, "\n")
    slowPrint(welcomestring, 0.05)
    print(linestring)
    time.sleep(1)
    slowPrint("Press ENTER to continue",0.05)
    input()
    print()

    #BIRTHDAY PROMPT
    birthdate = getBirthday()

    #BEGIN PROGRAM
    
    #Main menu with numerical input to initiate specific programs
    state = 0
    while True:
        valid = False
        input("~Press ENTER to go to Main Menu.~\n")
        time.sleep(1)
        while not valid:
            printMenu()
            newinput = input("What would you like to do? \n > ")
            try:
                state = int(newinput)
                if(state in range(1, 6)):
                    valid = True
                else:
                    print(
                        "INVALID INPUT! Please select an integer 1-5\n\nResetting...\n\n")
            except ValueError:
                print("INVALID INPUT! Please select an integer 1-5\n\nResetting...\n\n")
        
        # State 1: Get past event using getPast()
        if state == 1: 
            slowPrint("\n"+"I'm remembering the past",0.02)
            for i in range(4):
                print(".", end="")
                time.sleep(0.5)
            print("\n", end="")
           
            # Retrieve and format information from historical event 
            past = getPast(birthdate.strftime("%B"), birthdate.day)
            year = past[0].split(" ")[0]
            temp = past[0].split(" ")
            event = " ".join(temp[1:(len(temp))])
            paststring = "On your birthday back in "+year+",\n"+event+"."
            detailstring = past[1]
            sparklestring = "~◷~"*15

            # Display historical event
            print()
            slowPrint(sparklestring, 0.005)
            print("\n")
            print(paststring+"\n\n")
            slowPrint("Details",0.1)
            for i in range(6):
                print(".", end="")
                time.sleep(0.5)
            print()
            slowPrint(detailstring,0.04)
            time.sleep(2)
            print("\n")
            slowPrint(sparklestring,0.005)
            print()
            time.sleep(5)
        
        # State 2: Get current holiday using getPresent()
        elif state == 2:  
            slowPrint("\n"+"I'm thinking about the present",0.02)
            for i in range(4):
                print(".", end="")
                time.sleep(0.5)
            print()
            
            # Retrieve and format holiday found on birthday 
            presentstring = getPresent(birthdate.month, birthdate.day)
            sparklestring = "⫱"*int(len(presentstring)*1.5)
            
            # Dispaly holiday information
            slowPrint(sparklestring, 0.05)
            print("\n")
            slowPrint(presentstring, 0.04)
            print("\n")
            slowPrint(sparklestring, 0.05)
            print()
            time.sleep(3)
          
        # State 3: Get an astrological horoscope using getSign() and getHoroscope()
        elif state == 3:
            
            # Get sign from CSV
            sign = getSign(birthdate.month, birthdate.day)
            
            # Input sign into getHoroscope() to get horoscope from web
            horoscope = getHoroscope(sign)
            
            # Format and display horoscope and sign
            starstring = "✪❍"*15
            slowPrint("\n Reading your future",0.02)
            for i in range(4):
                print(".", end="")
                time.sleep(0.5) 
            print("\n")
            slowPrint(starstring,0.01)
            print()
            time.sleep(1)
            print("\nYour sign is ",end="")
            time.sleep(1)
            print(sign[1])
            print()
            time.sleep(1.5)
            print("Here is what I found",end="")
            for i in range(4):
                print(".", end="")
                time.sleep(0.5)
            print("\n")
            slowPrint(horoscope,0.04)
            time.sleep(1)
            print()
            print()
            slowPrint(starstring,0.01)
            print()
            time.sleep(3)
            
        #State 4: Call getBirthday() again to reset the birthdate variable
        elif state == 4:
            birthdate = getBirthday()
       
        #State 5: Exit the while loop
        elif state == 5:  # leave program
            byestring = "\n...\n...\n...\nGoodbye."
            slowPrint(byestring, 0.1)
            time.sleep(1)
            break
        valid = False



# A function to display the menu string
def printMenu():
   menu = """
*************** MENU ******************

   1. Explore the past.
   2. Know your present.
   3. Divine your future.
   4. Change your birthday.
   5. Leave program.
   
***************************************
   """
   slowPrint(menu, 0.01)


# A function to print out a string char by char with a certain speed
def slowPrint(string, timesep):
    for i in range(len(string)):
        print(string[i], end="")
        time.sleep(timesep)


# A function to get the user's birthday
def getBirthday():
    
    # Prompt user
    slowPrint("To continue, please tell me your birthday.",0.01)
    stringinput = input(" > ")
    
    # TryCatch any errors in birthday formatting
    try:
        # Use the parse function to interpret user input as a date
        birthdate = parse(stringinput)
    except:
        print()
        print("Invalid input for your birthday... resetting.")
        print()
        return getBirthday()
    print("\n \t\t mhm", end="")
    
    # Echo the birthday month and day to the user
    for i in range(6):
        print(".", end="")
        time.sleep(0.25)
    slowPrint("\n\n\tSo your birthday is ",0.01)
    time.sleep(1)
    print(birthdate.strftime("%B %d")+".",end="")
    time.sleep(2)
    print("\n\n")
    
    # Return birthdate
    return(birthdate)


# A function to read a GitHub CSV containing horoscope start and end dates
def getSign(month, day):
    ### Get the Horoscope/Astrology CSV from GitHub
    httpString = "https://raw.githubusercontent.com/tahsinozden/horoscope-calculator/master/horoscopes.csv"
    ### Read data to a dataframe
    data = pd.read_csv(httpString)
    ### Initialize new columns
    data["Start"] = ""
    data["End"] = ""

    ### Birthday Datetime
    birthday = datetime(2020, month=month, day=day)

    ### Check to see if they're a capricorn, because capricorns mess everything up
    if (month == 1 and day <= 19) or (month == 12 and day >= 22):
        horoscope = data[data["Horoscope"] == "Capricorn"]
    ### Compare birthday to each start and end date to create a list of bools
    else:
        for i in range(len(data)):
            string = data["TimeStart"][i].split("-")
            data["Start"][i] = birthday > datetime(
                2020, int(string[0]), int(string[1]))
            string = data["TimeEnd"][i].split("-")
            data["End"][i] = birthday < datetime(
                2020, int(string[0]), int(string[1]))
        horoscope = data[data["Start"] & data["End"]]

    ### Get horoscope
    signName = str(horoscope.iloc[0][0])
    Zodiac = {'ARIES': 1, 'TAURUS': 2, 'GEMINI': 3, 'CANCER': 4,
              'LEO': 5, 'VIRGO': 6, 'LIBRA': 7, 'SCORPIO': 8,
              'SAGITTARIUS': 9, 'CAPRICORN': 10, 'AQUARIUS': 11, 'PISCES': 12}
    signNum = Zodiac[signName.upper()]

    # Return Horoscope and its corresponding number
    sign = [signNum, signName]
    return sign


# A function to get any holidays this year that fall on the input date using an API
def getPresent(month, day):
    
    #TryCatch the webscraper
    try:
        page = requests.get("https://calendarific.com/api/v2/holidays?&api_key=ccf6a8e782f716124A6813beebc76fd5cde99547&country=us" +
                        "&year=2021" + "&month=" + str(month) + "&day=" + str(day), headers={'Content-Type': 'application/json'})
    except ConnectionRefusedError:
        return "This year, there are no holidays on your birthday."
    
    #Process the retrieved JSON file into a DataFrame
    data = json.loads(page.content.decode('utf-8'))
    dataDF = pd.json_normalize(data["response"]["holidays"])
    
    #Return the holiday only if there is a holiday on that day
    try:
        return "This year, your birthday falls on " + dataDF["name"][0]
    except:
        return "This year, there are no holidays on your birthday."


# A function to web scrape a historical event that occured on the input day
def getPast(month, day):

    #month parameter must be string and all lower case (example: october)
    month = month.lower()
    day = str(day)
    #piecing together the url
    httpString ='https://www.timeanddate.com/on-this-day/' + month + '/' + day
    page = requests.get(httpString)
    
    #checking the page status code
    if page.status_code != 200:
        print('Error Status Code', page.status_code)
    else:
        #parse the page
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #finding the tags and sub-tags
        t = soup.find(class_="main-content-div")
        a = t.find_all(class_="big_banner-article")
        a = a[0]
        
        #getting the title of the event (includes year in the title)
        b = a.find(class_="otd-ttl")
        title = b.text
    
        z = a.find(class_="eight columns")
        
        #getting paragraph text
        sub = z.find_all('p')
        paragraph = sub[0].text
        
        #returns tuple with title (string) in the first position and 
        #paragraph (string) in the second position
        return(title, paragraph)

# A function to web scrape a horoscope that corresponds with input date 
def getHoroscope(sign):
    sign = sign[0]
    #Webscraping of horoscope website 
    httpString = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='+ str(sign)
    #testing
    #httpString = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9'       
    #print(httpString)
    page = requests.get(httpString)
    if page.status_code != 200:
        print('Error', page.status_code)    #raise status error if status != 200
    else:
        #Scraping: parse the page
        soup = BeautifulSoup(page.content, 'html.parser')
        x = soup.find(class_="main-horoscope")
        y = x.find('p').get_text()
        #Return text
        y.strip('<.*?>')        #remove HTML tags
        y = y.split(" - ")[1]
        return(y)     



# Call the main function to begin the program
main()
