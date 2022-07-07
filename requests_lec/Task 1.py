import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url).json()


def smartest_hero(hero_list):
    intelligence_max = 0
    for hero in response:
        if hero['name'] in hero_list and hero['powerstats']['intelligence'] > intelligence_max:
            intelligence_max = hero['powerstats']['intelligence']
            max_hero = hero['name']
    print(f'Самый умный супергерой - {max_hero}, его интеллект - {intelligence_max}')


if __name__ == '__main__':
    smartest_hero(['Thanos', 'Captain America', 'Hulk'])
