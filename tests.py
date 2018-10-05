import os
import cassiopeia as lol

lol.set_riot_api_key(os.environ.get('LOL_API_KEY'))
lol.set_default_region('EUNE')

summoner = lol.get_summoner(name='Xerrion')

print("{name} is a level summoner on the {region} server.".format(name=summoner.name, region=summoner.region))
