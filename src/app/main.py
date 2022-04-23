from time import sleep
from typing import List
from anyio import TypedAttributeLookupError
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from dataclasses import asdict
import json
import pandas as pd
import uuid
import twint
import asyncio
import time, datetime
from googletrans import Translator
from app.twiter_search import search_twit
from app.translate_twit import translate_twit
asyncio.set_event_loop(asyncio.new_event_loop())


@dataclass
class TweetResponse:
    share: str
    tweet: List[str]
# def get_user_info(username):
#     c = twint.Config()
#     c.Username = username
#     c.Pandas = True
#     twint.run.Following(c)
#     list_of_followings = twint.storage.panda.Follow_df

#     return list_of_followings


# def search_twint(search):
#     file = search + str(uuid.uuid1())
#     c = twint.Config()
#     c.Search = search  # "cloudflare"
#     c.Pandas = True
#     c.Since = (datetime.date.today()-datetime.timedelta(days=2)).strftime('%Y-%m-%d')
#     c.Until = datetime.date.today().strftime('%Y-%m-%d')
#     twint.run.Search(c)
#     data = twint.output.panda.Tweets_df[["username", "tweet"]]
#     return data

# def translate_data(data):
#     translator = Translator()
#     print(data.head())
#     data["tweet"] = data["tweet"].apply(lambda x: translator.translate(x).text)
#     return data

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/twins/{search}")
def get_twiter(search):
    df =  search_twit(search)
    model = TweetResponse(share=search,tweet = df["tweet"].tolist())
    return asdict(model)

# @app.get("/translate")
# def get_twiter(search):
#     df =  search_twit(search)
#     data = translate_twit(df["tweet"])
#     model = TweetResponse(share=search,tweet = data.tolist())
#     return asdict(model)

@app.get("/analysis/{search}")
def get_analysis(search):
    #moc servise response with twits analysis as positive and negativ posts
    data = {"stock": search, "positive": 200,"negative":300 }
    return data#{"stock": search, "positive": data["pos"].len,"negative":data["neg"].len }
