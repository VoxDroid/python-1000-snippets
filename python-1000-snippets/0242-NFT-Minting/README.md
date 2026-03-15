# NFT Minting

## Description
This snippet demonstrates deploying a minimal ERC-721 style NFT contract and minting an NFT on a local in-memory Ethereum chain using `web3`, `eth-tester`, and `py-solc-x`.

## Code
```python
# Requires: pip install web3 eth-tester py-solc-x
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import install_solc, set_solc_version, compile_source

# Minimal ERC-721 contract (not full standard, for demo purposes)
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

# Compile contract
install_solc('0.8.20')
set_solc_version('0.8.20')
compiled = compile_source(CONTRACT_SOURCE, output_values=["abi", "bin"])
contract_interface = compiled['<stdin>:SimpleNFT']

w3 = Web3(EthereumTesterProvider())

contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Deploy contract
acct = w3.eth.accounts[0]
tx_hash = contract.constructor('ExampleNFT', 'ENFT').transact({'from': acct})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

nft = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])

# Mint an NFT
nft.functions.mint(acct, 1, 'https://example.com/nft/1').transact({'from': acct})
print('Owner of token 1:', nft.functions.ownerOf(1).call())
print('Token URI:', nft.functions.tokenURI(1).call())
```

## Output
```
Owner of token 1: 0x...
Token URI: https://example.com/nft/1
```

## Explanation
- **NFT Minting**: Compiles a small NFT contract, deploys it to a local in-memory Ethereum chain, and mints an NFT.
- **Logic**: Uses `eth-tester` for a local chain, `web3` to deploy/interact with the contract, and `py-solc-x` to compile Solidity.
- **Use Case**: Useful for local testing of NFT smart contract logic without an external node.
- **Best Practice**: Use proper ERC-721 implementation (OpenZeppelin) for production; validate inputs and guard against reentrancy.
