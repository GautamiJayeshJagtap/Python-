import webbrowser
import time

print("current time is" +time.ctime())

breatno=3
count=0
while (count<breatno):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=AJtDXIazrMo")
    count=count+1
