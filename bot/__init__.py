import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "20219667"))
    API_HASH = os.environ.get("API_HASH" , "82b82bcd10c857178cc49e22f5e8d67c" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN" , "6299210485:AAEb3tjYjE8DmwqX8ZCQ98kx8XcA3Q9Vals")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "spectreurluploaderbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
