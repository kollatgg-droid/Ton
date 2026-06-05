import os
import random
import asyncio
import time

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode

from db import *

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 123456789  # <-- поменяй

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

captcha_store = {}
join_times = []  # anti-raid
