from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import wikipedia

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ListTrainer(english_bot)
#trainer = ChatterBotCorpusTrainer(english_bot)

'''conversation = [
    "Hello",
    "Hello!!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.c
]

trainer.train(conversation)


trainer.train(['Hello', ' Ask me something' ])
trainer.train(['Tell me about agriculture in India', "India's agriculture is composed of many crops, with the foremost food staples being rice and wheat. Indian farmers also grow pulses, potatoes, sugarcane, oilseeds, and such non-food items as cotton, tea, coffee, rubber, and jute. India is a fisheries giant as well." ])
trainer.train(['which crops are grown in india', "'Major crops grown in India are rice, wheat, millets, pulses, tea, coffee, sugarcane, oil seeds, cotton and jute, etc. of canal irrigation and tubewells have made it possible to grow rice in areas of less rainfall such as Punjab, Haryana and western Uttar Pradesh and parts of Rajasthan." ])
trainer.train(['What are the negative effects of climate change on agriculture?', 'Climate change can disrupt food availability, reduce access to food, and affect food quality. For example, projected increases in temperatures, changes in precipitation patterns, changes in extreme weather events, and reductions in water availability may all result in reduced agricultural productivity' ])
trainer.train(['What are governments scheme', 'PM-Kisan Scheme, Pradhan Mantri Kisan Maandhan yojana, Pradhan Mantri Fasal Bima Yojana (PMFBY), Soil Health Card Scheme, Paramparagat Krishi Vikas Yojana (PKVY), Pradhan Mantri Krishi Sinchai Yojana (PMKSY), National Agriculture Market (e-NAM) ' ])

#trainer.train(['What is your name?', 'My name is Pikachu'])
trainer.train(['How are you?', 'I am good' ])
trainer.train(['Bye?', 'Bye, see you later' ])'''

trainer.train(['Hi', ' Ask me something' ])
trainer.train(['Bye', ' Bye,Thank you for ' ])

#trainer.train("chatterbot.corpus.english")
#trainer.train("data/data.yml")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get("msg")
	userText1 = wikipedia.summary(userText, sentences = 2)
	print(userText)
	print(userText1)
	print(english_bot.get_response(userText1))
	return str(userText1)
    #return str(english_bot.get_response(userText1))
    #return str(english_bot.get_response(userText))

	#if (userText == 'Hi' or 'hi' or 'Bye' or 'bye'):
		#return str(english_bot.get_response(userText))
	#else:
		#userText1 = wikipedia.summary(userText, sentences = 2)
		#print(userText1)
		#return str(userText1)
 

if __name__ == "__main__":
#app.run(debug = False)
    from waitress import serve
    serve(app, host="192.168.43.131", port=8080)
