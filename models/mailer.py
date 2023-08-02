from loguru import logger

from config import DMAIL_ABI, DMAIL_CONTRACT_ADDRESS, ZkEra
from models import Chain
from utils import gas_delay, read_from_json

from . import Client


class Mailer(Client):
    def __init__(self, private_key: str, chain: Chain = ZkEra):
        super().__init__(private_key, chain)
        self.contract_address = DMAIL_CONTRACT_ADDRESS
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=read_from_json(DMAIL_ABI))

    @gas_delay(gas_threshold=20, delay_seconds=10)
    def send_mail(self, to: str):
        logger.info(f"Building mail tx at {self.public_key}.")

        to = f"{self.public_key}@dmail.ai"
        subject = f"{self.public_key}@dmail.ai"

        data = self.contract.encodeABI("send_mail", args=(to, subject))

        tx_hash = self.send_transaction(to=self.contract_address, data=data)
        logger.info(f"Sent a mail tx with hash: {self.chain.explorer}tx/{self.w3.to_hex(tx_hash)}")

        if self.verify_tx(tx_hash=tx_hash):
            return True
        return False
