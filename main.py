import webbrowser
import speedtest
import smtplib
import wikipedia
import os
import calendar
import datetime
import requests
import socket
import speech_recognition as sr
import psutil as p
import platform
#importing functions in modules
from bs4 import BeautifulSoup
from pyttsx3 import speak
class need: 
    '''class that contains the methods
    that have been used for this program'''
    def numtotxt(num):
        '''converts number to text only for time'''
        num=str(num)
        unit = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                 '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

        tens = {'2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty',
                '6':'sixty','7':'seventy','8':'eighty','9':'ninty'}

        teen = {'11': 'eleven', '12': 'twelve', '13': 'thirteen',
                '15': 'fifteen', '18': 'eighteen'}

        if num=='10':
            return 'ten'
        if num=='100':
            return 'hundred'
        if len(num)==1:
            return unit[num]
        num1=num[1]
        num2=num[0]
        if num2!='1':
            fst_wrd=tens[num2]
            snd_wrd=unit[num1]
            return fst_wrd+snd_wrd
        if num not in teen.keys():
            return unit[num]+'teen'
        return teen[num]
    def get_voice():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('say something')
            audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return 'could not get you'

class net:
    '''class containing the methods which required net'''

    def is_connected():
        '''return true if connected to internet'''
        try:
            st = speedtest.Speedtest()
            return True
        except:
            return False
    def speed():
        '''method that calculate the speed of the internet'''
        st=speedtest.Speedtest()
        print(f"download speed is: {st.download()*1e-6}")
        print(f"upload speed is   : {st.upload()*1e-6}")
        servernames=[]
        st.get_servers(servernames)
        print(f"ping is          : {st.results.ping}")

    def sentmail():
        '''to sent mail'''
        toadress = input('to adress ')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("easyvoicecommand@gmail.com", 'password')
        message = need.get_voice()
        s.sendmail("easyvoicecommand@gmail.com", toadress, message)
        s.quit()

    def webpage(site):
        '''open the site given'''
        with open(r'1 links.txt') as f:
            l = f.readlines()
            for i in l:
                l2 = i.split(',')
                if l2[0] == site:
                    site = l2[1]
                    return
        webbrowser.open_new_tab(site)

    def wikisearch(cmd):
        '''search the cmd in wikipedia and  reads it'''
        sents = wikipedia.summary(cmd,sentences=2)
        print(sents)
        speak(sents)



    def weather():
        res=requests.get('https://ipinfo.io')
        city=res.json()['city']
        search=f'weather in {city}'
        url=f'https://www.google.com/search?&q={search}'
        r=requests.get(url)
        s=BeautifulSoup(r.text,'html.parser')
        update=s.find('div',class_='BNeawe').text
        print(update)

    def emergency():
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        hostname=socket.gethostname()
        ipaddr=socket.gethostbyname(hostname)
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
            'apikey':apiKey,
            'secret':secretKey,
            'usetype':useType,
            'phone': phoneNo,
            'message':textMessage,
            'senderid':senderId
            }
            return requests.post(reqUrl, req_params)

            # get response
        response = sendPostRequest(URL, '5JWO6YEWE4KHEPAXWTZZZGTD1YMDWDE8', 'KR1G106LQ86IRD3S', 'stage', '8825801149', 'mail@gmail.com', "emergency!! my ip address is "+str(ipaddr) )
        print(response)


    def mylocation():
        res=requests.get("https://ipinfo.io")
        print(res.json())

class pc:
    '''class that contains methords handling with files and databases'''
    def medias(name):
        with open('1 paths.txt') as f:
            l = f.readlines()
            for i in l:
                l2 = i.split(',')
                if l2[0] == name:
                    path = l2[1]
                    os.startfile(path)
                    return
            net.webpage(name)

    def systeminfo():
        print("plaform      ::",platform.platform())
        print("systen       ::",platform.system())
        print("processer    ::",platform.processor())
        print("architecture ::",platform.architecture())

    def charge():
        battery=p.sensors_battery()
        plugged=battery.power_plugged
        percent=str(battery.percent)
        if plugged==False:
            plugged = "not plugged in"
        else:
            plugged="plugged in"
            num=int(percent)
            #a=need.numtotxt(num)
        #print(a+percent"+"charging",plugged)
        #print(a,"percent")
        print(percent)

class py:
    '''class contains the methord that doesn't
    required any external files  or internet'''
    def Calendar(year=str(datetime.date.today())[:4],
                   month=str(datetime.date.today())[5:7]):
        '''displays calander of ge=iven month and year
        else present month's calander'''
        print(calendar.month(int(year),int(month)))

    def time():
        now = datetime.datetime.now()
        hrs = now.hour
        mint = now.minute
        if hrs == 0:
            hrs = 12
        elif hrs > 12:
            hrs -= 12
        if mint == 0:
            mint = None
        speak('the time is'+str(hrs)+','+str(mint))
    
