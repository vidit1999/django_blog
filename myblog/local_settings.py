import os, json
from django.core.exceptions import ImproperlyConfigured

try:
	with open(os.environ['SECRET_TOKENS']) as f:
	    secret_tokens = json.load(f)
except KeyError:
	raise ImproperlyConfigured("Environment variable not set properly.")
except FileNotFoundError:
	raise ImproperlyConfigured("Secrets file not found at specified location.")

def get_token(variable, secret_tokens = secret_tokens):
	try:
		val = secret_tokens[variable]
		return val
	except KeyError:
		raise ImproperlyConfigured(f"Set {variable} variable in secret_tokens.json.")

ADMIN_URL = get_token('ADMIN_URL')
LOGIN_URL = get_token('LOGIN_URL')
SIGNIN_URL = get_token('SIGNIN_URL')
LOGOUT_URL = get_token('LOGOUT_URL')
BLOG_CREATE = get_token('BLOG_CREATE')
BLOG_CHANGE = get_token('BLOG_CHANGE')
BLOG_DELETE = get_token('BLOG_DELETE')
SECRET_KEY = get_token('SECRET_KEY')
TIME_ZONE = get_token('TIME_ZONE')
DEBUG = get_token('DEBUG')