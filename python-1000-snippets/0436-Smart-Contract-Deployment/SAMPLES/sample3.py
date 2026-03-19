# sample3.py
# Demonstrates reading events emitted by a smart contract.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
import solcx


SIMPLE_CONTRACT_SOURCE = """
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public value;

    event ValueChanged(uint256 newValue);

    function set(uint256 newValue) public {
        value = newValue;
        emit ValueChanged(newValue);
    }
}
"""


def main() -> None:
    solcx.install_solc("0.8.0")
    compiled = solcx.compile_source(
        SIMPLE_CONTRACT_SOURCE,
        output_values=["abi", "bin"],
        solc_version="0.8.0",
    )

    _, contract_interface = compiled.popitem()
    abi = contract_interface["abi"]
    bytecode = contract_interface["bin"]

    w3 = Web3(EthereumTesterProvider())
    acct = w3.eth.accounts[0]

    SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = SimpleStorage.constructor().transact({"from": acct})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    tx_hash = contract.functions.set(100).transact({"from": acct})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Parse events from the receipt.
    events = contract.events.ValueChanged().processReceipt(receipt)
    for evt in events:
        print("ValueChanged event:", evt["args"])


if __name__ == "__main__":
    main()
