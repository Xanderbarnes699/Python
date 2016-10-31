import twitter, sqlite3, urllib2 


historyArray = []
##list of urls



while True:

	select = sqlite3.connect("/Users/AlexBarnes/Library/Application\ Support/Google/Chrome/Default/Archived History
")
    ##opens history
    cursor = console.cursor()
    ##executes the sql 
    cursor.execute()
	
                             
    fetchInfo = select.fetchall()
    ##collects data from history
	
    
    

for row in fetchInfo:
        historyArray.append(row)
		##collects last url in history 
        recentHistory = str(historyArray[-1])
	    ##converts url into a string
        select.close

    
    
file = open("TwitterCredentials.txt")
creds = file.read().split('\n')
    ##reads in credentials
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
response = api.PostUpdate("I just viewed " + str )
print("Status updated to: " + response.text)
    ##post to twitter + print alert
    
    
	
                              
 