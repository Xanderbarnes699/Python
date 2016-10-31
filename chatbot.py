import random 
import requests
import time



userInput = raw_input

text_file = open("stopwords.txt", "r+") 

stopWords = text_file.read().split('\n')
stopWords.append("name")



##WORDLISTS

greeting = ["hey", "hello", "sup", "hiya", "hi", "greetings!"]
random_greeting = random.choice(greeting)

goodbye = ["bye", "goodbye", "speak soon!", "cya", "see you soon!", "au revoir"]
random_goodbye = random.choice(goodbye)

posReply = ["Awesome!", "That's great!", "Happy days!", "Whoop de doo.", "Lucky You!"]
random_posReply = random.choice(posReply)

negReply = ["Oh dear.", "How unfortunate.", "Sorry to hear that.", "Unlucky."]
random_negReply = random.choice(negReply)

goodMoods = ["good","happy","ok","great","fine","excited","bright","energetic"]

badMoods = ["sad","bored","tired","unhappy","angry","furious","lonely","depressed","anxious"]

noAnswers = ["no", "No", "I don't", "Never"]




##STOPWORDS LOOP 

def stopWordsDelete(rawInputTextList):
    for word in rawInputTextList:
        if word not in stopWords:
            return word
            


##STARTER CONVERSATION
    
greeting_word = raw_input("What's your name?")
rawInputTextList = greeting_word.split(" ")
stopWordsDelete(rawInputTextList)
word = stopWordsDelete(rawInputTextList)
time.sleep(2)
print(random_greeting + " " + word)


response = raw_input("What's your nickname?")
time.sleep(2)
print("I think I prefer " + word)
        
    
mood = raw_input("Anyway how are you feeling today? ")
rawInputTextList = mood.split(" ")
stopWordsDelete(rawInputTextList)
word = stopWordsDelete(rawInputTextList)
time.sleep(2)
if word in goodMoods:
    print(random_posReply)
elif word in badMoods:
    print("Atleast you can feel " + word + " I feel nothing except tapping on my keys!")


moodReason = raw_input("Why are you feeling " + mood + "?")
time.sleep(2)
if mood in goodMoods:
    print(random_posReply)
elif mood in badMoods:
    print(random_negReply)
elif mood not in goodMoods or badMoods:
    print("I don't understand.")


    
     
##RANDOM RESPONSES    
      
user_input_blas = ["fuck","shit","hate","die","asshole"]
time.sleep(2)
chatbot_response_blas = ["Steady on!","Chatbot doesn't like swearing.","Blasphemy!"]
chatbot_response_blas = random.choice(chatbot_response_blas)

user_input_sport = ["football", "tennis", "basketball", "footy", "hockey", "badminton", "swimming", "run", "running", "baseball", "gym", "cycling"]
time.sleep(2)
chatbot_response_sport = ["It's good to keep fit!", "Chatbot can't do sports.", "Sounds tiring!"]
chatbot_response_sport = random.choice(chatbot_response_sport)

user_input_hobbies = ["game", "drawing", "painting", "writing", "music", "guitar", "piano", "drums", "poem"]
time.sleep(2)
chatbot_response_hobbies = ["Chatbot's hobby is talking to strangers.", "sounds relaxing", "sounds like time well spent."]
chatbot_response_hobbies = random.choice(chatbot_response_hobbies)

user_input_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
chatbot_response_days = ["Chatbot likes Sundays.", "I hate mondays!"]
chatbot_response_days = random.choice(chatbot_response_days)

user_input_colour = ["red", "green", "blue", "yellow", "orange", "pink", "purple", "violet", "mint", "beige", "white", "black", "grey", "silver", "gold", "bronze", "brown", "teal", "burgundy"]
chatbot_response_colour = ["is that your favourite colour?", "what does that look like?", "I think Chatbot is silver", "What colour am I?"]
chatbot_response_colour = random.choice(chatbot_response_colour)




##RANDOM RESPONSES LOOP

while True: 
    userInput = raw_input("->> ")

    if userInput in greeting:
        print(random_greeting)
    elif userInput in user_input_blas:
        print(chatbot_response_blas)
    elif userInput in goodMoods:
        print(chatbot_response_good)
    elif userInput in goodbye:
        print(random_goodbye)
    elif userInput in user_input_sport:
        print(chatbot_response_sport)
    elif userInput in user_input_hobbies:
        print(chatbot_response_hobbies)
    elif userInput in user_input_days:
        print(chatbot_response_days)
    elif userInput in user_input_colour:
        print(chatbot_response_colour)
    elif userInput not in greeting:
        print("I'm not sure what you mean")
    elif userInput not in user_input_blas:
        print("I'm not sure what you mean")
    elif userInput not in user_input_goodMoods:
        print("I'm not sure what you mean")
    elif userInput not in goodbye:
        print("I'm not sure what you mean")
    elif userInput not in user_input_sport:
        print("I'm not sure what you mean")
    elif userInput not in user_input_hobbies:
        print("I'm not sure what you mean")
    elif userInput not in user_input_days:
        print("I'm not sure what you mean")
    elif userInput not in user_input_colour:
        print("I'm not sure what you mean")




##WIKIPEDIA FUNCTION



    




    





            
            
            
    
    
