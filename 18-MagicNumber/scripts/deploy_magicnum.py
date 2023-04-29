from brownie import accounts, config, AttackMagicNum


def main():
    contract = '0x6F7e52ec3b67CBED4388192861144125734FB2687'
    hacker = accounts.add(config['wallets']['from_key'])
    attack_contract = AttackMagicNum.deploy(contract, {'from': hacker})