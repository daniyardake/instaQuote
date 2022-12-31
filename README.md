To run:
`./bootstrap.sh`

To add new user:
`curl -i -H "Content-Type: application/json" -X POST -d '{"login":"daniyar", "password":"123"}' http://localhost:5000/user/signup`
