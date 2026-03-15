# sample2.py
# Deploy a contract and read events emitted by it.

from web3 import Web3
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

    # Create a filter for the ValueChanged event (latest block onwards)
    event_filter = storage.events.ValueChanged.create_filter(from_block="latest")

    tx_hash = storage.functions.set(999).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    events = event_filter.get_all_entries()
    print("Events from transaction receipt:")
    for event in events:
        print("  event", event["event"], "args", dict(event["args"]))

    # Alternatively, parse logs from the receipt directly
    parsed = storage.events.ValueChanged().process_receipt(receipt)
    print("Parsed events from receipt:")
    for evt in parsed:
        print("  event", evt["event"], "args", dict(evt["args"]))


if __name__ == "__main__":
    main()
