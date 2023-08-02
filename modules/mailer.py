import random

from loguru import logger

from config import PRIVATE_KEYS_PATH, PROXIES_PATH, TX_COUNT, USE_PROXY
from models import MailerClient
from utils import read_from_txt


def run_mailer():
    private_keys = read_from_txt(PRIVATE_KEYS_PATH)
    if USE_PROXY:
        proxies = read_from_txt(PROXIES_PATH)

    for private_key in private_keys:
        proxy = proxies.pop(0) if USE_PROXY else None
        mailer_client = MailerClient(private_key=private_key, proxy=proxy)

        for _ in range(random.randint(TX_COUNT[0], TX_COUNT[1])):
            mailer_client.func()

    logger.success("All accounts are finished.")
