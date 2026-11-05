
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility

# 1. LETTER GRADE TESTS

def test_letter_grade_s():
    assert letter_grade(95) == "S"


def test_letter_grade_a():
    assert letter_grade(85) == "A"


def test_letter_grade_b():
    assert letter_grade(75) == "B"


def test_letter_grade_c():
    assert letter_grade(65) == "C"


def test_letter_grade_d():
    assert letter_grade(55) == "D"


def test_letter_grade_e():
    assert letter_grade(45) == "E"


def test_letter_grade_f():
    assert letter_grade(30) == "F"


def test_letter_grade_invalid():
    with pytest.raises(ValueError):
        letter_grade(-1)


# 2. FINAL MARKS TESTS

def test_final_marks_invalid():
    with pytest.raises(ValueError):
        final_marks(45, 50, False)


def test_final_marks_without_project():
    assert final_marks(30, 40, False) == 70


def test_final_marks_with_project():
    assert final_marks(30, 40, True) == 75


def test_final_marks_project_cap():
    assert final_marks(40, 60, True) == 100


# 3. EXAM ELIGIBILITY TESTS


def test_exam_blocked_fees_not_paid():
    assert exam_eligibility(80, False, False) == "blocked"


def test_exam_eligible_attendance():
    assert exam_eligibility(80, True, False) == "eligible"


def test_exam_eligible_medical():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_detained():
    assert exam_eligibility(60, True, False) == "detained"
