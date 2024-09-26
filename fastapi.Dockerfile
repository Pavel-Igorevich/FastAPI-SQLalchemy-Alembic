FROM python:3.12-alpine AS base

RUN apk --no-cache add git
RUN git clone https://github.com/Pavel-Igorevich/FastAPI-SQLalchemy-Alembic.git
WORKDIR FastAPI-SQLalchemy-Alembic
RUN git checkout dev
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
# RUN alembic upgrade head

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]