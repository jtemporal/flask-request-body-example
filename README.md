# How to pass data inside the request body example with Flask

## Configure your environment

```console
python3 -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Run the flask app (development server)

```console
export FLASK_APP=application/app.py
flask run
```

## Making the requests

In a new terminal window, navigate to the project directory and run the following:

```console
source .env/bin/activate
python make_rquests.py
```