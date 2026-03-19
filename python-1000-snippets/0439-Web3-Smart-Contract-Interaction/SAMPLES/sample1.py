# sample1.py
# Demonstrates deploying and interacting with a smart contract using web3 and eth-tester.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
import solcx


SIMPLE_CONTRACT_SOURCE = """
pragma solidity ^0.8.0;

contract Counter {
    uint256 public count;

    function increment() public {
        count += 1;
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

    Counter = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Counter.constructor().transact({"from": acct})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)

    # Call contract function and read state.
    contract.functions.increment().transact({"from": acct})
    value = contract.functions.count().call()
    print("Counter value after increment:", value)


if __name__ == "__main__":
    main()
