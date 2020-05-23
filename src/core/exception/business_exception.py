from src.core.exception.application_exception import ApplicationException


class BusinessApplicationException(ApplicationException):
    def __init__(self, error_code: int) -> None:
        super().__init__(error_code)
