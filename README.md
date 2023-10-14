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

* [Python] (3.10): an interpreted high-level programming language