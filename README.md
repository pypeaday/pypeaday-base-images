# Base Images

This repo is a side-project of mine to several ends:

1. Learn GitHub Actions better
2. Implement specific things in Actions
    * Testing
    * Linting (python, docker, yaml)
    * Building Docker images
    * Shipping Docker images
    * Multi-stage builds
    * Project gating (ie. manual approval based on git branch or something)
3. Translate the Actions CI pipeline and tasks to other frameworks
    * Goal: self-hosted
    * idea: self-hosted GH agent
    * idea: Jenkins pipeline
    * idea: Nomad?
4. Help outline basic CI/CD and DevOps concepts as a general reference
    * CI Pipeline with GH Actions
    * Testing Python applications
    * Linting Dockerfiles, yaml/config, python

# Images

## Hello World

The `hello-world` directory is a simple lightweight dockerfile that echos "hello world" via an entrypoint script.

## Python Hello World

The `python-hello-world` directory is a basic `hatch` project to illustrate a few things:

1. Dockerizing a Python application
2. Testing a Python application
3. Testing a Python application in CI
4. Linting Python code in CI
