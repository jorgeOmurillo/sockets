{# ... #}
{% load staticfiles %}
{# ... #}

{% block extra_body %}
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/reconnecting-websocket/1.0.0/reconnecting-websocket.min.js"></script>
    <script src="{% static "main.js" %}"></script>
{% endblock %}
