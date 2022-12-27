---
date: 2022-09-01 1:00:00
title: Markata Blog Starter
published: True
tags:
  - home
  - meta

---

Welcome to Pypeaday Base Image docs

## Some helpful pages

{% for post in markata.map('post', sort='date', filter='post.get("published", False)==True and date<=today and "quick" in post.get("tags", [])', reverse=False) %}
!!! note "[{{ post['title'] }}]({{ post['slug'] }})"
    {{post['description']}}...
{% endfor %}
