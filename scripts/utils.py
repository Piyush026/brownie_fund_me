from brownie import network, accounts, config

# 5:42:00 for ganache-new-local in video

FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork-dev"]
LOCAL_BLOACKCHAIN_ENVIROMENTS = ["development", "ganache-local", "ganache-new-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOACKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
