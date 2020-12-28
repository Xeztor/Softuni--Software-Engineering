import re

html_code = input()

title = re.findall(r'<title>(.+)</title>', html_code)
title = title.pop()
print(f'Title: {title}')

content = re.sub(r'.+<body>', '', html_code)
content = re.sub(r'</?[^<>]+>|\\n', '', content)
print(f"Content: {content}")
