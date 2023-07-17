import requests

uri = 'https://api.openalex.org/'


def getRandomWork():
    return requests.get(f'{uri}/works?sample=1').json()['results'][0]
