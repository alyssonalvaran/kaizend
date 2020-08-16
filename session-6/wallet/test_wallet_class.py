import pytest
from random import randint

from test_wallet import transaction_params
from wallet import InsufficientAmount, Wallet


class TestWallet:

    def test_default_initial_amount(self):
        wallet = Wallet()
        assert wallet.balance == 0

    # @pytest.mark.smoke
    def test_setting_initial_amount(self):
        wallet = Wallet(100)
        assert wallet.balance == 100

    # @pytest.mark.smoke
    def test_wallet_add_cash(self):
        wallet = Wallet(10)
        wallet.add_cash(90)
        assert wallet.balance == 100

    # @pytest.mark.smoke
    # @pytest.mark.skip(reason="not supported until version 0.0.2")
    # @pytest.mark.xfail()
    def test_wallet_spend_cash(self):
        wallet = Wallet(20)
        wallet.spend_cash(10)
        assert wallet.balance == 10

    # @pytest.mark.skip(reason="not supported until version 0.0.2")
    # @pytest.mark.xfail()
    def test_wallet_spend_cash_raises_exception_on_insufficient_amount(self):
        wallet = Wallet()
        with pytest.raises(InsufficientAmount):
            wallet.spend_cash(100)

    @pytest.mark.parametrize(
        "earned,spent,expected", transaction_params(10)
    )
    def test_transactions(self, earned, spent, expected):
        my_wallet = Wallet()
        my_wallet.add_cash(earned)
        my_wallet.spend_cash(spent)
        assert my_wallet.balance == expected