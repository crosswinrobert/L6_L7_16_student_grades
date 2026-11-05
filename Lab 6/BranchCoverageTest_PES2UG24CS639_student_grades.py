
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# 1. LETTER GRADE - BRANCH TESTS


def test_letter_grade_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_letter_grade_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_letter_grade_s():
    assert letter_grade(90) == "S"


def test_letter_grade_a():
    assert letter_grade(80) == "A"


def test_letter_grade_b():
    assert letter_grade(70) == "B"


def test_letter_grade_c():
    assert letter_grade(60) == "C"


def test_letter_grade_d():
    assert letter_grade(50) == "D"


def test_letter_grade_e():
    assert letter_grade(40) == "E"


def test_letter_grade_f():
    assert letter_grade(39) == "F"


# 2. FINAL MARKS - BRANCH TESTS


def test_final_marks_internal_above_limit():
    with pytest.raises(ValueError):
        final_marks(41, 30, False)


def test_final_marks_external_above_limit():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_final_marks_without_project():
    assert final_marks(30, 40, False) == 70


def test_final_marks_with_project_below_100():
    assert final_marks(30, 40, True) == 75


def test_final_marks_project_total_above_100():
    assert final_marks(40, 60, True) == 100


# -------------------------------------------------
# 3. EXAM ELIGIBILITY - BRANCH TESTS
# -------------------------------------------------

def test_exam_blocked_when_fees_not_paid():
    assert exam_eligibility(80, False, False) == "blocked"


def test_exam_eligible_attendance_75_or_above():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligible_with_medical_exception():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_detained_without_medical_exception():
    assert exam_eligibility(70, True, False) == "detained"


def test_exam_detained_low_attendance():
    assert exam_eligibility(60, True, True) == "detained"
