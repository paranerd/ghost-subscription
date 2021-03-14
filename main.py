import os
import requests
import lxml.html
import hashlib
from utils import util
from utils.config import ConfigHelper
from utils.cache import Cache
from utils.sites import Sites
from utils import mail

config = ConfigHelper()
cache = Cache()
sites = Sites()

def run():
    subs = config.get('subscriptions')

    for sub in subs:
        check(sub, sites.get(sub))

def check(sub, site):
    res = requests.get(site['url'])
    root = lxml.html.fromstring(res.content)

    title = root.xpath(site['title'])[0]
    cached = cache.get(sub)
    modified = root.xpath(site['modified'])[0]
    hashed = hashlib.md5(modified.encode()).hexdigest()

    if cached != hashed:
        link = root.xpath(site['link'])[0]

        send(title, link)
        update_cache(sub, hashed)

def update_cache(name, value):
    print('Setting {} to {}'.format(name, value))
    cache.set(name, value)

def send(title, link):
    print('Sending:')
    print('Title: {}'.format(title.strip()))
    print('Link: {}'.format(link))
    mail.send_gmail(config.get('mail_user'), config.get('mail_pass'), config.get('mail_user'), 'Ghost Subscription', 'worx')

if __name__ == '__main__':
    run()
