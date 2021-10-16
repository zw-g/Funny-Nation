from src.data.casino.table.BlackJackTable import BlackJackTable

from discord import Client, Message, Member, DMChannel

from src.data.casino import Casino
from src.data.poker.Card import Card


async def blackJackHit(self: Client, message: Message, casino: Casino):
    table: BlackJackTable = casino.getTable(message.channel.id)
    playerID: int = message.author.id
    user: Member = message.author
    if table is None:
        await message.channel.send("这里没人开游戏")
        return
    if not table.hasPlayer(playerID):
        await message.channel.send("你不在这场牌局里")
        return

    if table.shouldStopHitting(playerID):
        await message.channel.send("你不能再要了")
        return
    card: Card = table.hit(playerID)
    dmChannel: DMChannel = await user.create_dm()
    await dmChannel.send(card.getString())
    await dmChannel.send("你还要吗")