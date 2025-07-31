from account import Account

def test_account():
    sut = Account(10000)
    assert sut is not None


def test_account_init_10000_won():
    account = Account(10000)
    ret = account._balance
    assert ret == 10000


def test_deposit_and_confirmation():
    account = Account(10000)
    account.deposit(500)
    assert account._balance == 10500