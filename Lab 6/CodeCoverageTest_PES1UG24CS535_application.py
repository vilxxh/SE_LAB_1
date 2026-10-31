import pytest

from warranty_claims import out_of_warranty_charge, claim_allowed, sla_status


# ==========================================
# OUT OF WARRANTY CHARGE TESTS
# ==========================================

def test_unknown_plan():
    with pytest.raises(ValueError):
        out_of_warranty_charge("gold", 20, "defect", False)


def test_invalid_age():
    with pytest.raises(ValueError):
        out_of_warranty_charge("standard", -5, "defect", False)


def test_within_warranty():
    assert out_of_warranty_charge("standard", 20, "defect", False) == 0


def test_registered_customer():
    assert out_of_warranty_charge("standard", 31, "defect", True) == 100


def test_premium_registered():
    assert out_of_warranty_charge("premium", 37, "defect", True) == 100


def test_accidental_claim():
    assert out_of_warranty_charge("basic", 13, "accidental", False) == 200


def test_defect_claim():
    assert out_of_warranty_charge("basic", 13, "defect", False) == 100


def test_excess_above_12_accidental():
    assert out_of_warranty_charge("basic", 25, "accidental", False) == 3575


def test_excess_above_12_defect():
    assert out_of_warranty_charge("basic", 25, "defect", False) == 1950


# ==========================================
# CLAIM ELIGIBILITY TESTS
# ==========================================

def test_recall_claim_allowed():
    assert claim_allowed(10, 5, True) is True


def test_recall_claim_rejected():
    assert claim_allowed(10, 6, True) is False


def test_recent_claim_rejected():
    assert claim_allowed(15, 1, False) is False


def test_normal_claim_allowed():
    assert claim_allowed(30, 2, False) is True


def test_normal_claim_limit_exceeded():
    assert claim_allowed(45, 3, False) is False


# ==========================================
# SLA STATUS TESTS
# ==========================================

def test_hardware_on_track():
    assert sla_status(48, True, False) == "on_track"


def test_software_on_track():
    assert sla_status(24, False, False) == "on_track"


def test_priority_on_track():
    assert sla_status(48, False, True) == "on_track"


def test_at_risk_status():
    assert sla_status(15, False, False) == "at_risk"


def test_critical_status():
    assert sla_status(10, False, False) == "critical"