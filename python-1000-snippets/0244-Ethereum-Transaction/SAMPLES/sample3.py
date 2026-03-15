# sample3.py
# Create a local account, fund it on eth-tester, sign a raw transaction, and broadcast it.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider


def main():
    w3 = Web3(EthereumTesterProvider())

    # Create a local (offline) account
    acct = w3.eth.account.create()
    print("Local account:", acct.address)

    # Fund the account from a pre-funded eth-tester account
    funder = w3.eth.accounts[0]
    tx = {
        "from": funder,
        "to": acct.address,
        "value": w3.to_wei(1, "ether"),
    }
    fund_hash = w3.eth.send_transaction(tx)
    w3.eth.wait_for_transaction_receipt(fund_hash)

    print("Balance after funding:", w3.eth.get_balance(acct.address))

    # Build a transaction to send funds back
    tx = {
        "nonce": w3.eth.get_transaction_count(acct.address),
        "to": w3.eth.accounts[1],
        "value": w3.to_wei(0.1, "ether"),
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
        "chainId": w3.eth.chain_id,
    }

    signed = acct.sign_transaction(tx)
    raw = signed.raw_transaction.hex()

    # Broadcast the signed raw transaction
    tx_hash = w3.eth.send_raw_transaction(raw)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print("Signed raw transaction hash:", receipt.transactionHash.hex())
    print("Recipient balance:", w3.eth.get_balance(w3.eth.accounts[1]))


if __name__ == "__main__":
    main()
