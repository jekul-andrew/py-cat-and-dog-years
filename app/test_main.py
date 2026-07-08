import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expect_list",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Check with zero parameters"),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test with first boundary parameter"

            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Different human ages for equal cat/dog ages"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Big ages for cat/dog"
            )
        ]
    )
    def test_modify_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expect_list: list[int]
    ) -> None:

        assert get_human_age(cat_age, dog_age) == expect_list

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "",
                "-",
                TypeError,
                id="Raise TypeError if params are strings"
            ),
            pytest.param(
                2,
                -2,
                ValueError,
                id="Raise ValueError if age is negative number"
            ),
        ]
    )
    def test_raise_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[TypeError | ValueError]
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
