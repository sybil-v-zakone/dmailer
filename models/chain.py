class Chain:
    def __init__(
        self,
        name: str,
        rpc: str,
        chain_id: int,
        coin_symbol: str,
        explorer: str,
        decimals: int = 18,
    ):
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.coin_symbol = coin_symbol
        self.decimals = decimals
        self.explorer = explorer

    def __str__(self):
        return f"{self.name}"
