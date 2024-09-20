import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import random
import json
import pickle
from time import sleep
from tensorflow import keras
from tensorflow.keras import layers

# Initialize the stemmer
stemmer = LancasterStemmer()

# Load intents data
with open("intents.json") as file:
    data = json.load(file)

# Load or create training data
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(set(words))

    labels = sorted(labels)

    training = []
    output = []
    out_empty = [0] * len(labels)

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            bag.append(1 if w in wrds else 0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# Build the model
model = keras.Sequential([
    layers.Input(shape=(len(training[0]),)),
    layers.Dense(8, activation='relu'),
    layers.Dense(8, activation='relu'),
    layers.Dense(len(output[0]), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Load or train the model
try:
    model.load_weights("model.h5")
except:
    model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
    model.save_weights("model.h5")

def bag_of_words(s, words):
    bag = [0] * len(words)
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def chat():
    print("Hi, how can I help you?")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        # Suppress the output of model prediction
        results = model.predict(np.array([bag_of_words(inp, words)]), verbose=0)[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            sleep(3)
            Bot = random.choice(responses)
            print(Bot)
        else:
            print("I don't understand!")

chat()