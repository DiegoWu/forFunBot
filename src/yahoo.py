# yahoo.py

from bs4 import BeautifulSoup as bs 
import requests
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import discord
import os
from discord.ext import commands
class Stonk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        help = 
        '''
        TSMC is the best stock in Taiwan, please enter the stock number to get the stock price diagram
        note: some graph's line may be inconsistent due to the fact that that the stock is really unpopular QQ 
        ''', 
        brief = "Print current day's simple stock price diagram"
    )
    async def stonk(self, ctx):
        await ctx.send("please enter stock number:")
        t= await self.bot.wait_for('message', timeout= 300.0)
        if t.content== '2330':
            await ctx.send("TSMC!!!")
        try:
            r= requests.get(f'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22{t.content}.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true')
            jd =r.json()['data']
        except Exception as CommandInvokeError:
            await ctx.send("stock not found")
        close = jd[0]['chart']['indicators']['quote'][0]['close']
        timestamp = jd[0]['chart']['timestamp']
        df = pd.DataFrame({'timestamp': timestamp, 'close':close})
        df['dt'] = pd.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
        plt.plot(df['dt'], df['close']) 
        plt.title("stonk {}".format(t.content), fontsize=24) #tile
        plt.xlabel("time", fontsize=16) #x axis label
        plt.ylabel("price", fontsize=20) 
        plt.savefig(os.path.join("..", "storage",'stonk.png'), bbox_inches='tight') 
        plt.close() 
        await ctx.send("done!")  
        try:
            with open(os.path.join("..", "storage", "stonk.png"), "rb") as f:
                picture = discord.File(f) # convert files to discord campatible format
                await ctx.send(file = picture) # Bot sends picture
        except FileNotFoundError:
            await ctx.send('Saved image not found!')
    @commands.command(
        help= "get stats for stock index",
        brief= "get the overall info of Taiwan's stock market"
    )
    async def tmarket(self, ctx):
        r= requests.get('https://tw.stock.yahoo.com/')
        soup= bs(r.text, "html.parser")
        z= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Ai\(fe\).Jc\(fe\) > span')
        c= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Ai\(fe\).Jc\(fe\) > div > span')
        v= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Ai\(fe\).Jc\(fe\) > div > div')
        vv= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Mt\(12px\) > div:nth-child(1)')
        vvv= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Mt\(12px\) > div:nth-child(2)')
        cc= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Mt\(12px\) > div:nth-child(3)')
        ccc= soup.select('#main-0-ComponentGrid-Proxy > div > div.grid-item.item-span-8.default-row-gap > div > div > div.D\(f\).Mt\(8px\).Bd.Bdc\(\$bd-primary-divider\).Ov\(h\) > div > div.D\(f\).Mt\(12px\) > div:nth-child(4)')
        await ctx.send("Taiwanese Stock Index（listed comapanies: ")
        await ctx.send(z[0].text)
        await ctx.send(c[0].text)
        await ctx.send("stock flunctuations and percentage: ")
        await ctx.send(v[0].text)
        await ctx.send(vv[0].text)
        await ctx.send(vvv[0].text)
        await ctx.send(cc[0].text)
        await ctx.send(ccc[0].text)


def setup(bot):
    bot.add_cog(Stonk(bot))