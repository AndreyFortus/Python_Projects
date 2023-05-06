from lab_5.task_5_1 import sum_series


def test_sum():
    input_param = 1
    actual = sum_series(input_param)
    expected = 3.4999
    assert actual == expected
