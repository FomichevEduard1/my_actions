import random

from faker import Faker

from services.university.models.base_student import DegreeEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.student_request import StudentRequest

faker = Faker()


class TestGradePut:
    def test_put_grade(self, grade, teacher, new_grade_value, university_service):
        grade_r = GradeRequest(
            teacher_id=teacher.id,
            student_id=grade.student_id,
            grade=new_grade_value
        )
        grade_response = university_service.put_grade(grade_id=grade.id, grade_request=grade_r)

        assert grade_response.grade == new_grade_value, (
            f"Wrong grade. Actual result: {grade_response.grade}\n"
            f"Expected result: {new_grade_value}\n"
        )

    def test_put_student_id(self, grade, teacher, group, university_service):
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice(list(DegreeEnum)),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group.id)
        student_response = university_service.create_student(student_request=student)
        grade_r = GradeRequest(
            teacher_id=teacher.id,
            student_id=student_response.id,
            grade=grade.grade
        )
        grade_response = university_service.put_grade(grade_id=grade.id, grade_request=grade_r)

        assert grade_response.student_id == student_response.id, (
            f"Wrong grade student id. Actual result: {grade_response.student_id}\n"
            f"Expected result: {student_response.id}\n"
        )
