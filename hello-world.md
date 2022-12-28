---
cover: ''
date: 2022-12-04
datetime: 2022-12-04 00:00:00+00:00
description: The smallest example is my This is simply a lightweight Docker image
  that I wanted to work through an example of using multiple stages for a build I
  am using  T
edit_link: https://github.com/edit/main/pages/hello-world.md
long_description: The smallest example is my This is simply a lightweight Docker image
  that I wanted to work through an example of using multiple stages for a build I
  am using  The main pre-commit hook that matters here is The  We could use bash to
  build and tag our D
now: 2022-12-28 01:06:35.987336
path: pages/hello-world.md
published: true
slug: hello-world
status: draft
super_description: The smallest example is my This is simply a lightweight Docker
  image that I wanted to work through an example of using multiple stages for a build
  I am using  The main pre-commit hook that matters here is The  We could use bash
  to build and tag our Docker images, but GH Actions has a nice option for us called  I
  want to use best-practice tools and for GH Actions I think this makes good Note
  that I specify  Also note, and this is just my playing around, that I output the
  docker image This is usef
tags:
- quick
- home
templateKey: ''
title: Hello World
today: 2022-12-28
---

The smallest example is my
[hello-world](https://github.com/pypeaday/pypeaday-base-images/tree/main/hello-world)
and associated
[build](https://github.com/pypeaday/pypeaday-base-images/blob/main/.github/workflows/ci-hello-world.yml)

This is simply a lightweight Docker image that's built in my CI pipeline and
deployed to my DockerHub for now.

# Multi-Stage CI

I wanted to work through an example of using multiple stages for a build
pipeline (note for an example this small this is ridiculous)

## Lint

I am using [pre-commit]() basically whenever I can. In this repo I will use it
heavily but also do some linting explicitly just for practice. In general I'd
say it's best to consoloidate tools as much as makes sense - and pre-commit
makes sense for wrapping a bunch of linting (and testing) into one GH Action,
or one more general task in a different CI system

The main pre-commit hook that matters here is
[hadolint](https://github.com/hadolint/hadolint) which I'm playing with as a
Dockerfile linter

## Build

The `build` job is where we build the Docker image. This is a different
job/stage so that it can be running at the same time as the lint checks, rather
than one after the other.

We could use bash to build and tag our Docker images, but GH Actions has a nice option for us called `docker/build-push-action@v3`

I want to use best-practice tools and for GH Actions I think this makes good
sense, otherwise we'd have to write a little bash - examples below

```yaml
      - name: Build and export
        uses: docker/build-push-action@v3
        with:
          context: ./hello-world
          file: ./hello-world/alpine.Dockerfile
          build-args: |
            BASE_VERSION=${{env.BASE_VERSION}}
          tags: |
            hello-world-alpine-latest
          outputs: type=docker,dest=/tmp/myimage.tar
```

Note that I specify `context` here because my base-images repo is kind of a
meta-repo with just sub-directories that are not git-submodules. Therefore in
practice this might/probably be unnecessary.

Also note, and this is just my playing around, that I output the docker image
to a `tar` file which is available in cache to all the jobs in a workflow. I
think more generally this is just serializing an artifact somewhere that your
runner/task manager has access to

This is useful for:
  1. breaking up the stages of `build` and `push` because otherwise the GH Action wants to just push right to Docker
  2. sharing the docker image with other stages if that becomes relevant... I have ideas

## Push

Our Push job starts by setting up the same Docker build environment that the
Docker job uses (canned GH Action - probably similar options in other CI
systems) then logging into DockerHub.

We don't re-build the image - instead we grab the `tar` file from the cache and
make sure it's good to go before manually tagging the image in a relevant way -
like with a version or branch name

Pushing then happens based on the branch - this is highly subject to change and
be different depending on any team's CI/CD workflow
<div class='prevnext'>

    <style type='text/css'>

    :root {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #e1bd00c9;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="light"] {
      --prevnext-color-text: #1f2022;
      --prevnext-color-angle: #ffeb00;
      --prevnext-subtitle-brightness: 3;
    }
    [data-theme="dark"] {
      --prevnext-color-text: #eefbfe;
      --prevnext-color-angle: #e1bd00c9;
      --prevnext-subtitle-brightness: 3;
    }
    .prevnext {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: flex-start;
    }
    .prevnext a {
      display: flex;
      align-items: center;
      width: 100%;
      text-decoration: none;
    }
    a.next {
      justify-content: flex-end;
    }
    .prevnext a:hover {
      background: #00000006;
    }
    .prevnext-subtitle {
      color: var(--prevnext-color-text);
      filter: brightness(var(--prevnext-subtitle-brightness));
      font-size: .8rem;
    }
    .prevnext-title {
      color: var(--prevnext-color-text);
      font-size: 1rem;
    }
    .prevnext-text {
      max-width: 30vw;
    }
    </style>
    
    <a class='prev' href='/404'>
    

        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13.5 8.25L9.75 12L13.5 15.75" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"> </path>
        </svg>
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>prev</p>
            <p class='prevnext-title'>Whoops that page was not found</p>
        </div>
    </a>
    
    <a class='next' href='/'>
    
        <div class='prevnext-text'>
            <p class='prevnext-subtitle'>next</p>
            <p class='prevnext-title'>Markata Blog Starter</p>
        </div>
        <svg width="50px" height="50px" viewbox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.5 15.75L14.25 12L10.5 8.25" stroke="var(--prevnext-color-angle)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
    </a>
  </div>