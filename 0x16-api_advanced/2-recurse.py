#!/usr/bin/python3
""" GET all hot posts from a subreddit """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ GET all hot posts from a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
