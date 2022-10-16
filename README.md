# Discord Meme Bot
A simple Discord bot to spam memes 24/7
## Steps to deploy to Heroku
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and login: ```heroku login```

2. Download/Clone this repo: ```git clone https://github.com/AbstractGhoul05/discord_meme_bot.git```

3. Enter meme bot directory: ```cd discord_meme_bot```

4. Get [Discord](https://discordpy.readthedocs.io/en/latest/discord.html) and [Reddit](https://github.com/reddit-archive/reddit/wiki/OAuth2#getting-started) API keys

5. Create ```config.yaml```: ```cp sample_config.yaml config.yaml```

6. Fill in the required stuff in ```config.yaml```

7. Track and commit ```config.yaml```: ```git add config.yaml && git commit -m "Add config.yaml"```

8. Create a new Heroku app: ```heroku create myapp --buildpack heroku/python```
Note: Replace myapp with your desired name without spaces

9. Deploy bot to Heroku: ```git push heroku master```

10. Start worker dyno: ```heroku ps:scale worker=2``` 

## Steps to setup Locally/Server
1. Download/Clone this repo: ```git clone https://github.com/AbstractGhoul05/discord_meme_bot.git```

2. Enter meme bot directory: ```cd discord_meme_bot```

3. Get [Discord](https://discord.com/developers/applications) and [Reddit](https://www.reddit.com/prefs/apps) API keys

4. Create ```config.yaml```: ```cp sample_config.yaml config.yaml```

5. Fill in the required stuff in ```config.yaml```

6. Install requirements,
for Windows:
```pip install -r requirements.txt```
or for others:
```pip3 install -r requirements.txt```

7. Run the bot
for Windows:
```python main.py```
or for others:
```python3 main.py```
