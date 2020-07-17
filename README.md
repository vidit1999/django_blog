# Code Blog
#### A coding blog site created using **Django**.
#### Write the blog in **Markdown**.
#### Also has code highlighting featutes.

To use it,
* First clone the repositry or download the zip file.
```shell
$:\> git clone https://github.com/vidit1999/django_blog.git
```
* You will have a folder named *django_blog*. Go into that folder.
```shell
$:\> cd django_blog
```
* Activate a Python virtual environment from your terminal.
```shell
$:django_blog\> <your_env_name>\Scripts\activate.bat # for windows
$:django_blog\> source <your_env_name>/bin/activate # for Linux & MacOs
$:django_blog\> conda activate <your_env_name> # for anaconda users
```
* Install required dependencies,
```shell
$:django_blog\> pip install -r requirements.txt
```
* Now Create a file with name *secret_tokens.json*.
```shell
$:django_blog\> touch secret_tokens.json
```
* In the *secret_tokens.json*  file wrtie all necessary secret keys mentioned below,
```json
{
	"SECRET_KEY" : "<your-secret-key>",
	"ADMIN_URL" : "<your-admin-url>",
	"LOGIN_URL" : "<your-login-url>",
	"SIGNIN_URL" : "<your-signin-url",
	"LOGOUT_URL" : "<your-logout-url>",
	"BLOG_CREATE" : "<your-blog-creation-url>",
	"BLOG_CHANGE" : "<your-blog-change-url>",
	"BLOG_DELETE" : "<your-blog-delete-url>",
	"TIME_ZONE" : "<your-time-zone>",
	"DEBUG" : "<your-debug-mode>"
}
```
* Then create a environment variable with name *'SECRET_TOKENS'* and set its value t o the absolute path of *secret_tokens.json*.

So,
Admin site : ***hosturl/your-admin-url***

Login site : ***hosturl/your-login-url***

Signin site : ***hosturl/your-signin-url***

Logout site : ***hosturl/your-logout-url***

Blog Create site : ***hosturl/blog/your-blog-creation-url***

Blog Change site : ***hosturl/blog/your-blog-change-url/blog_id***

Blog Delete site : ***hosturl/your-blog-delete-url/blog_id***

Example,
Contens of file : *secret_tokens.json*
```json
{
    "SECRET_KEY" : "j+8t^!679rs4kg1_-mhyg7hrtl0fev@c5(3&pd#$o=)n%uq*iwb",
	"ADMIN_URL" : "2xsmRyVBiMlHAh",
	"LOGIN_URL" : "S6rXbRPmouBM0t7",
	"SIGNIN_URL" : "5Iox0a2eGLZquj63A",
	"LOGOUT_URL" : "Q2VKFmT8OfL1bGhoz",
	"BLOG_CREATE" : "WmSrJRK5AFN",
	"BLOG_CHANGE" : "86YDMKoPlucEznJ27",
	"BLOG_DELETE" : "e2lkBmfcjY8uNi1ab",
	"TIME_ZONE" : "Asia/Kolkata",
	"DEBUG" : true
}
```
So, respective sites will be at,
Admin site : ***hosturl/2xsmRyVBiMlHAh***

Login site : ***hosturl/S6rXbRPmouBM0t7***

Signin site : ***hosturl/5Iox0a2eGLZquj63A***

Logout site : ***hosturl/Q2VKFmT8OfL1bGhoz***

Blog Create site : ***hosturl/blog/WmSrJRK5AFN***

Blog Change site : ***hosturl/blog/86YDMKoPlucEznJ27/blog_id***

Blog Delete site : ***hosturl/e2lkBmfcjY8uNi1ab/blog_id***


* Start the server,
```shell
$:django_blog\> python manage.py runserver
```

Only one user can sign in using the signin site. So you can either create it by visiting *Signin Site* or by using the django command,

```shell
$:django_blog\> python manage.py createsuperuser username
```

You are free to create other users using `createsuperuser` command as shown above.

Visit your Hosturl (say : *http://127.0.0.1:8000/*) and you will the home page.
Signin or Login and create some articles.

You will see them appearing in Blog Site (say : *http://127.0.0.1:8000/blog/*).

If user is signed in then he/she will be able to create/change/delete articles.
Else he/she will only be able to view articles.