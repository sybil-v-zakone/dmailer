from loguru import logger
from web3 import Web3

from models import Chain


class Client:
    def __init__(self, private_key: str, chain: Chain, proxy: str):
        self.private_key = private_key
        self.chain = chain
        self.proxy = proxy
        self.w3 = self.init_web3()
        self.public_key = Web3.to_checksum_address(self.w3.eth.account.from_key(private_key=private_key).address)

    def init_web3(self):
        if self.proxy:
            request_kwargs = {"proxies": {"https": f"http://{self.proxy}", "http": f"http://{self.proxy}"}}
        else:
            request_kwargs = {}

        return Web3(Web3.HTTPProvider(endpoint_uri=self.chain.rpc, request_kwargs=request_kwargs))

    def send_transaction(
        self,
        to,
        data=None,
        from_=None,
        gas_multiplier=1.0,
        value=None,
    ):
        if not from_:
            from_ = self.public_key

        tx_params = {
            "chainId": self.w3.eth.chain_id,
            "nonce": self.w3.eth.get_transaction_count(self.public_key),
            "from": Web3.to_checksum_address(from_),
            "to": Web3.to_checksum_address(to),
        }

        if data:
            tx_params["data"] = data

        if value:
            tx_params["value"] = value

        tx_params["gasPrice"] = self.w3.eth.gas_price

        try:
            tx_params["gas"] = int(self.w3.eth.estimate_gas(tx_params) * gas_multiplier)
        except Exception as e:
            logger.error(f"Transaction failed: {e}")
            return None

        sign = self.w3.eth.account.sign_transaction(tx_params, self.private_key)
        return self.w3.eth.send_raw_transaction(sign.rawTransaction)

    def verify_tx(self, tx_hash) -> bool:
        try:
            data = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=200)
            if "status" in data and data["status"] == 1:
                logger.success(f"Transaction was successful: {self.chain.explorer}tx/{tx_hash.hex()}")
                return True
            else:
                logger.error(f'Transaction failed {data["transactionHash"].hex()}')
                return False
        except Exception as e:
            logger.exception(f"Unexpected error in verify_tx function: {e}")
            return False
