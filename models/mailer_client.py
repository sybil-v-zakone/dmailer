from loguru import logger

from config import (
    DMAIL_ABI,
    DMAIL_CONTRACT_ADDRESS,
    GAS_DELAY_RANGE,
    GAS_THRESHOLD,
    TX_DELAY_RANGE,
)
from models import Chain
from models.chain import ZkEra
from utils import gas_delay, read_from_json, wait

from . import Client


class MailerClient(Client):
    def __init__(self, private_key: str, proxy: str = None, chain: Chain = ZkEra):
        super().__init__(private_key, chain, proxy)
        self.contract_address = DMAIL_CONTRACT_ADDRESS
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=read_from_json(DMAIL_ABI))

    @wait(delay_range=TX_DELAY_RANGE)
    @gas_delay(gas_threshold=GAS_THRESHOLD, delay_range=GAS_DELAY_RANGE)
    def send_mail(self, to: str = None, subject: str = None):
        logger.info(f"Building mail tx at {self.public_key}.")

        if not to:
            to = f"{self.public_key}@dmail.ai"
        if not subject:
            subject = f"{self.public_key}@dmail.ai"

        data = self.contract.encodeABI("send_mail", args=(to, subject))

        tx_hash = self.send_transaction(to=self.contract_address, data=data)
        logger.info(f"Sent a mail tx with hash: {self.chain.explorer}tx/{self.w3.to_hex(tx_hash)}")

        if self.verify_tx(tx_hash=tx_hash):
            return True
        return False
