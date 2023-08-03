import json
import random
import time
from functools import wraps

from loguru import logger
from tqdm import tqdm
from web3 import Web3

from models.chain import EthMainet


def read_from_json(file_path):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        logger.exception(f"File '{file_path}' not found.")
    except Exception as e:
        logger.exception(f"Encountered an error while reading a JSON file '{file_path}': {e}.")


def read_from_txt(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError as e:
        logger.exception(f"File '{file_path}' not found.")
    except Exception as e:
        logger.exception(f"Encountered an error while reading a TXT file '{file_path}': {str(e)}.")


def gas_delay(gas_threshold: int, delay_range: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                current_eth_gas_price = get_eth_gas_fee()
                threshold = Web3.to_wei(gas_threshold, "gwei")
                if current_eth_gas_price > threshold:
                    random_delay = random.randint(delay_range[0], delay_range[1])

                    logger.warning(
                        f"Current gas fee '{current_eth_gas_price}' wei > Gas threshold '{threshold}' wei. Waiting for {random_delay} seconds..."
                    )

                    with tqdm(total=random_delay, desc="Waiting", unit="s", dynamic_ncols=True, colour="blue") as pbar:
                        for _ in range(random_delay):
                            time.sleep(1)
                            pbar.update(1)
                else:
                    break

            return func(*args, **kwargs)

        return wrapper

    return decorator


def wait(delay_range: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            random_delay = random.randint(delay_range[0], delay_range[1])
            logger.info(f"Sleeping for {random_delay} seconds...")
            with tqdm(total=random_delay, desc="Waiting", unit="s", dynamic_ncols=True, colour="blue") as pbar:
                for _ in range(random_delay):
                    time.sleep(1)
                    pbar.update(1)
            return result

        return wrapper

    return decorator


def get_eth_gas_fee():
    w3 = Web3(Web3.HTTPProvider(EthMainet.rpc))
    return w3.eth.gas_price


def check_balance(min_balance):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            balance = self.w3.eth.get_balance(self.public_key)
            if balance < Web3.to_wei(min_balance, "ether"):
                logger.error(f"Balance is below minimum at {self.public_key}.")
                return False
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
