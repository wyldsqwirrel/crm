file_path = "/Users/lisagills/Django/recruitment/templates/recruitment/apply_for_job.html

html_content =

"""<html>
{% extends "base.html" %}
{% block content %}
<h2>Apply for {{ job.job_title }}</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit Application</button>
</form>
{% endblock %}
</html>"""

# Write the content to the file
with open(file_path, "w") as file:
    file.write(html_content)

print("✅ application file updated successfully!")
