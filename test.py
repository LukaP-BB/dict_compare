from dict_diff import diff

def test_function() :
    ref_diff = {'c': {'dict1': 10, 'dict2': 5},
                'f': {'dict2': {'h': {'to', 'bla', 'ka'}},
                      'i': {'dict1': 'j', 'dict2': {'foo', 'bla'}},
                      'k': {'dict1': {'o'}},
                      'set': {'index_0': {'index_2': {'dict1': 'c', 'dict2': 'd'},
                                          'supp_elmts': {'dict2': ['d']}},
                              'index_1': {'index_2': {'dict1': 'd', 'dict2': 'a'}},
                              'index_2': {'supp_elmts': {'dict1': ['f']}},
                              'supp_elmts': {'dict1': [['bla']]}}}}

    l1 = [("a", "b", "c", "d"),("a", "b", "d"),("a", "b", "e")]

    l2 = [("a", "b", "d"),("a", "b", "a"),("a", "b", "e", "f"),["bla"]]

    d1 = {"a": "b","c": 10,
        "f": {"g": "h","i": "j",
            "k": {"l", "m", "n", "o"},
            "set": l1
        },
    }

    d2 = {"a": "b","c": 5,"f": {"g": "h",
            "i": {"bla", "foo"},
            "k": {"l", "m", "n"},
            "set": l2,
            "h": {"bla", "ka", 'to'}
        },
    }

    assert diff(d1, d2) == ref_diff