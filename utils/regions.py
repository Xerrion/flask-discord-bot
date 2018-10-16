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


def get_region(region=None):
    if not region:
        return None
    for r, d in regions.items():
        if r == region:
            return d['domain']
