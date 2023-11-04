# Flask Deep Learning

This repository showcases the deployment of a Deep Learning model as a microservice using [Python], [Keras], [Flask], [Docker], [Jupyter Notebook], [microservices], [REST API] and [GitHub Actions].

- [PURPOSE](#purpose)
- [DEPENDENCIES](#dependencies)
  - [PYTHON VIRTUAL ENVIRONMENT](#python-virtual-environment)
- [REPOSITORY CONTENT](#repository-content)
- [ARCHITECTURE](#architecture)
- [DEEP LEARNING MODEL](#deep-learning-model)
- [HOW TO RUN DEEP LEARNING ON FLASK WITH DOCKER COMPOSE](#how-to-run-deep-learning-on-flask-with-docker-compose)
- [TEST SERVER \& REST API](#test-server--rest-api)
- [CREDITS](#credits)

## PURPOSE

The objective here is to deploy a [Deep Learning] model on [Flask] as a microservice. The model is used to predict handwritten digits. It was previously trained on a [Jupyter Notebook]. [REST API] are used to communicate with the deployed model, e.g. send images to be analyzed and return the generated predictions to the client. [GitHub Actions] are used to implement CI/CD workflows in the project.

## DEPENDENCIES

The code has been tested using:

* [Python] (3.10): an interpreted high-level programming language for general-purpose programming.
* [Jupyter Lab] (4.0): a web-based interactive development environment for [Jupyter Notebooks], code and data.
* [Flask] (3.0): a microframework for [Python] based on Werkzeug, Jinja 2 and good intentions.
* [Gunicorn] (21.2): a [Python] [WSGI] HTTP Server for UNIX.
* [NGINX] (1.25): a free, open-source, high-performance HTTP server, reverse proxy, and IMAP/POP3 proxy server.
* [Docker] (24.0): an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud.
* [Docker Compose] (2.21): a tool for defining and running multi-container [Docker] applications.
* [Keras] ([TensorFlow] built-in): a high-level neural networks [API], written in [Python] and capable of running on top of [TensorFlow].
* [TensorFlow] (2.14): an open source software [Deep Learning] library for high performance numerical computation using data flow graphs.
* [Matplotlib] (3.8): a plotting library for [Python] and its numerical mathematics extension [NumPy].
* [NumPy] (1.26): a library for [Python], adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
* [scikit-imag