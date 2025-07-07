html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Yasas Harshana - Portfolio</title>
</head>
<body>
    <h1>Hello, I'm Yasas Harshana</h1>
    <p>This is my simple portfolio page.</p>
    <p>testing</p>
</body>
</html>
"""

with open("build/index.html", "w") as f:
    f.write(html_content)
