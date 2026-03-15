# sample2.py
# Send a simple transaction between two pre-funded eth-tester accounts.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main():
    w3 = Web3(EthereumTesterProvider())

    sender = w3.eth.accounts[0]
    recipient = w3.eth.accounts[1]

    balance_before = w3.eth.get_balance(recipient)
    print("Recipient balance before:", balance_before)

    tx_hash = w3.eth.send_transaction({
        "from": sender,
        "to": recipient,
        "value": w3.to_wei(1, "ether"),
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction mined in block", receipt.blockNumber)

    balance_after = w3.eth.get_balance(recipient)
    print("Recipient balance after:", balance_after)


if __name__ == "__main__":
    main()
