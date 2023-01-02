

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```



<br />

Setup API KEY 

follow this path 
 ############## apps/config.py  ################


# https://beta.openai.com/account/api-keys
OPENAI_API_KEY = ''# Open ai key


# Email UserID & APP Password(otp code)
# https://myaccount.google.com/u/1/security
EMAIL_ID = " " #UserID
EMAIL_APP_PASSWORD =" " #APP Password

# GOOGLE CLIENT ID (google login)
# https://console.cloud.google.com/apis/credentials?authuser=1&project=esoteric-pad-334905
GOOGLE_CLIENT_ID = " " # CLIENT ID 

# stripe payment gateway API key
# https://dashboard.stripe.com/login
PAYMENT_API_KEY = ' ' # stripe API key




<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 




<br />


### Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />



# WritingApp
