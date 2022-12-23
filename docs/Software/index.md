---
title: index
---

{% set nav_title = "Software" %}

# {{ nav_title }}
<ul>
{% for nav_item in nav %}
    {% if nav_item.title.lower() == nav_title.lower() %}
        {% for nav_item in nav_item.children %}
            {{ nav_item.title }}

            {% if nav_item.title and nav_item.title.lower() != "index" %}
            <li>
                <a href="{{ nav_item.url }}">
                    {{ nav_item.title }}
                </a>
            </li>
            {% endif %}
        {% endfor %}
    {% endif %}
{% endfor %}
</ul>
