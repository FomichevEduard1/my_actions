from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = "/teachers"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_teacher(self, json: dict):
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response
