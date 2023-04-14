# Real state backend

## Requirements

 * Docker
 * Docker Compose
 * [Python 3](https://www.python.org/)
 * [pre-commit](https://pre-commit.com/)

## Setup

Install the git hooks with:

```bash
$ pre-commit install
$ cp ./git-hook-commit-msg .git/hooks/commit-msg
```

Run the `install.sh` script:

```bash
$ ./install.sh
```

Start Docker containers:

```bash
$ docker-compose up -d
```

Create a new superuser:

```bash
$ docker-compose run web python manage.py createsuperuser
```

Link to http://localhost/admin/ and log in!



### Access Adminer in the browser

To access the database, go to http://localhost:8080/ and use the following credentials:

 * System: PostgreSQL
 * Server: database
 * Username: real_state
 * Password: real_state!
 * Database: real_state


### Access Mongo Express in the browser

To access the database, go to http://localhost:8081/ and use the following credentials:

 * Username: real_state
 * Password: real_state!
