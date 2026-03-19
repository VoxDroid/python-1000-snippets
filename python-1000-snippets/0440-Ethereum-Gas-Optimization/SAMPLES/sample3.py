# sample3.py
# Demonstrates how compiler optimization can affect contract deployment gas.

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


def compile_contract(optimize: bool) -> tuple[dict, str]:
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


def deploy_contract(w3: Web3, account: str, abi: dict, bytecode: str) -> tuple[Web3, int]:
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact({"from": account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return contract, receipt.gasUsed


def main() -> None:
    w3 = Web3(EthereumTesterProvider())
    account = w3.eth.accounts[0]

    for optimize in (False, True):
        abi, bytecode = compile_contract(optimize)
        gas_used = deploy_contract(w3, account, abi, bytecode)[1]
        print(f"Deploy gas used (optimize={optimize}):", gas_used)


if __name__ == "__main__":
    main()
