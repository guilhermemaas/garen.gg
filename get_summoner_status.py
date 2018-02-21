import requests

#RGAPI-f8b2eed3-0857-4026-bb0b-85c7968935d2

def requestSummonerData(region, summonerName, APIKey):
    #Criando URL
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    
    #Retornar o JSON, utilizando requests.get
    response = requests.get(URL)

    #Retornar JSON
    return response.json()

#print(requestSummonerData('br1','SwordArtOffline','RGAPI-f8b2eed3-0857-4026-bb0b-85c7968935d2'))

def requestRankedData(region, summonerID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/leagues/by-summoner/" + summonerID + "?api_key=" + APIKey

    response = requests.get(URL)

    return response.json()

#print(requestRankedData('br1','585438','RGAPI-f8b2eed3-0857-4026-bb0b-85c7968935d2'))

#def main():
print("Consulte o elo do de um Summoner!")

region = str(input("Informe a sua região: "))
summonerName = str(input("Informe o nome de invocador: "))
APIKey = str(input("Informe a API KEY: "))

responseJSON = requestSummonerData(region, summonerName, APIKey)

ID = responseJSON[summonerName]['id']
print(ID)
IDInvoc = str(ID)

responseJSON2 = requestRankedData(region, IDInvoc, APIKEY)

print(responseJSON2[IDInvoc][0]['tier'])
print(responseJSON2[IDInvoc][0]['entries'][0]['divison'])
print(responseJSON2[IDInvoc][0]['entries'][0]['leaguepoints'])