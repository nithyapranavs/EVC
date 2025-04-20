#%%
import nltk
import tflearn
import tensorflow
import json
import numpy
import pickle
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
with open('intents.json') as file:
    data = json.load(file)
words = list()#['i','want'...,
label = list()
docs_x = list()
docs_y = list()
for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)#['i','want'...]
        #print(pattern,':',wrds)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent['tag'])
    if intent['tag'] not in label:
        label.append(intent['tag'])
words = [stemmer.stem(w.lower()) for w in words if w != '?']
words = sorted(list(set(words)))#{1,2,3}
label = sorted(label)#len=10

training = list()
output = list()
out_empty = [0 for _ in range(len(label))]#0,0,0,0...0
for x,doc in enumerate(docs_x):
    bag = list()
    wrds = [stemmer.stem(w.lower()) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row = list(out_empty)
    output_row[label.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)
training = numpy.array(training)
output = numpy.array(output)
with open('data.pickle','wb') as f:
    pickle.dump((words,label,training,output),f)
tensorflow.reset_default_graph()
net = tflearn.input_data(shape = [None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]),activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)
model.fit(training,output,n_epoch=1000, batch_size=8 , show_metric=True)
model.save('model.tflearn')
print('trained sucessfully')

# %%
