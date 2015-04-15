# Shorter

An useless Bitly wrapper

## Requirements

- Python 2.7+
- Tornado 4.1
- Unirest

## Running

Set `BITLY_TOKEN` and `BITLY_SHORTER_DOMAIN` environment variables to access Bitly API.
Set `REQUIRE_AUTH`, `AUTH_USER`, `AUTH_PWD` to require Basic Auth.
Set `STATIC_FOLDER` to point static pages folder (`./static`).

Run `python server.py`.

Access [localhost:8888](http://localhost:8888).

## Deploy

This application can be deployed at [OpenShift](https://www.openshift.com/).

Remember to edit `wsgi.py` file.

## Purpose

The main purpose of this project was to work with Tornado and Bitly API.

## Bitly

To get an access token visit [this page](https://bitly.com/a/oauth_apps).

To setup you own custom domain for Bitly, visit [this page](https://bitly.com/a/settings/advanced).
