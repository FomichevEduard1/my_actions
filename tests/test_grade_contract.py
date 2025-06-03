import requests

from services.university.helpers.grade_helper import GradeHelper


class TestGradeContract:
    def test_create_grade_anonym(self, student, teacher, new_grade_value, university_api_utils_anonym):
        grade_helper = GradeHelper(api_utils=university_api_utils_anonym)
        response = grade_helper.post_grade({
            "teacher_id": student.id,
            "grade": new_grade_value
        })

        assert response.status_code == requests.status_codes.codes.unauthorized, (
            f"Wrong status code. Actual result: {response.status_code}\n"
            f"Expected result: {requests.status_codes.codes.unauthorized}\n"
        )

    def test_student_not_found(self, teacher, new_grade_value, university_api_utils_admin):
        grade_helper = GradeHelper(api_utils=university_api_utils_admin)
        response = grade_helper.post_grade({
            "teacher_id": teacher.id,
            "grade": new_grade_value
        })

        assert response.status_code == requests.status_codes.codes.not_found, (
            f"Wrong status code. Actual result: {response.status_code}\n"
            f"Expected result: {requests.status_codes.codes.not_found}\n"
        )
