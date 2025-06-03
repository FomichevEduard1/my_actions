class TestGradeGet:
    def test_get_grades(self, grade, university_service):
        grade_response = university_service.get_grade()

        assert any(g.teacher_id == grade.teacher_id and g.student_id == grade.student_id
                   for g in grade_response), (
            f"Expected grade '{grade}' not found in response"
        )
