##Requirements
pipenv (uses Pipfile)
docker

##Usage:
Start the zipkin Backend & UI:
`docker-compose up -d`

Install the dependencies:
`pipenv install`

Run the server (need multiple worker threads because the flask app calls
itself, and I'm lazy):
`pipenv run gunicorn -w 4 hello:app`
