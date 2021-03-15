import hashlib
import requests
import lxml.html
import jinja2
from utils.config import ConfigHelper
from utils.cache import Cache
from utils.sites import Sites
from utils import mail

TEMPLATE_FILE = "templates/base.html"

config = ConfigHelper()
cache = Cache()
sites = Sites()


def run():
    subs = config.get('subscriptions')
    updates = []

    for sub in subs:
        update = check(sub, sites.get(sub))

        if update:
            updates.append(update)

    html = render_html(updates)

    if len(updates) > 0:
        send(html)


def check(sub, site):
    res = requests.get(site['url'])
    root = lxml.html.fromstring(res.content)

    title = root.xpath(site['title'])[0]
    cached = cache.get(sub)
    modified = root.xpath(site['modified'])[0]
    hashed = hashlib.md5(modified.encode()).hexdigest()

    if cached != hashed:
        link = root.xpath(site['link'])[0]

        update_cache(sub, hashed)

        return {
            'name': sub,
            'title': title.strip(),
            'link': link
        }


def update_cache(name, value):
    cache.set(name, value)


def render_html(updates):
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader, autoescape=True)
    template = template_env.get_template(TEMPLATE_FILE)

    return template.render(updates=updates)


def send(html):
    mail.send_gmail(config.get('mail_user'), config.get('mail_pass'),
                    [config.get('mail_user')], 'Ghost Subscription', html)


if __name__ == '__main__':
    run()
