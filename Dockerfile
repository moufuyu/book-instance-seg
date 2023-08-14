FROM python:3.11
# install python package
COPY pyproject.toml ./
RUN apt update \
    && apt install --no-install-recommends -y python3-pip git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg g++ libusb-1.0-0
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

WORKDIR /home/book_detection_app
# expose port
EXPOSE 8888