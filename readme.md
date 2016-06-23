# Slack Stock Bot

Simple Slack bot that will return the current stock price for a given set of stock symbols.

![](./media/stock-bot.png)

## Build Stock Bot Container

- Create slack bot user and generate API key.
- Build container image from Dockerfile.

## Start Bot

The Slack Stock Bot takes two arguments:
- --slack-token – this is the slack API token
- --slack-channel – this is the slack channel

The Docker Run command will look like this:

```none
docker run -it b4191f06a147 --slack-token xoxb-77643255603-kM6lA5yuenpBxwWdewrvdRSU --slack-channel stock-demo
```

## Use Stock Bot

When the stock bot has been successfully started, a startup message will be displayed.

To return the current stock price use:

```none
stock:symbol
```

For example:

```none
stock:msft
```

Multiple symbols can be combined like this:

```none
stock:msft;xoml;gpro
```


