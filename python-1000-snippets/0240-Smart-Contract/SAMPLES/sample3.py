# sample3.py
# Demonstrate executing a contract call that reverts and handling the error.

from web3 import Web3
from web3.exceptions import ContractLogicError
from web3.providers.eth_tester import EthereumTesterProvider
from eth_tester.exceptions import TransactionFailed
from solcx import compile_source, install_solc, set_solc_version

SIMPLE_STORAGE_SOURCE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    function willRevert() public pure {
        require(false, "This always reverts");
    }
}
"""


def compile_contract(solidity_source: str, contract_name: str, solc_version: str = "0.8.20"):
    install_solc(solc_version)
    set_solc_version(solc_version)

    compiled = compile_source(solidity_source, output_values=["abi", "bin"])
    key = f"<stdin>:{contract_name}"
    contract_interface = compiled[key]
    return contract_interface["abi"], contract_interface["bin"]


def get_web3():
    return Web3(EthereumTesterProvider())


def deploy_simple_storage(w3: Web3):
    abi, bytecode = compile_contract(SIMPLE_STORAGE_SOURCE, "SimpleStorage")
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    tx_hash = contract.constructor().transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=receipt.contractAddress, abi=abi)


def main():
    w3 = get_web3()
    storage = deploy_simple_storage(w3)

    try:
        storage.functions.willRevert().transact({"from": w3.eth.accounts[0]})
    except (ContractLogicError, TransactionFailed) as e:
        # web3/eth-tester wrap the revert reason in the exception message
        print("Transaction reverted as expected:", str(e))


if __name__ == "__main__":
    main()
