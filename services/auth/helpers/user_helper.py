from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    ENDPOINT_PREFIX = "/users"

    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me"

    def get_me(self):
        response = self.api_utils.post(self.ME_ENDPOINT)
        return response
