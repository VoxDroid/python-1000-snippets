# sample3.py
# Demonstrates creating an event filter and reading logs from a smart contract.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
import solcx


SIMPLE_CONTRACT_SOURCE = """
pragma solidity ^0.8.0;

contract Counter {
    uint256 public count;

    event Incremented(uint256 newValue);

    function increment() public {
        count += 1;
        emit Incremented(count);
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

    # Create a filter for Incremented events.
    event_filter = contract.events.Incremented.createFilter(fromBlock="latest")

    # Trigger the event twice.
    contract.functions.increment().transact({"from": acct})
    contract.functions.increment().transact({"from": acct})

    events = event_filter.get_all_entries()
    for evt in events:
        print("Event Incremented, new value:", evt["args"]["newValue"])


if __name__ == "__main__":
    main()
