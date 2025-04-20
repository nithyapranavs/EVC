#%%
import tkinter
import random
import json
import pickle
from pyttsx3 import speak
import main
#modules downloaded
import numpy
#M L modules
import nltk
import tflearn
import tensorflow
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
with open('intents.json') as file:
    data = json.load(file)
try:
    with open('data.pickle','rb') as f:
        words,label,training,output=pickle.load(f)
except:
    print('need to train model')
tensorflow.reset_default_graph()
net = tflearn.input_data(shape = [None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]),activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)
try:
    model.load('model.tflearn')
except:
    print('model does not exist')

def bagwrds(s,words):
    bag = [0 for _ in range(len(words))]
    s_wrds = nltk.word_tokenize(s)
    s_wrds = [stemmer.stem(word.lower()) for word in s_wrds]
    for se in s_wrds:
        for i,w in enumerate(words):
            if w==se:
                bag[i] = 1
    return numpy.array(bag)

def chat():
    print('chat with me')
    resp = list()
    tag = None
    inp = main.need.get_voice()
    if inp == 'could not get you':
        print('could not get you')
        #continue
    if inp.lower()=='exit':
        pass
        #break
    elif inp == "be my translator" or inp == 'be my interpetor':
        main.net.translater()
    elif inp == "calender":
        main.py.Calendar()
    elif inp == "emergency":
        main.net.emergency()
    elif inp == 'system info':
        main.pc.systeminfo()
    else:
        arr = bagwrds(inp,words)
        sp = arr.shape[0]
        arr = arr.reshape(1,sp)
        results = model.predict(arr)
        l = results.tolist()[0]
        temp = 0
        for i in l:
            print(i)
            temp += i
        print(temp)
        result_index = numpy.argmax(results)
        if not results[0][result_index] > 0.5:
            speak("couldn't get you try another way")
            #continue
        tag = label[result_index]
        print(inp)
        print("tag",tag)

        if tag=="netspeed":
            main.net.speed()
        elif tag=="mail":
            toaddress=input(" enter toadress :" )
            content=input("enter the  content :")
            main.net.sentmail(content,toaddress)
        elif tag=="open":
            #site=input("enter the scarch")
            main.pc.medias(inp.split()[-1])
        elif tag=="wiki":
            main.net.wikisearch(inp)
        elif tag=="weath":
            main.net.weather()
        elif tag=="location":
            main.net.mylocation()
        elif tag=="charge":
            main.pc.charge()
        elif tag=="time":
            main.py.time()
        for tg in data['intents']:
            if tg['tag'] == tag:
                resp = tg['responses']
        if not resp == list():
            speak(random.choice(resp))
def chat_call():
    if main.net.is_connected():
        chat()
    else:
        t = 'you are not connected to internet'
        print(t)
        speak(t)
root = tkinter.Tk()
root.iconbitmap('pig.ico')
tkinter.Button(root,text="mic symbol here",command=chat_call).pack()
root.mainloop()
# %%
