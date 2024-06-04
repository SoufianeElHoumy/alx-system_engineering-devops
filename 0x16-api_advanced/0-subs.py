#!/usr/bin/python3
""" GET how many subscribers a subreddit has """

import requests


def number_of_subscribers(subreddit):
    """ GET how many subscribers a subreddit has """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
