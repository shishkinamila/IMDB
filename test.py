from imdb import DataBase


def test_set_null():
    db = DataBase()
    db.set_value("A", "NULL")
    assert db.get("A") == "NULL"


def test_set():
    db = DataBase()
    db.set_value("A", 10)
    assert db.get("A") == 10


def test_get_null():
    db = DataBase()
    db.set_value("A", "NULL")
    assert db.get("A") == "NULL"


def test_get():
    db = DataBase()
    db.set_value("A", 5)
    assert db.get("A") == 5


def test_fail_get():
    db = DataBase()
    db.set_value("A", 6)
    assert db.get("A") != 5


def test_counts():
    db = DataBase()
    db.set_value("A", 10)
    db.set_value("B", 10)
    db.set_value("C", 10)
    assert db.counts(10) == 3


def test_fail_counts():
    db = DataBase()
    db.set_value("A", 10)
    db.set_value("B", 10)
    db.set_value("C", 10)
    countsA = db.counts(5)
    assert countsA == 0


def test_commit():
    db = DataBase()
    db.set_value("A", 10)
    db.begin()
    db.set_value("A", 20)
    assert db.get("A") == 20
    db.commit()
    assert db.get("A") == 20


def test_from_task1():
    db = DataBase()
    db.set_value("A", "NULL")
    assert db.get("A") == "NULL"
    db.set_value("A", 10)
    assert db.get("A") == 10
    assert db.counts(10) == 1
    db.set_value("B", 20)
    db.set_value("C", 10)
    assert db.counts(10) == 2
    db.unset("B")
    db.set_value("B", "NULL")
    assert db.get("B") == "NULL"


def test_from_task2():
    db = DataBase()
    db.begin()
    db.set_value("A", 10)
    db.begin()
    db.set_value("A", 20)
    db.set_value("A", 30)
    db.get("A")
    assert db.get("A") == 30
    db.rollback()
    db.get("A")
    assert db.get("A") == 10
    db.commit()
    db.get("A")
    assert db.get("A") == 10
