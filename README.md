## Setup fastapi-vue-mongo

##### Requirements
* Python 3
* Pip 3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:
```bash
$ cd fastapi-vue-mongo
$ virtualenv -p python3 .venv
```

Activate the virtualenv:
```bash
$ source .venv/bin/activate
```

Install Requirements:
```bash
$ pip install -r requirements.txt
```

Configure the location of your MongoDB database:
```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"
export MONGODB_DB="<db>"
```

Run the development environment:
```bash
$ uvicorn app:app --reload
```

Deactivate the virtualenv:
```bash
$ deactivate
```