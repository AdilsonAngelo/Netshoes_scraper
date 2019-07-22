FROM ubuntu:latest
FROM mongo:3.6-xenial
FROM python:3.7.4-buster

ENV PYENV_ROOT="/root/.pyenv" \
	PATH="/root/.pyenv/shims:/root/.pyenv/bin:${PATH}" \
	PIPENV_YES=1 \
	PIPENV_DONT_LOAD_ENV=1 \
	LC_ALL="C.UTF-8" \
	LANG="en_US.UTF-8"

RUN apt-get update
RUN apt-get install -y git mercurial build-essential libssl-dev libbz2-dev zlib1g-dev libffi-dev libreadline-dev libsqlite3-dev curl
# install pyenv
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

ADD . /home/onboarding
COPY . /home/onboarding

RUN pyenv install 3.7.4
RUN pyenv global 3.7.4
RUN pyenv rehash

WORKDIR /home/onboarding
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

RUN mongod --port 27018