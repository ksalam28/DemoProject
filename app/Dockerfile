FROM python:3.7.2

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
