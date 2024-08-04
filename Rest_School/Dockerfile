FROM python:3.10

#SHELL ["/bin/bash", "-c"]

# set environmeent variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirments.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# http://127.0.0.1:8000/
#RUN pip install --upgradee pip
#
#RUN apt update && apt -qy install gcc libjpeg-dev libxslt-deev \
#    libpq-dev libmariadb-dev libmariadb-dev-compat getteext cron openssh-client flake8 locales vim

#FROM node:latest
#WORKDIR /usr/src/app
#COPY package.json .
#RUN npm install
#COPY . ./
#EXPOSE 3000
#CMD [ "npm", "start" ]