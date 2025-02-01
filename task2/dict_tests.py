from dict_list import AssociativeArray

def test_insert():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert str(a) == "{1: 10, 3: 30, 4: 40, 5: 50, 6: 60}"
    
def test_get():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert a[1] == 10
    assert a[3] == 30
    assert a[4] == 40
    assert a[5] == 50
    assert a[6] == 60
    
def test_delete():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    del a[3]
    del a[5]
    assert str(a) == "{1: 10, 4: 40, 6: 60}"
    
def test_len():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert len(a) == 5
    
def test_contains():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert 1 in a
    assert 3 in a
    assert 4 in a
    assert 5 in a
    assert 6 in a
    assert 2 not in a
    assert 7 not in a
    
def test_iter():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert list(iter(a)) == [1, 3, 4, 5, 6]

def test_items():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert list(a.items()) == [(1, 10), (3, 30), (4, 40), (5, 50), (6, 60)]
    
def test_keys():
    a = AssociativeArray()
    a[1] = 10
    a[3] = 30
    a[4] = 40
    a[5] = 50
    a[6] = 60
    assert list(a.keys()) == [1, 3, 4, 5, 6]
    
def test_resize():
    a = AssociativeArray()
    for i in range(1000):
        a[i] = i
    assert len(a) == 1000
    for i in range(1000):
        assert a[i] == i
    for i in range(1000):
        del a[i]
    assert len(a) == 0
    for i in range(1000):
        assert i not in a
    assert a.map.capacity == 2048
    
