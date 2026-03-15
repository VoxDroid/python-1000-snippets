# sample2.py
# Send Ether between two pre-funded eth-tester accounts.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main():
    w3 = Web3(EthereumTesterProvider())

    sender = w3.eth.accounts[0]
    recipient = w3.eth.accounts[1]

    print("Sender balance before:", w3.eth.get_balance(sender))
    print("Recipient balance before:", w3.eth.get_balance(recipient))

    tx_hash = w3.eth.send_transaction({
        "from": sender,
        "to": recipient,
        "value": w3.to_wei(0.5, "ether"),
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction mined in block", receipt.blockNumber)

    print("Sender balance after:", w3.eth.get_balance(sender))
    print("Recipient balance after:", w3.eth.get_balance(recipient))


if __name__ == "__main__":
    main()
