#!/usr/bin/python3
''' get subs '''
from requests import get


def number_of_subscribers(subreddit):
    '''get subscribers total number'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'jomojay-app0'}
    res = get(url, headers=header)
    sub_total = res.json()
    try:
        subscribers = sub_total.get('data').get('subscribers')
        return int(subscribers)
    except ValueError:
        return 0
