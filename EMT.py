import requests
import json

# open json files
with open("buses.json") as f:
    data = json.load(f)

# constant url, do not change or everything stops working
URL = "http://api.interurbanos.welbits.com/v1/stop/"


def getEtsiinf():
    stopNumber = "08771"
    """Returns a dictionary with (busNumber => time) to stopNumber"""
    busLines =  data[stopNumber]["bus"]

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    answer = {}

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        for j in range (0, len(busLines)):
            if(aux == busLines[j]):
                answer[busLines[j]] = req["lines"][i]["waitTime"]

    stopNumber = "17573"
    busLines =  data[stopNumber]["bus"]

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        for j in range (0, len(busLines)):
            if(aux == busLines[j]):
                answer[busLines[j]] = req["lines"][i]["waitTime"]

    stopNumber = "08411"
    busLines =  data[stopNumber]["bus"]

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        for j in range (0, len(busLines)):
            if(aux == busLines[j]):
                answer[busLines[j]] = req["lines"][i]["waitTime"]

    if(answer == {}):
        return None
    return answer

def getColonia():
    stopNumber = "08409"
    """Returns a dictionary with (busNumber => time) to stopNumber"""
    busLines =  data[stopNumber]["bus"]

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    answer = {}

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        for j in range (0, len(busLines)):
            if(aux == busLines[j]):
                answer[busLines[j]] = req["lines"][i]["waitTime"]

    if(answer == {}):
        return None
    return answer

def getSpecificBus(place, busNumber):
    """Returns a dictionary with (busNumber => time) to stopNumber"""

    stopNumber = 0
    for i in data:
        if(data[i]["start"] == place and busNumber in data[i]["bus"]):
            stopNumber = i

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    answer = []

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        if(aux == busNumber):
            answer.append(req["lines"][i]["waitTime"])

    if(answer == []):
        return None
    return answer


def main():
    print("Here we go!")
    res = getSpecificBus("etsiinf", "573")

    for i in res:
        print(i)

# main()
