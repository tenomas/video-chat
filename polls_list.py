<!-- polls_list.html -->
{% extends "base.html" %}
{% block title %}Polls Application Site{% endblock %}

{% block sidebar %}
  {{ block.super }}
  <ul>
    <li><a href="/polls/">Polls_Home</a></li>
  </ul>
{% endblock %}
