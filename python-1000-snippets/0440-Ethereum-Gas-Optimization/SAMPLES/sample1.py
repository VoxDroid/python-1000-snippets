# sample1.py
# Demonstrates estimating gas for deploying a smart contract using eth-tester.

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


def compile_contract(optimize: bool = False) -> tuple[dict, str]:
    # Ensure solc is available.
    solcx.install_solc("0.8.0")
    compiled = solcx.compile_source(
        CONTRACT_SOURCE,
        output_values=["abi", "bin"],
        solc_version="0.8.0",
        optimize=optimize,
        optimize_runs=200,
    )
    _, contract_interface = compiled.popitem()
    return contract_interface["abi"], contract_interface["bin"]


def main() -> None:
    w3 = Web3(EthereumTesterProvider())
    account = w3.eth.accounts[0]

    abi, bytecode = compile_contract(optimize=False)
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    gas_estimate = contract.constructor().estimate_gas({"from": account})
    print("Estimated gas for deployment:", gas_estimate)

    tx_hash = contract.constructor().transact({"from": account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Actual gas used:", receipt.gasUsed)
    print("Deployed contract:", receipt.contractAddress)


if __name__ == "__main__":
    main()
