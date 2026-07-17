import os

def fix_svg(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<?xml' not in content:
        content = '<?xml version="1.0" encoding="utf-8"?>\n' + content
    # add version="1.1" if not present
    if 'version="1.1"' not in content:
        content = content.replace('<svg ', '<svg version="1.1" ')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_svg('e:/precious-05/assets/footer.svg')
fix_svg('e:/precious-05/assets/pipeline.svg')

with open('e:/precious-05/README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme = readme.replace('https://https://github.com/precious-05', 'https://github.com/precious-05')
readme = readme.replace('github-readme-stats.vercel.app', 'github-stats-extended.vercel.app')

with open('e:/precious-05/README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Done")
