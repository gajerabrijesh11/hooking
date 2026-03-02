

def test_a(db_connection):
    db_connection["val"] = 42
    assert db_connection["val"] == 42

def test_b(db_connection):
    assert isinstance(db_connection, dict)