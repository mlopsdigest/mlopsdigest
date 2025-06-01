---
layout: home
---

<p>
  <img src="/assets/banner/banner.png" width="600px" alt="MLOps Lifecycle" style="display: block; margin: 0 auto;" />
</p>

# Welcome to MLOps Digest

**Curated, practical insights for the modern ML engineer.**  
Stay ahead with weekly tutorials, code recipes, and real-world strategies for deploying and managing machine learning in production.

- Hands-on MLOps, data engineering, and automation
- Bite-sized guides, opinion, and expert-curated links
- No hype. No basics. Just what matters for practitioners.

Browse by category below, or [subscribe](/subscribe) to get new issues straight to your inbox.

<!-- Gather unique categories from all posts -->
{% assign all_categories = "" | split: "" %}
{% for post in site.posts %}
  {% for category in post.categories %}
    {% unless all_categories contains category %}
      {% assign all_categories = all_categories | push: category %}
    {% endunless %}
  {% endfor %}
{% endfor %}

<!-- Display categories and their posts -->
{% for category in all_categories %}
  <h2>{{ category }}</h2>
  <ul>
    {% for post in site.posts %}
      {% if post.categories contains category %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
{% endfor %}