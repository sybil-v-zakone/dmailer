import json
import time
from functools import wraps

from loguru import logger
from tqdm import tqdm


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


def gas_delay(gas_threshold: int, delay_seconds: tuple):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            while True:
                current_gas_price = self.w3.eth.gas_price
                logger.info(current_gas_price)
                if current_gas_price > gas_threshold:
                    logger.warning(f"Gas price above set threshold. Waiting for {delay_seconds} seconds...")
                    with tqdm(
                        total=delay_seconds, desc="Waiting", unit="s", dynamic_ncols=True, colour="blue"
                    ) as pbar:
                        for _ in range(delay_seconds):
                            time.sleep(1)
                            pbar.update(1)
                else:
                    break

            return func(self, *args, **kwargs)

        return wrapper

    return decorator
