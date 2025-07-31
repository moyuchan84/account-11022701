from account import Account

def test_account():
    sut = Account(10000)
    assert sut is not None


def test_account_init_10000_won():
    account = Account(10000)
    ret = account._balance
    assert ret == 10000