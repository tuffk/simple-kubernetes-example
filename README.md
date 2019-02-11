# simple-kubernetes-example
Very basic kubernetes flask API deployment

Code for `Catedra de computo cognitivo`

# Local Setup
`pip install -r requirements.txt`

## Run
### Export environment variables
```shell
export FLASK_APP=server.py
export FLASK_ENV=development
```
### Start the server
```shell
flask run
```
Then open a browser with the url `localhost:5000`

# Endpoints
## GET
`url/<name>`
name is a string

## POST
`url/`
parameter
```json
{
  "name": "string"
}
```
name is a string
