# Discord Meme Bot
A simple Discord bot to spam memes 24/7
## Steps to deploy to Heroku
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and login: ```heroku login```

2. Download/Clone this repo: ```git clone https://github.com/AbstractGhoul05/discord_meme_bot.git```

3. Enter meme bot directory: ```cd discord_meme_bot```

4. Create ```config.yaml```: ```cp sample_config.yaml config.yaml```

5. Track and commit ```config.yaml```: ```git add config.yaml && git commit -m "Add config.yaml"```

6. Create a new Heroku app: ```heroku create myapp --buildpack heroku/python```
Note: Replace myapp with your desired name without spaces

6. Deploy bot to Heroku: ```git push heroku master```

7. Start worker dyno: ```heroku ps:scale worker=2``` 

## Steps to setup Locally/Server
1. Download/Clone this repo: ```git clone https://github.com/AbstractGhoul05/discord_meme_bot.git```

2. Enter meme bot directory: ```cd discord_meme_bot```

3. Create ```config.yaml```: ```cp sample_config.yaml config.yaml```

4. Install requirments,
for Windows:
```pip install -r requirments.txt```
or for others:
```pip3 install -r requirments.txt```

5. Run the bot
for Windows:
```python main.py```
or for others:
```python3 main.py```
