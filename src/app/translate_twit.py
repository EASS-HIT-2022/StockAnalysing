from googletrans import Translator
import pandas as pd
async def translate_twit(data:pd):
    translator = Translator()
    data["tweet"] = await data["tweet"].apply(lambda x: translator.translate(x).text)
    return data