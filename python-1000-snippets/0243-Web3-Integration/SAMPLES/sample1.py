# sample1.py
# Connect to an in-memory Ethereum chain and print basic chain info.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main():
    w3 = Web3(EthereumTesterProvider())
    print("Connected:", w3.is_connected())
    print("Chain ID:", w3.eth.chain_id)
    print("Latest block number:", w3.eth.block_number)
    print("Accounts:", w3.eth.accounts)


if __name__ == "__main__":
    main()
