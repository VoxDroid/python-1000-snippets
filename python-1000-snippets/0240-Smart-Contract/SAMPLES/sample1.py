# sample1.py
# Deploy a simple Solidity contract and call its getter/setter.

from web3 import Web3
from web3.exceptions import ContractLogicError
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source, install_solc, set_solc_version

SIMPLE_STORAGE_SOURCE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private value;

    event ValueChanged(uint256 newValue);

    function set(uint256 newValue) public {
        value = newValue;
        emit ValueChanged(newValue);
    }

    function get() public view returns (uint256) {
        return value;
    }

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

    print("Initial value:", storage.functions.get().call())

    tx_hash = storage.functions.set(123).transact({"from": w3.eth.accounts[0]})
    w3.eth.wait_for_transaction_receipt(tx_hash)

    print("New value:", storage.functions.get().call())


if __name__ == "__main__":
    main()
