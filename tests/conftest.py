import random
import time

import pytest
import requests

from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_grade import BaseGrade
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker

faker = Faker()


@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 30
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            Logger.info(f"Service not ready yet: {e}")
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.")


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_service_anonym(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    return auth_service


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_service_anonym):
    username = faker.user_name()
    password = faker.password(
        length=15,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True)
    auth_service_anonym.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()
        )
    )
    login_response = auth_service_anonym.login_user(login_request=LoginRequest(username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_service(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    return university_service


@pytest.fixture(scope="function", autouse=False)
def teacher(university_service):
    teacher = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice(list(SubjectEnum))
    )
    return university_service.create_teacher(teacher_request=teacher)


@pytest.fixture(scope="function", autouse=False)
def teacher_factory(university_service):
    def _create_teacher():
        teacher = TeacherRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            subject=random.choice(list(SubjectEnum))
        )
        return university_service.create_teacher(teacher_request=teacher)

    return _create_teacher


@pytest.fixture(scope="function", autouse=False)
def group(university_service):
    group = GroupRequest(name=faker.name())
    return university_service.create_group(group_request=group)


@pytest.fixture(scope="function", autouse=False)
def student(university_service, group):
    student = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=random.choice(list(DegreeEnum)),
        phone=faker.numerify("+7##########"),
        group_id=group.id
    )
    return university_service.create_student(student_request=student)


@pytest.fixture(scope="function", autouse=False)
def student_factory(university_service, group):
    def _create_student():
        student = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice(list(DegreeEnum)),
            phone=faker.numerify("+7##########"),
            group_id=group.id
        )
        return university_service.create_student(student_request=student)

    return _create_student


@pytest.fixture(scope="function", autouse=False)
def grade(university_service, student, teacher):
    grade = GradeRequest(
        teacher_id=teacher.id,
        student_id=student.id,
        grade=random.randint(1, 5)
    )
    return university_service.create_grade(grade_request=grade)


@pytest.fixture(scope="function", autouse=False)
def new_grade_value():
    return random.randint(BaseGrade.MIN_GRADE, BaseGrade.MAX_GRADE)
