from services.university.models.grade_request import GradeRequest


class TestGradeGetStat:
    @staticmethod
    def _create_grade(student, teacher, university_service, grade_value):
        grade = GradeRequest(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade_value
        )
        university_service.create_grade(grade_request=grade)

    def test_get_stat_by_student_id(self, student_factory, teacher, new_grade_value, university_service):
        students = [student_factory() for _ in range(2)]
        for s in students:
            grade_value = new_grade_value
            self._create_grade(s, teacher, university_service, grade_value)

        grade_stat_response = university_service.get_grades_stats(student_id=students[0].id)
        expected_count = 1

        assert grade_stat_response.count == expected_count, (
            f"Wrong student_id count. Actual result: {grade_stat_response.count}\n"
            f"Expected result: {expected_count}\n"
        )

    def test_get_stat_by_teacher_id(self, teacher_factory, student, new_grade_value, university_service):
        teachers = [teacher_factory() for _ in range(2)]
        for t in teachers:
            grade_value = new_grade_value
            self._create_grade(student, t, university_service, grade_value)

        grade_stat_response = university_service.get_grades_stats(teacher_id=teachers[0].id)
        expected_count = 1

        assert grade_stat_response.count == expected_count, (
            f"Wrong teacher_id count. Actual result: {grade_stat_response.count}\n"
            f"Expected result: {expected_count}\n"
        )
