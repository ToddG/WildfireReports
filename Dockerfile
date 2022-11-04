FROM python:3.9
ENV PYTHONUNBUFFERED 1  
RUN mkdir /config  
ADD /config/requirements.txt /config/
RUN python -m pip install --upgrade pip
RUN pip install -r /config/requirements.txt  
RUN mkdir /src;
WORKDIR /src
