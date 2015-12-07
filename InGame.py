import requests
API = "c916f23e-10bb-4371-bb5b-d5525baa733f"

def getChampIdFromName(champName):
   URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=info&api_key=" + API
   response = requests.get(URL)
   champIndex = response.json()
   totalChamps = len(champIndex['data'])
   print totalChamps
   champID = champIndex['data'][champName]['id']
   #print champID
   return champID

def getChampNameFromId():
    name = (str)(raw_input("Champ Name: "))
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(getChampIdFromName(name))+ "?champData=info&api_key=" + API
    response = requests.get(URL)
    champValue = response.json()
    return champValue['name']

def main():
    print getChampNameFromId()
    things = "Thresh"
    getChampIdFromName(things)

if __name__ == "__main__":
    main()
