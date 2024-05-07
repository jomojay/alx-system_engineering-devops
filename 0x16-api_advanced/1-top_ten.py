#!/usr/bin/python3
''' get subs '''
from requests import get


def top_ten(subreddit):
    '''get subscribers total number'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'jomojay-app1'}
    res = get(url, headers=header, allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return
    children = res.json()
    try:
        children = children.get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except ValueError:
        print("None")
