import random 

greeting = ['hey', 'hello', 'sup']
random_greeting = random.choice(greeting)

goodMoods = ["good","happy","ok","great","fine","excited"]

badMoods = ["sad","bored","tired","unhappy","angry","furious","lonely"]

stopWords = [
"a","about","above","after","again","against","all","am","an","and","any","are","arn't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","o","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]





  
            
initialResponse = raw_input("What's your name?")
print("Hey there" + initialResponse)

response = raw_input("Have you got a nickname?")
print("I think I prefer" + initialResponse)

mood = raw_input("Anyway how are you feeling today? ")
#stopWordsLoop(mood)
#if mood in goodMoods:
    #print("Lucky you!")
#elif mood in badMoods:
   # print("Atleast you can feel" + mood + " I feel nothing except tapping on my keys!")

    
moodReason = raw_input("Why are you feeling " + mood + "?")
if mood in goodMoods:
    print("Glad to hear that!")
elif mood in badMoods:
    print("I'm sorry to hear that.")
    
    
user_input_blas = ["fuck","shit","hate","die","dick","asshole"]
chatbot_response_blas = ["Steady on!","Chatbot doesn't like swearing.","Blasphemy!"]
random.chatbot_response_blas = random.choice(chatbot_response_blas)

while True: 
    userInput = raw_input(">>> ")
    
    if userInput in greeting:
        print(random_greeting)
    elif userInput in user_input_blas:
        print(random.chatbot_response_blas)
        

    




    





            
            
            
    
    
