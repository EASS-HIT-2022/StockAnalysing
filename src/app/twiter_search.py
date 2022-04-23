import time, datetime
import twint
import pandas as pd
def search_twit(search):
    # file = search + str(uuid.uuid1())
    tasks = []
    df = pd.DataFrame()
    # for i in range(7):
    #     c = twint.Config()
    #     c.Search = search  # "cloudflare"
    #     c.Pandas = True
    #     c.Since = (datetime.date.today()-datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
    #     c.Until = (datetime.date.today()-datetime.timedelta(days=i)).strftime('%Y-%m-%d')
    #     task =  await twint.run.Search(c)
    #     tasks.append(asyncio.create_task(task))
    # await asyncio.gather(*tasks)
    c = twint.Config()
    c.Search = search  # "cloudflare"
    c.Pandas = True
    c.Hide_output = True
    c.Since = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    c.Until = (datetime.date.today()).strftime('%Y-%m-%d')
    twint.run.Search(c)
    # results=await [t.result() for t in tasks]
    # df = pd.concat(results, ignore_index=True)
    data =  twint.output.panda.Tweets_df[["username", "tweet"]]
    return data
# async def main():
#     df = await search_twit("cloudflare")
#     print(df)
# if __name__ == "__main__":
#     asyncio.run(main())