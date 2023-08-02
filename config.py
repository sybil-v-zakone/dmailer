import os
import sys
from pathlib import Path

from models import Chain

if getattr(sys, "frozen", False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

ABI_DIR = os.path.join(ROOT_DIR, "abis")

DMAIL_ABI = os.path.join(ABI_DIR, "dmail_abi.json")
DMAIL_CONTRACT_ADDRESS = "0x981F198286E40F9979274E0876636E9144B8FB8E"

ZkEra = Chain(
    name="zkSync Era Mainnet",
    rpc="https://zksync-era.blockpi.network/v1/rpc/public",
    chain_id=324,
    coin_symbol="ETH",
    explorer="https://explorer.zksync.io/",
)

EthMainet = Chain(
    name="Ethereum Mainnet",
    rpc="https://rpc.ankr.com/eth",
    chain_id=1,
    coin_symbol="ETH",
    explorer="https://etherscan.io/",
)

GAS_MULTIPLIER = 1.1

USE_PROXY = False

# gas threshold in GWEI
GAS_THRESHOLD = 20
