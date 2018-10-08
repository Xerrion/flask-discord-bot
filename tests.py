import os
import cassiopeia as lol

lol.set_riot_api_key(os.environ.get('RIOT_API_KEY'))

summoner = lol.get_summoner(name='Xerrion', region='EUNE')

print(f'{summoner.match_history_uri}')
