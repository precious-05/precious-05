import os
import re

readme_path = 'e:/precious-05/README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace username
content = content.replace('username=alinaliaquat', 'username=precious-05')
content = content.replace('user=alinaliaquat', 'user=precious-05')

# 2. Extract pipeline SVG and replace
pipe_match = re.search(r'<svg width="800" height="180".*?</svg>', content, re.DOTALL)
if pipe_match:
    with open('e:/precious-05/assets/pipeline.svg', 'w', encoding='utf-8') as f:
        f.write(pipe_match.group(0))
    content = content.replace(pipe_match.group(0), '<img src="./assets/pipeline.svg" width="100%" alt="ML Pipeline" />')

# 3. Extract footer SVG and replace
footer_match = re.search(r'<svg width="100%" height="80".*?</svg>', content, re.DOTALL)
if footer_match:
    with open('e:/precious-05/assets/footer.svg', 'w', encoding='utf-8') as f:
        f.write(footer_match.group(0))
    content = content.replace(footer_match.group(0), '<img src="./assets/footer.svg" width="100%" alt="Footer" />')

# 4. Replace top SVG with Banner3.jpg
top_match = re.search(r'<!-- Custom Animated SVG Header - Simplified Styling -->\n<svg width="100%" height="220".*?</svg>', content, re.DOTALL)
if top_match:
    content = content.replace(top_match.group(0), '<img src="./assets/Banner3.jpg" width="100%" alt="Banner" />')

# 5. Bring back girl.gif
# Look for the Deep Learning badge and closing div
dl_badge = '<img src="https://img.shields.io/badge/Deep%20Learning-Neural%20Networks-2E294E?style=for-the-badge&logo=pytorch&logoColor=white" alt="Deep Learning" />\n\n</div>'
dl_replacement = '<img src="https://img.shields.io/badge/Deep%20Learning-Neural%20Networks-2E294E?style=for-the-badge&logo=pytorch&logoColor=white" alt="Deep Learning" />\n\n<br />\n<br />\n\n<img src="./assets/girl.gif" width="150" height="170" alt="Alina" />\n\n</div>'
content = content.replace(dl_badge, dl_replacement)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
