from brownie import FundMe, network, MockV3Aggregator, config
from scripts.utils import get_account, LOCAL_BLOACKCHAIN_ENVIROMENTS
from web3 import Web3


def deploy():
    account = get_account()
    # pass the price feed address for contract
    # if we are on rinkeby then use associated address otherwise deploy mocks

    if network.show_active() not in LOCAL_BLOACKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(8, 2000000000000000000, {"from": account})
        price_feed_address = MockV3Aggregator[-1].address
        print(f"deployed from {network.show_active()}")
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(account)

    print("fundme", fund_me.address)


def main():
    deploy()
