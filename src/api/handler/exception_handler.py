import traceback
from fastapi import HTTPException

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from firefly_logger.log_provider import logger
from starlette import status
from starlette.responses import JSONResponse

from src.api.handler.error_response import ErrorResponse
from src.core.exception.application_exception import ApplicationException
from src.infra.util.errors import errors


def http_exception_handler(request, exc: HTTPException):
    error_code = 1999

    # TODO : this case special exception should be thrown
    if status.HTTP_401_UNAUTHORIZED == exc.status_code:
        error_code = 1200

    if status.HTTP_403_FORBIDDEN == exc.status_code:
        error_code = 1201

    logger.error(msg=generate_error_message(error_code),
                 data=generate_stack_trace(exc))

    return JSONResponse(status_code=exc.status_code,
                        content=jsonable_encoder(
                            ErrorResponse(error_code=error_code, error_message=errors[error_code]).dict()))


def validation_exception_handler(request, exc: RequestValidationError):
    error_code = 1000
    logger.error(msg=generate_error_message(error_code), data=generate_stack_trace(exc))
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=jsonable_encoder(ErrorResponse(error_code=error_code, error_detail=exc.errors(),
                                                               error_message=errors[error_code]).dict()))


def application_exception_handler(request, exc: ApplicationException):
    logger.error(msg=generate_error_message(exc.error_code), data=generate_stack_trace(exc))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder(
                            ErrorResponse(error_code=exc.error_code, error_message=exc.error_message).dict()))


def generate_error_message(error_code):
    return "error code: {}, error message: {}".format(error_code, errors[error_code])


def generate_stack_trace(exc: Exception) -> str:
    return "".join(traceback.TracebackException.from_exception(exc).format())
