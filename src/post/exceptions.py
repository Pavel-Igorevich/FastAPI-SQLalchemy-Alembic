from fastapi import HTTPException, status


class PostException(HTTPException):

    @staticmethod
    def invalid_data():
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid data")

    @staticmethod
    def not_found():
        return HTTPException(status.HTTP_404_NOT_FOUND, detail="Post not found")