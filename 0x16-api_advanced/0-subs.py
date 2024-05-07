#!/usr/bin/python3
''' get subs '''
from requests import get


def number_of_subscribers(subreddit):
    '''get subscribers total number'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'jomojay-app0'}
    res = get(url, headers=header)
    if res.status_code == 200:
        data = res.json()
        return data.get('data').get('subscribers')
    else:
        return 0
