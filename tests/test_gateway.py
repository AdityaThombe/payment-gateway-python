import json

from gateway import accounts, client, orders


def test_search_returns_only_matching_customer():
    conn = orders.connect()
    orders.add_order(conn, "acme", "alice", 1200)
    orders.add_order(conn, "acme", "bob", 800)
    rows = orders.search_orders(conn, "acme", "alice")
    assert [(r[1], r[2]) for r in rows] == [("alice", 1200)]


def test_search_is_scoped_to_merchant():
    conn = orders.connect()
    orders.add_order(conn, "acme", "alice", 1200)
    orders.add_order(conn, "globex", "alice", 500)
    assert len(orders.search_orders(conn, "globex", "alice")) == 1


def test_total_for_merchant():
    conn = orders.connect()
    orders.add_order(conn, "acme", "alice", 1200)
    orders.add_order(conn, "acme", "bob", 800)
    assert orders.total_for(conn, "acme") == 2000
    assert orders.total_for(conn, "nobody") == 0


def test_login_accepts_correct_password_only():
    store = {}
    accounts.create_account(store, "acme", "correct horse battery staple")
    assert accounts.login(store, "acme", "correct horse battery staple")
    assert not accounts.login(store, "acme", "wrong")
    assert not accounts.login(store, "unknown", "correct horse battery staple")


def test_duplicate_account_rejected():
    store = {}
    accounts.create_account(store, "acme", "pw-one-1234")
    try:
        accounts.create_account(store, "acme", "pw-two-1234")
    except ValueError:
        return
    raise AssertionError("duplicate merchant accepted")


def test_charge_request_is_signed():
    req = client.signed_charge(42, 1999)
    assert req["url"].endswith("/charges")
    assert json.loads(req["body"]) == {"amount": 1999, "currency": "EUR", "order": 42}
    assert len(req["signature"]) == 64
