FROM python:3.10-slim
ADD . /usr/src/app/
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app
COPY . /usr/src/app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python","manage.py" ]
CMD [ "runserver","0.0.0.0:8000" ]
 