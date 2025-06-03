from faker import Faker

from services.university.models.grade_request import GradeRequest

faker = Faker()


class TestGradeCreate:
    def test_grade_create(self, student, teacher, new_grade_value, university_service):
        grade = GradeRequest(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=new_grade_value
        )
        grade_response = university_service.create_grade(grade_request=grade)

        assert grade_response.teacher_id == teacher.id, (
            f"Wrong grade teacher id. Actual result: {grade_response.teacher_id}\n"
            f"Expected result: {teacher.id}\n"
        )
