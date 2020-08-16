def lowercase(x):
    return x.lower()

def test_lowercase():
    assert lowercase("TEAM KAIZEND") == "team kaizend"

def test_lowercase2():
    assert lowercase("Team Kaizend") == "team kaizend"
