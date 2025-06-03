from services.general.base_service import BaseService
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_response import GradeResponse
from services.university.models.grade_stat_response import GradeStatResponse
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from services.university.models.teacher_request import TeacherRequest
from services.university.models.teacher_response import TeacherResponse
from utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest):
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest):
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest):
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest):
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def get_grade(self):
        response = self.grade_helper.get_grade()
        grades = [GradeResponse(**item) for item in response.json()]
        return grades

    def put_grade(self, grade_id: int, grade_request: GradeRequest):
        response = self.grade_helper.put_grade(grade_id=grade_id, data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def delete_grade(self, grade_id: int):
        response = self.grade_helper.delete_grade(grade_id=grade_id)
        return response

    def get_grades_stats(self, student_id=None, teacher_id=None, group_id=None):
        params = {}
        if student_id:
            params["student_id"] = student_id
        if teacher_id:
            params["teacher_id"] = teacher_id
        if group_id:
            params["group_id"] = group_id
        response = self.grade_helper.get_grades_stats(params=params)
        return GradeStatResponse(**response.json())
