from lab_5.task_5_3 import square_root


def test_square():
    input_param = 81
    actual = square_root(input_param)
    expected = 9
    assert actual == expected
