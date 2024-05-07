#!/usr/bin/python3
''' get subs '''

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'jomojay-app0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
