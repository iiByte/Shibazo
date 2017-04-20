import discord
import asyncio
import numpy
from discord.ext.commands import Bot
import logging
import math


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='shibazo.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

shibazo = Bot(command_prefix="?")

@shibazo.command()
async def hello(*args):
	return await shibazo.say("such hello")

@shibazo.command()
async def shoutout(name):
	return await shibazo.say(name +" many shoutout")

@shibazo.command()
async def add(num1,num2):
	answer = int(num1) + int(num2)
	return await shibazo.say(answer)

@shibazo.command()
async def subtract(num1,num2):
	answer = int(num1) - int(num2)
	return await shibazo.say(answer)

@shibazo.command()
async def multiply(num1,num2):
	answer = int(num1) * int(num2)
	return await shibazo.say(answer)

@shibazo.command()
async def divide(num1,num2):
	answer = int(num1) / int(num2)
	return await shibazo.say(answer)

@shibazo.command()
async def square(num):
	answer = int(num) ** 2
	return await shibazo.say(answer)

@shibazo.command()
async def sqrt(num):
	answer = math.sqrt(int(num))
	return await shibazo.say(answer)

shibazo.run("MzAzMzU3NzcyMDg5NjU1Mjk2.C9efrA.BRrpp-Mq_wIdIL43E0srOHdxCBg")