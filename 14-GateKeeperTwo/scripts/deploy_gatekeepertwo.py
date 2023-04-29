from brownie import accounts, AttackGateKeeperTwo, config


def main():
    contract = '0xA9a0252f488a4778Aa30a67C78D430C59b2ef849'
    hacker = accounts.add(config['wallets']['from_key'])

    AttackGateKeeperTwo.deploy(contract, {'from': hacker,"gas_limit":12000000})
    