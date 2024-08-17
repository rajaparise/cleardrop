from rest_framework.exceptions import APIException

class MissingParamException(APIException):
    status_code = 400
    default_detail = 'Request does not have required parameter(s).'
    default_code = 'no_param'

class InvalidParamException(APIException):
    status_code = 400
    default_detail = 'Your request contain invalid parameter'
    default_code = 'invalid_param'

class NoValidDataException(APIException):
    # def __init__(self, message):
    #    self.message = message
    
    status_code = 400
    default_detail = 'No Valid data found for the given '
    default_code = 'invalid_data'

class ShowUserDefinedException(APIException):
    status_code = 400
    default_detail = ''
    default_code = 'invalid_data'

    def __init__(self, message):
       self.message = message

    def throw_message(self):
        self.default_detail = self.message

    # status_code = 400
    # default_detail = message
    # default_code = 'invalid_data'

class ValidService(APIException):
    status_code = 200
    default_detail = 'Success'
    default_code = 'valid_service'