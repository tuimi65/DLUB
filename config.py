import os

class Config:
    API_ID = -1
    API_HASH = ""
    BOT_TOKEN = ""
    SESSION_STRING = "t"
    def __init__(self):
        self.API_ID = int(os.environ.get("API_ID"))
        self.API_HASH = os.environ.get("API_HASH")
        self.SESSION_STRING = os.environ.get("SESSION_STRING")

Bot = Config()