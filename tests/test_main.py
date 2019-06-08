from compare import Any, List, String, Dict


def test_main():
    assert 5 == Any()
    assert not 5 == Any(type=str)
    assert 'aa' == Any(type=str)

    assert [
        {'name': 'Andrew', 'id': 7},
        {'name': 'Boris', 'id': 2},
        {'name': 'Grigoriy', 'id': 8},
    ] == List(
        [
            {'name': 'Boris', 'id': 2},
            {'name': 'Grigoriy', 'id': 8},
            {'name': 'Andrew', 'id': 7},
        ],
        cmp_key=lambda x: x['id']
    )
    assert not [
        {'name': 'Andrew', 'id': 7},
        {'name': 'Boris', 'id': 2},
        {'name': 'Grigoriy', 'id': 8},
    ] == List(
        [
            {'name': 'Boris', 'id': 0},
            {'name': 'Grigoriy', 'id': 8},
            {'name': 'Andrew', 'id': 7},
        ],
        cmp_key=lambda x: x['id']
    )

    assert "a452345b" == String(regexp=r'^a\d+b$')
    assert not "a452b345b" == String(regexp=r'^a\d+b$')

    sample_dict = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
    }
    assert sample_dict == Dict(
        {'first': 1, 'third': 3}
    )
    assert not sample_dict == Dict(
        {'first': 1, 'third': 4}
    )


def test_list_compare():
    # assert [1, 2, 3] == [1, 2]
    assert [
        3, 1, 2
    ] == List([1, 2, ], cmp_key=lambda x: x)
