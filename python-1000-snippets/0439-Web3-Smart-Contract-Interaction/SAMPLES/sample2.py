# sample2.py
# Demonstrates signing and sending a raw transaction using web3 and eth-tester.

from eth_account import Account
from eth_tester import EthereumTester
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main() -> None:
    eth_tester = EthereumTester()
    w3 = Web3(EthereumTesterProvider(eth_tester))

    # Create a new account and fund it from the default funded account.
    acct = Account.create()
    eth_tester.add_account(acct.key)

    funding_account = w3.eth.accounts[0]
    w3.eth.send_transaction(
        {"from": funding_account, "to": acct.address, "value": w3.to_wei(1, "ether")}
    )

    # Build a simple transaction (send a small amount back to the funding account).
    tx = {
        "nonce": w3.eth.get_transaction_count(acct.address),
        "to": funding_account,
        "value": w3.to_wei(0.1, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei(1, "gwei"),
        "chainId": 1337,
    }

    signed = Account.sign_transaction(tx, acct.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print("Raw transaction hash:", tx_hash.hex())
    print("Transaction status:", receipt.status)


if __name__ == "__main__":
    main()
