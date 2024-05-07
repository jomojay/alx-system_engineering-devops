#!/usr/bin/python3
''' Get hot posts '''
import pprint
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'jomojay-app2'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return hot_list
    res = get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
