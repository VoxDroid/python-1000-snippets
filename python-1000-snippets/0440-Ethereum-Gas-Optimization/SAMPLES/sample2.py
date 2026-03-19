# sample2.py
# Demonstrates estimating gas for a state-changing function call in a deployed contract.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
import solcx

CONTRACT_SOURCE = """
pragma solidity ^0.8.0;

contract GasDemo {
    uint256 public value;

    function setValue(uint256 newValue) public {
        value = newValue;
    }
}
"""


def compile_contract() -> tuple[dict, str]:
    solcx.install_solc("0.8.0")
    compiled = solcx.compile_source(
        CONTRACT_SOURCE,
        output_values=["abi", "bin"],
        solc_version="0.8.0",
        optimize=True,
        optimize_runs=200,
    )
    _, contract_interface = compiled.popitem()
    return contract_interface["abi"], contract_interface["bin"]


def main() -> None:
    w3 = Web3(EthereumTesterProvider())
    account = w3.eth.accounts[0]

    abi, bytecode = compile_contract()
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    tx_hash = contract.constructor().transact({"from": account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    deployed = w3.eth.contract(address=receipt.contractAddress, abi=abi)

    tx = deployed.functions.setValue(123).build_transaction({"from": account})
    estimate = w3.eth.estimate_gas(tx)
    print("Estimated gas to call setValue():", estimate)

    tx_hash = deployed.functions.setValue(123).transact({"from": account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Actual gas used:", receipt.gasUsed)


if __name__ == "__main__":
    main()
