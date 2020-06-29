import os
import itertools

import asyncio

import requests
from urllib.parse import urlparse

import discord
from discord.ext import commands, tasks

import praw

from tinydb import TinyDB, Query

import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--config',
    default='config.yaml',
    dest='config_path',
    help='path_to_config_file'
)

args = parser.parse_args()

with open(args.config_path, mode='r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)
        exit(1)

bot_token = config['discord']['bot_token']
guild_name = config['discord']['guild_name']

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    user_agent=config['reddit']['user_agent'],
    username=config['reddit']['username'],
    password=config['reddit']['password']
)

client = discord.Client()

subreddit = reddit.subreddit(
        f"{'+'.join(sr for sr in config['content']['subreddits'])}"
    )

async def get_posts():
    return set(
        itertools.chain.from_iterable(
            getattr(subreddit, sort_type)(limit=config['content']['limit']) for sort_type in config['reddit']['sorting']
        )
    )

db = TinyDB('published_posts_id.json')

async def get_direct_link(post):
    if 'gfycat.com' in post.url:
        gfy_id = urlparse(post.url).path.partition('-')[0]
        gfy_data_url = f"https://api.gfycat.com/v1/gfycats/{gfy_id}"
        gfy_data = requests.get(gfy_data_url).json()
        return gfy_data['gfyItem']['gifUrl']
    return post.url if post.url.endswith(('jpg', 'gif', 'jpeg', 'png')) else None

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild_name:
            break
    print(f'{client.user} has connected to the following guild:\n', 
    f'{guild.name}(id: {guild.id})')
    client.loop.create_task(loop_through_memes())

async def send_memes():
    posts = await get_posts()
    for post in posts:
        check_published = Query()
        is_published = bool(db.search(check_published.post_id == post.id))
        if is_published:
            continue
        media_url = await get_direct_link(post)
        meme_channel = client.get_channel(config['discord']['channel_id'])
        await meme_channel.send(media_url)
        await meme_channel.send(f"{post.title}\nSource: [{post.subreddit_name_prefixed}]({post.shortlink})")
        db.insert({'post_id': post.id})
        await asyncio.sleep(300)

async def loop_through_memes():
    while True:
        await send_memes()

client.run(bot_token)
