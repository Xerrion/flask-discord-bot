import cassiopeia as cass
from riotwatcher import RiotWatcher

import settings
from requests import HTTPError

watcher = RiotWatcher(settings.RIOT_API_KEY)



my_region = 'eune'

regions = {
    'ru': {'domain': 'ru'},
    'kr': {'domain': 'kr'},
    'br': {'domain': 'br1'},
    'oca': {'domain': 'oc1'},
    'jp': {'domain': 'jp1'},
    'na': {'domain': 'na1'},
    'euw': {'domain': 'euw1'},
    'eune': {'domain': 'eun1'},
    'tr': {'domain': 'tr1'},
    'la1': {'domain': 'la1'},
    'la2': {'domain': 'la2'},
}
for region, domain in regions.items():
    if my_region is region:
        print('s')
