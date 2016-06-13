# Slack Stock Bot

## Build Stock Bot Container

- Create slack bot user and generate API key.
- Replace KEY and Channel name in Dockerfile ENV instructions.
- Build and start container image.


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

The following image demonstrates all of the above examples.

![](./media/stock-bot.png)


