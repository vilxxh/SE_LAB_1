
from hypothesis import given, strategies as st
from warranty_claims import parse_claim, age_average, payable_charge
import math


@given(
    plan=st.text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=1),
    months=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False)
)
def test_parse_claim_valid(plan, months):
    result = parse_claim(f"{plan}:{months}")
    assert result == (plan.title(), months)


# Check that malformed claim formats are rejected
@given(s=st.text().filter(lambda s: s.count(":") != 1))
def test_parse_claim_invalid_format(s):
    try:
        parse_claim(s)
    except ValueError:
        return
    assert False, "Invalid claim format was accepted"



@given(ages=st.lists(st.integers(min_value=0, max_value=100000), min_size=1))
def test_age_average_valid(ages):
    csv_input = ",".join(str(age) for age in ages)
    expected = sum(ages) // len(ages)
    assert age_average(csv_input) == expected


# Check that invalid CSV inputs are rejected
@given(s=st.sampled_from(["", "abc", "12,,24", "12,abc,36", ",12", "12,"]))
def test_age_average_invalid(s):
    try:
        age_average(s)
    except ValueError:
        return
    assert False, "Invalid age input was accepted"



@given(
    charge=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False),
    discount=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False)
)
def test_payable_charge_valid(charge, discount):
    result = payable_charge(f"{charge}|{discount}")
    expected = max(charge * 1.18 - discount, 0)
    assert math.isclose(result, expected, rel_tol=1e-9)


# Check that malformed charge inputs are rejected
@given(s=st.sampled_from(["", "1500", "abc|200", "1500|abc", "|200", "1500|", "1|2|3"]))
def test_payable_charge_invalid(s):
    try:
        payable_charge(s)
    except ValueError:
        return
    assert False, "Invalid charge input was accepted"
