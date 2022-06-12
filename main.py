import asyncio

import modules.utility as utility
import modules.price_module as price_module
import modules.overview_module as overview_module
import modules.alert_module as alert_module

from discord.ext import commands

bot = commands.Bot(command_prefix = '!')
bot.alert_prices_above = {  }
bot.alert_prices_below = {  }

@bot.command()
async def price(ctx, ticker: str) -> None:
    """CURRENT PRICE OF PASSED TICKER"""
    
    json_data = utility.fetch(f'https://stockanalysis.com/stocks/{ticker}/')
    message = price_module.console(json_data)
    await ctx.send(message)

@bot.command()
async def overview(ctx, ticker: str) -> None:
    """OVERVIEW OF PASSED TICKER"""

    json_data = utility.fetch(f'https://stockanalysis.com/stocks/{ticker}/')
    message = overview_module.console(json_data)
    await ctx.send(message)

async def alert_above_func(ctx, ticker):
    
    json_data = utility.fetch(f'https://stockanalysis.com/stocks/{ticker}/')

    while True:

        current_price = alert_module.fetch_current_price(json_data)

        messages = alert_module.check_above(current_price, bot.alert_prices_above)

        for message in messages:
            await ctx.send(message)

        if bot.alert_prices_above:
            break

        await asyncio.sleep(30)

@bot.command()
async def alert_above(ctx, ticker: str, alert_price: float) -> None:
    """SET PRICE ABOVE ALERT FOR PASSED TICKER"""
    alert_module.add_alert_price(ticker.upper(), alert_price, bot.alert_prices_above)
    bot.loop.create_task(alert_above_func(ctx, ticker))

async def alert_below_func(ctx, ticker):

    json_data = utility.fetch(f'https://stockanalysis.com/stocks/{ticker}/')

    while True:

        current_price = alert_module.fetch_current_price(json_data)

        messages = alert_module.check_below(current_price, bot.alert_prices_below)

        for message in messages:
            await ctx.send(message)

        if bot.alert_prices_below:
            break

        await asyncio.sleep(30)

@bot.command()
async def alert_below(ctx, ticker: str, alert_price: float) -> None:
    """SET PRICE BELOW ALERT FOR PASSED TICKER"""
    alert_module.add_alert_price(ticker.upper(), alert_price, bot.alert_prices_below)
    bot.loop.create_task(alert_below_func(ctx, ticker, alert_price))

if __name__ == '__main__':
    api_key = utility.fetch_api_key()
    bot.run(api_key)