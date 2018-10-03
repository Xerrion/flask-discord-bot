import os

servers = {
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
server = 'eune'
for s, d in servers.items():
    # self.response = requests.get(
    #    f"https://{d['domain']}.api.riotgames.com/lol/status/v3/shard-data?api_key={os.environ.get('LOL_API_KEY')}")
    if s == server:
        print(
            f"https://{d['domain']}.api.riotgames.com/lol/status/v3/shard-data?api_key={os.environ.get('LOL_API_KEY')}")
else:
    pass
