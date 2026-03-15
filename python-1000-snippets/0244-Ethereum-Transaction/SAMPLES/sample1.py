# sample1.py
# Show account balances, nonces, and gas price on a local eth-tester chain.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main():
    w3 = Web3(EthereumTesterProvider())

    accounts = w3.eth.accounts
    print("Accounts:", accounts)

    for acct in accounts[:3]:
        balance = w3.eth.get_balance(acct)
        nonce = w3.eth.get_transaction_count(acct)
        print(f"{acct} balance={balance} wei nonce={nonce}")

    print("Current gas price:", w3.eth.gas_price)


if __name__ == "__main__":
    main()
