from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STAT_ENDPOINT = f"{ENDPOINT_PREFIX}/stats"

    def post_grade(self, data: dict):
        response = self.api_utils.post(self.ROOT_ENDPOINT, data)
        return response

    def get_grade(self):
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def put_grade(self, grade_id: int, data: dict):
        response = self.api_utils.put(f"{self.ROOT_ENDPOINT}{grade_id}", data)
        return response

    def delete_grade(self, grade_id: int):
        response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{grade_id}")
        return response

    def get_grades_stats(self, params: dict):
        response = self.api_utils.get(self.STAT_ENDPOINT, params=params)
        return response
