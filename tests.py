import cassiopeia as cass
from riotwatcher import RiotWatcher

import settings
from requests import HTTPError

from utils.regions import get_region

watcher = RiotWatcher(settings.RIOT_API_KEY)

summoner = watcher.summoner.by_name(region=get_region('eune'), summoner_name='xerrion')
league = watcher.league.positions_by_summoner(get_region('eune'), summoner['id'])


print(summoner)
print(league[0])
