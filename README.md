# Image Repository
Image repository app for shopify's internship application.

## Installation

> If you don't have Python installed, install it from the offical store.

Clone the repository first:

```
$ git clone https://github.com/Youngestdev/image-repository.git
$ cd image-repository
```

### Configuring the application

Create and initialise a virtual environment:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the application dependencies next:

```
(venv)$ pip install -r requirements.txt
```

Configure your environment values:

```
(venv)$ mv .env.sample .env
```

Edit the `.env` file to suit your taste.

### Running the application

Run your application with the command:

```
(vevn)$ python3 main.py
```

A similar response like the one below is displayed in your terminal:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [6849] using statreload
INFO:     Started server process [6851]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Navigate to http://0.0.0.0/docs to use the interactive documentation page to test the API routes.

## Testing

Start by registering a new user then logging in to get an authorisation token to enable you have access to protected routes.
