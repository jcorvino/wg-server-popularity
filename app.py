import os
import requests


def get_active_players(app_id: str) -> dict:
    """
    Query the WG API to get the number of active players for each server

    :param app_id: WG API secret application id
    :return: player counts for each game on each region
    """
    query = {'application_id': app_id}
    host = 'https://api.worldoftanks'
    regions = {
        'Russia': '.ru',
        'Europe': '.eu',
        'North America': '.com',
        'Asia': '.asia'
    }
    end_point = '/wgn/servers/info/'

    player_count = {region: dict() for region in regions.keys()}
    for region, domain in regions.items():
        url = host + domain + end_point
        r = requests.get(url, params=query)
        for game, servers in r.json()['data'].items():
            player_count[region][game] = sum(server['players_online'] for server in servers)
    return player_count


if __name__ == '__main__':
    WG_API_SECRET = os.getenv('WG_API_SECRET')
    
    players = get_active_players(WG_API_SECRET)
    print(players)
