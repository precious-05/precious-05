import urllib.request

icons = ['python', 'java', 'cpp', 'c', 'js', 'tensorflow', 'pytorch', 'scikit', 'scikitlearn', 'pandas', 'numpy', 'fastapi', 'postgres', 'mongodb', 'mysql', 'sqlite', 'git', 'androidstudio', 'vercel', 'netlify', 'linux', 'arduino']

for icon in icons:
    try:
        url = f"https://skillicons.dev/icons?i={icon}"
        req = urllib.request.Request(url, method="HEAD")
        resp = urllib.request.urlopen(req)
        if resp.status == 200:
            pass #print(f"{icon}: OK")
    except Exception as e:
        print(f"{icon}: FAILED ({e})")
