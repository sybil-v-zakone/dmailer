import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

ABI_DIR = os.path.join(ROOT_DIR, "abis")

DMAIL_ABI = os.path.join(ABI_DIR, "dmail_abi.json")
DMAIL_CONTRACT_ADDRESS = "0x981F198286E40F9979274E0876636E9144B8FB8E"


GAS_MULTIPLIER = 1.0

USE_PROXY = False

# gas threshold in GWEI
GAS_THRESHOLD = 20

# time delay between gas checkups in seconds
GAS_DELAY_RANGE = [10, 15]

# path to private_keys.txt file
PRIVATE_KEYS_PATH = "data/private_keys.txt"

# path to proxies.txt file
PROXIES_PATH = "data/proxies.txt"

# range of transactions to be sent on each accout
TX_COUNT = [2, 4]

# range for time delay between each transaction in seconds
TX_DELAY_RANGE = [60, 120]

# minimum balance in ether
MIN_BALANCE = 0.0001
