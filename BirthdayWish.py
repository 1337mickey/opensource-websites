import webbrowser
import datetime
import pyautogui as pg
import time

#Determine when to text
timeRun = input("Enter the time in 24 hour format (Hour:Minute) -> ")
#facebook-messenger chat link
url = input("Enter URL -> ")
#choose 1 to sent line by line else 2 to send as a whole
ask = int(input("Enter 1 if you want to send the messages in file \nEnter 2 if you want to loop the single message \nEnter a value : "))
#how many times same text is to be sent
loop = int(input("Loop -> "))

#code-----------------
work = "notDone"
while work == "notDone": #set for looping till the desired time is pulled from system time
    dateTime = datetime.datetime.now().strftime("%H:%M") #Hour:Minute(00:00) format
    THour = dateTime.split(":")[0]
    TMinute = dateTime.split(":")[1]

    if int(THour) > 12:
        THour = int(THour) - (12)
        if THour < 10:
            THour = str(0) + str(THour)
        dateTime = str(THour)+":"+str(TMinute)

    if str(dateTime) == timeRun: #test for set time
        webbrowser.open(url)
        time.sleep(7)
        for i in range(loop):
            f = open("text.txt", "r")

            if ask == 1:
                for word in f:
                    pg.typewrite(word)
                    time.sleep(1) #sleep time after each line of text
                    pg.press("enter") #press enter to send msg
            else:
                repeat = ""
                word = f.read()
                repeat = repeat + word
                pg.typewrite(repeat)
                time.sleep(1)
                pg.press("enter")
        work = "done" #stops code when msg is sent
