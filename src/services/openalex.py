from typing import Dict, Any
import requests

URI: str = 'https://api.openalex.org/'


def getRandomWork() -> Dict[str, Any]:
    return requests.get(f'{URI}/works?sample=1').json()['results'][0]
