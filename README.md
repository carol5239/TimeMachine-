# TimeMachine-

Abstract:

This applet offers users a fun birthday, time-traveling surprise with information relevant
to their birthdate about astrology, historical events, and current holidays.

The user inputs their birthdate and selects whether they would like to “travel” to the
past, present, or future. Using the user’s birthdate, the application transforms the user’s
input into canonical text, which is then used to scrape websites and csv files for
corresponding data. The user’s birthdate is used to pull astrological data (representing
the future), historical event data (representing the past), and recurring holidays
(representing the present). Utilizing matplotlib and time libraries, the application
presents this information in an engaging format so the user feels like they are
time-traveling under the guidance of an omnipresent computer.

Consolidating date-relevant information, the applet parses data from disparate sources
utilizing API queries and data scraping techniques like BeautifulSoup and requests. The
application also utilizes a series of if/then statements, while and try/except loops, and
developer-defined functions to create a seamless experience for applet users.

User Guide:

1. User sets up a directory to the file containing the program files.
2. User imports the following packages:
- pandas
- requests
- BeautifulSoup
- re
- json
- dateutil
- datetime
- time
- matplotlib
3. Once the directory has been set up and the packages have been installed
properly, the user runs the program.
4. In the getBirthday() function, the user is prompted to input their birthdate (str) in
any format (e.g. 07-10-1954, July 10, 1954, 07/10/1954). The datetime.parser
package transforms the str into canonical text so that it is compatible with the
websites’ date format.
5. The user is prompted with a menu of options to select whether they would like to
“explore”... the 1) past, 2) present, 3) future, 4) change birthday, or 5) quit.
Utilizing a while loop containing a try-catch, the user is re-prompted if they enter
a number that is not an integer or doesn’t fall within the range (1-5). This running
loop at the menu expects the number to be input as a char in set
{“1”,”2”,”3”,”4”,”5”}.
6. If the user selects option #4, getBirthday() is called, they are re-prompted to input
their birthdate (step #4) and the process repeats.
7. If the user selects option #5, the program quits.
8. If the user selects options #1, the program executes the getPast(month, day)
function. month is input as the full string name, and day is a char or int. The
function parses timeanddate.com with BeautifulSoup and requests and returns a
tuple with the title of the historical event (str) and the paragraph summarizing the
historical event (str) that matches those parameters.
9. If the user selects options #2, the program executes the getPresent(month,day)
function. Using the month and day parameters as integers, the function
searches calendarific.com, with requests, and returns a holiday name (str) in json
format that matches those parameters. If a holiday does not exist on the user’s
birthdate, a message is returned. Note: the program searches exclusively on
American holidays and the year 2021.
10.If the user selects option #3, the program executes the functions
getSign(month,day) and getHoroscope(sign). month and day are input as
integers. getSign(month,day) uses a Github CSV file to compute the astrological
sign. It returns a list which contains the astrological sign as both an integer and
string. getHoroscope(sign) uses this sign list to parse horoscope.com with
BeautifulSoup and requests. It then returns today’s horoscope as a string.
11. The results returned from options #1-3, are presented following sparkles and text
framing their past, present, or future (e.g. “On your birthday, x, the following
transpired: ”). This is meant to enhance user engagement.
12. Utilizing a while loop, the user continues to be prompted to enter their birthdate
and select a menu option (and the above steps repeat) until they select option #5
to quit, and the program stops running.
