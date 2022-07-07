import requests
import time
from pprint import pprint

todate = int(time.time())
fromdate = todate - 172800


def get_quantity():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=' + f'{fromdate}' + '&todate=' + f'{todate}' + \
          '&order=desc&sort=creation&tagged=python&site=stackoverflow&filter=total'
    response = requests.get(url)
    return response.json()


def all_requests():
    final_resp = []
    page = (get_quantity()['total'] // 100) + 1
    print(page)
    while page > 0:
        url = 'https://api.stackexchange.com/2.3/questions?page=' + f'{page}' + '&pagesize=100&fromdate=' + \
                  f'{fromdate}' + '&todate=' + f'{todate}' + '&order=desc&sort=creation&tagged=python&site=stackoverflow'
        response = requests.get(url).json()
        for item in response['items']:
            final_resp.append(item['title'])
        page -= 1
    return final_resp


if __name__ == '__main__':
     print(get_quantity())
     pprint(all_requests())