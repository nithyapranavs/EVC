import os
main = ['bs4','SpeechRecognition','speedtest-cli',
     'wikipedia','pyttsx3','psupil',]
for i in main:
    s = 'pip install '+i
    os.system(s)
ml = ['numpy','nltk',
       'tensorflow','tensorflow==1.5','tflearn']
for i in ml:
    s = 'pip install '+i
    os.system(s)
