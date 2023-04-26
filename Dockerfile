FROM python:3.8.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./main.py /code/
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"] 

