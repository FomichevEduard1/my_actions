class TestGradeDelete:
    def test_delete_grade(self, grade, university_service):
        university_service.delete_grade(grade_id=grade.id)
        grades_response = university_service.get_grade()

        assert grade.id not in [g.id for g in grades_response], (
            f"Grade with id '{grade.id}' found in response"
        )
