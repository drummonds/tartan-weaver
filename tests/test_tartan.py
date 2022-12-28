from tartan_weaver import Tartan


def test_threadcount():
    test = "R14 DB2 R4"
    a = Tartan.from_space_threadcount(test)
    assert test == f"{a}"
    assert 20 == a.threadcount
