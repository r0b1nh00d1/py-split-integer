from app.split_integer import split_integer

import pytest


@pytest.mark.parametrize(
    "value, n_p",
    [
        (8, 1),
        (6, 2),
        (17, 4)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, n_p: int
) -> None:
    assert (
        sum(split_integer(value, n_p)) == value
    ), "sum of the parts should be equal to value"


@pytest.mark.parametrize(
    "value, n_p",
    [
        (8, 2),
        (6, 2),
        (16, 4)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, n_p: int
) -> None:
    assert (
        len(set(split_integer(value, n_p))) == 1
    ), "should split into equal parts when value divisible by parts"


@pytest.mark.parametrize(
    "value, n_p",
    [
        (2, 1),
        (5, 1),
        (7, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, n_p: int
) -> None:
    assert (
        split_integer(value, n_p)[0] == value
    ), "should return part equals to value when split into one part"


@pytest.mark.parametrize("value, n_p, expected", [
    (8, 3, [2, 3, 3]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (17, 4, [4, 4, 4, 5])
])
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, n_p: int, expected: list
) -> None:
    assert (
        split_integer(value, n_p) == expected
    ), "parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "value, n_p",
    [
        (3, 5),
        (6, 24),
        (17, 48)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, n_p: int
) -> None:
    assert (
        0 in split_integer(value, n_p)
    ), "should add zeros when value is less than number of parts"
