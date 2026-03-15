# sample3.py
# Demonstrate reading Transfer events from the NFT contract.

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source, install_solc, set_solc_version

CONTRACT_SOURCE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleNFT {
    string public name;
    string public symbol;

    mapping(uint256 => address) private _owners;
    mapping(uint256 => string) private _tokenURIs;

    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function mint(address to, uint256 tokenId, string memory tokenURI) public {
        require(to != address(0), "Invalid to");
        require(_owners[tokenId] == address(0), "Already minted");
        _owners[tokenId] = to;
        _tokenURIs[tokenId] = tokenURI;
        emit Transfer(address(0), to, tokenId);
    }

    function transfer(address to, uint256 tokenId) public {
        require(_owners[tokenId] == msg.sender, "Not owner");
        _owners[tokenId] = to;
        emit Transfer(msg.sender, to, tokenId);
    }
}
"""


def compile_and_deploy(w3):
    install_solc("0.8.20")
    set_solc_version("0.8.20")
    compiled = compile_source(CONTRACT_SOURCE, output_values=["abi", "bin"])
    contract_interface = compiled["<stdin>:SimpleNFT"]

    contract = w3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
    tx_hash = contract.constructor("ExampleNFT", "ENFT").transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=receipt.contractAddress, abi=contract_interface["abi"])


def main():
    w3 = Web3(EthereumTesterProvider())
    nft = compile_and_deploy(w3)

    alice = w3.eth.accounts[0]
    bob = w3.eth.accounts[1]

    tx1 = nft.functions.mint(alice, 1, "https://example.com/nft/1").transact({"from": alice})
    receipt1 = w3.eth.wait_for_transaction_receipt(tx1)

    tx2 = nft.functions.transfer(bob, 1).transact({"from": alice})
    receipt2 = w3.eth.wait_for_transaction_receipt(tx2)

    # Read Transfer events from receipts
    print("Events from mint transaction:")
    for event in nft.events.Transfer().process_receipt(receipt1):
        print("  Mint ->", dict(event["args"]))

    print("Events from transfer transaction:")
    for event in nft.events.Transfer().process_receipt(receipt2):
        print("  Transfer ->", dict(event["args"]))


if __name__ == "__main__":
    main()
