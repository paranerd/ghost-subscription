# Ghost Subscription
Want to stay up-to-date with a website that doesn't provide a newsletter? Or maybe you just don't want to subscribe to the newsletter but still want the updates?

Ghost Subscription to the rescue!

It allows you to 'subscribe' to a website and get notified on new articles.

With the highly expandable plugin system you can subscribe to virtually any website for updates.

## Prerequisites
You will need a config file in the following format:
```
{
    "mail_user": "your-mail@example.com",
    "mail_pass": "your-password",
    "subscriptions": [
        "plugin-name",
        "another-plugin-name"
    ]
}
```

## Run with Docker
While you can run the tool by simply calling `python3 main.js`, it may be convenient to run it in a Docker container:
```
docker run --rm --name ghost-subscription -v /path/to/config:/app/config paranerd/ghost-subscription crawl
```
