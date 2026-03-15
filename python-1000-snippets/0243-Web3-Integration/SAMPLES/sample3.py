# sample3.py
# Compile and deploy a simple contract using eth-tester and call a function.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source, install_solc, set_solc_version

CONTRACT_SOURCE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    uint256 public count;

    function increment() public {
        count += 1;
    }
}
"""


def compile_contract():
    install_solc("0.8.20")
    set_solc_version("0.8.20")
    compiled = compile_source(CONTRACT_SOURCE, output_values=["abi", "bin"])
    return compiled["<stdin>:Counter"]


def main():
    w3 = Web3(EthereumTesterProvider())

    contract_data = compile_contract()
    contract = w3.eth.contract(abi=contract_data["abi"], bytecode=contract_data["bin"])

    tx_hash = contract.constructor().transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    counter = w3.eth.contract(address=receipt.contractAddress, abi=contract_data["abi"])

    print("Initial count:", counter.functions.count().call())
    tx_hash = counter.functions.increment().transact({"from": w3.eth.accounts[0]})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Count after increment:", counter.functions.count().call())


if __name__ == "__main__":
    main()
