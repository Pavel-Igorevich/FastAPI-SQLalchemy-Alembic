from fastapi import HTTPException, status


class FileException(HTTPException):

    @staticmethod
    def invalid_format():
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail="File is not allowed")

    @staticmethod
    def processing_failed():
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Processing failed")

    @staticmethod
    def success_upload(file_name):
        return HTTPException(status.HTTP_200_OK, detail=f"File: {file_name} was successfully uploaded")
