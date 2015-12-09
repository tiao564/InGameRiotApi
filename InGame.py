import requests
API = "c916f23e-10bb-4371-bb5b-d5525baa733f"

#################################################################
#This is a program to find the game you are currently in        #
#   it will find all the summoners, then get the ranked data    #
#   of each summoner, their win rate on champ they are on.      #
#   It will also give the runes and masteries the user is       #
#`  currently using. More features will be added but this is    #
#   a start.                                                    #
#   Goal to have a graphical interface as well.                 #
#                                                               #                              
#   Program started by Dylan Guldy                              #
#   Contributors:                                               #
#       Jon Simmons                                             #
#       Avraham Blaut                                           #
#                                                               #
#   Started December 7th 2015                                   #
#                                                               #
#   Thanks to RIOT API                                          #
#################################################################
#################################
#Function getChampIdFromName    #
#   takes in string champ name  #
#   requests and grabs champ id #
#   returnes an integer         #
#################################
def getChampIdFromName(champName):
   URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=info&api_key=" + API
   response = requests.get(URL)
   champIndex = response.json()
   totalChamps = len(champIndex['data'])
   champID = champIndex['data'][champName]['id']
   #print champID
   return champID

#################################
#Function getChampNameFromId    #
#   takes in integer id of champ#
#   returns the name as a string#
#################################
def getChampNameFromId(Identity):
#   name = (str)(raw_input("Champ Name: "))
   URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(Identity)+ "?champData=info&api_key=" + API
   response = requests.get(URL)
   champValue = response.json()
   return champValue['name']
          

#################################
#Function requestSummonerData   #
#   takes in region string      #
#   summonerName string         #
#                               #
#   Retuns the json data of the #
#   rquested summoner           #
#################################
def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + API
#   print URL
#   print "\n"
    response = requests.get(URL)
    return response.json()

#################################
#Function requrestRankedData    #
#   takes in region string      #
#   ID integer                  #
#   returns the ranked data json#
#################################
def requestRankedData(region, ID):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + API
#   print "\n"
#   print URL
#   print "\n"
    response = requests.get(URL)
    return response.json()
                          

def main():
   inputChampName = (str)(raw_input("Enter name of champ: "))
   functionChampId = getChampIdFromName(inputChampName)
   print functionChampId
   functionChampName = getChampNameFromId(functionChampId)
   print functionChampName
          

if __name__ == "__main__":
    main()
