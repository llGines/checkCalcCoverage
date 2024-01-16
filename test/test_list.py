import pytest
import learn_testing.mymates.list_mates as list_mates
import learn_testing.mymates.exception_list as El

# Giving a vocal as paramter, how many of the given vocal
# are in the list? Lower and upper case must be counted together
# NotInListError error must raise if what is passed is not a vocal


@pytest.mark.parametrize(
    "a,r",
    [
        ("a", 11),
        ("e", 6),
    ],
)
def test_count_vocals_happy_path(a, r):
    assert list_mates.count_vocals(a) == r


@pytest.mark.parametrize(
    "a,e",
    [
        ("n", El.NotInListError),
    ],
)
def test_count_vocals_sad_path(a, e):
    pytest.raises(e, list_mates.count_vocals, a)


# Given a letter, return all the names wich contain it.
# NotInListError must raise if there is no name with this letter


@pytest.mark.parametrize(
    "a,r",
    [
        ("m", ["Maria", "Mikel", "Thomas"]),
        ("v", ["David", "Vicente"]),
    ],
)
def test_return_names_happy_path(a, r):
    assert list_mates.return_names(a) == r


@pytest.mark.parametrize(
    "a,e",
    [
        ("x", El.NotInListError),
    ],
)
def test_return_names_sad_path(a, e):
    pytest.raises(e, list_mates.count_vocals, a)
