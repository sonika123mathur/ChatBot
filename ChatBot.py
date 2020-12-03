from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer



#instance of the class “ChatBot.”
my_bot = ChatBot(name='PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation' , 'chatterbot.logic.BestMatch'])
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

#specifying the lists of strings that can be later used to train your Python chatbot
small_talk = ['Hi There!',
              'Hi!', 
              'How are you?' , 
              'I am fine' , 
              'What is your name?'
              ]
math_talk_1 = ['pythagorean theorem' , 'A squared plus b squared equals c squared.']
math_talk_2 = ['Law of cosines' , 'c**2 = a**2 + b**2 -2 * a * b * cos(gamma)']

#train the bot by writing an instance of “ListTrainer” and supplying it with a list of strings
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)


print(my_bot.get_response("Hi"))
print(my_bot.get_response("How are you?"))