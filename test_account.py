from account import Account

def test_account():
    sut = Account()
    assert sut is not None


def test_account_init_10000_won():
    account = Account()
    ret = account._balance
    assert ret == 10000