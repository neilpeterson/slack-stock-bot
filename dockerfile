FROM python

ENV KEY <slack api key>
ENV CHANNEL <slack channel>

RUN pip install requests
RUN pip install slackclient
RUN mkdir stock-bot
RUN git clone https://github.com/neilpeterson/slack-stock-bot.git ./stock-bot

ENTRYPOINT python /stock-bot/slack-stock-ticker.py --slack-token $KEY --slack-channel $CHANNEL