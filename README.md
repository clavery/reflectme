reflectme
=========

Simple HTTP server for recording requests and returning arbitrary responses.

Installation
------------

```sh
$ pip install reflectme
```

Usage
-----

```sh
$ reflectme 0.0.0.0 8080
```

Open `http://localhost:8080` and create a new path (`test` below)

```sh
$ curl http://localhost:8080/test -i --data "foo=bar"
```

Refresh the inspection page to view your results.
