import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("testanimeflix")
    BOT_TOKEN = os.getenv("7820025967:AAGeYjX4wno2aFfTE9w6VHm6Ur6VFWa_2ns")  # From botfather
    API_ID = os.getenv(
        "25812247"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "00a50dc03d5b63a0eabfca83fa02c4ca
"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("mongodb+srv://AnimeFlix:Itzmecp@cluster0.qxdxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # From Firebase database
