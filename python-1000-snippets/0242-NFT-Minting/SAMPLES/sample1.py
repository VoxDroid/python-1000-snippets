# sample1.py
# Deploy a minimal NFT contract and mint a token.

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

    function ownerOf(uint256 tokenId) public view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Not minted");
        return owner;
    }

    function tokenURI(uint256 tokenId) public view returns (string memory) {
        require(_owners[tokenId] != address(0), "Not minted");
        return _tokenURIs[tokenId];
    }
}
"""


def compile_contract():
    install_solc("0.8.20")
    set_solc_version("0.8.20")
    compiled = compile_source(CONTRACT_SOURCE, output_values=["abi", "bin"])
    return compiled["<stdin>:SimpleNFT"]


def deploy_contract(w3, abi, bytecode):
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor("ExampleNFT", "ENFT").transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.eth.contract(address=receipt.contractAddress, abi=abi)


def main():
    w3 = Web3(EthereumTesterProvider())

    contract_data = compile_contract()
    nft = deploy_contract(w3, contract_data["abi"], contract_data["bin"])

    account = w3.eth.accounts[0]
    nft.functions.mint(account, 1, "https://example.com/nft/1").transact({"from": account})

    print("Owner of token 1:", nft.functions.ownerOf(1).call())
    print("Token URI:", nft.functions.tokenURI(1).call())


if __name__ == "__main__":
    main()
