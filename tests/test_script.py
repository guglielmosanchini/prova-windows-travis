from script import sum_list


def test_sum_list():
    l1 = [1, 2]
    l2 = [3, 4]

    assert sum_list(l1, l2) == [1, 2, 3, 4]
