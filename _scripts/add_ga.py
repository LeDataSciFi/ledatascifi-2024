# -*- coding: utf-8 -*-
"""
The way jupyter-book-0.10.X inserts Google Analytics is no longer functional.

Until I can update to a version of JB that does GA correct, I'm going to try 
this work around.

The plan: 
    
    This py file: Go through all the html files in _build/html, and insert 
    the GA snippet after head.
    
    .github/workflows/deploy.yml: Adjust the action to run this file after
    the book is built but before deployment.
"""

import glob

files = glob.glob("_build/html/content/**/*.html", recursive=True)

# set up find and replace

old = '<head>'
new = '''<head>
   <!-- Global site tag (gtag.js) - Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-QHB6CBHE8P"></script>
   <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-QHB6CBHE8P');
   </script>
'''

# replace

for file in files:
    # file = '../_build/html/content/frontpage - Copy.html'
    print(file)
    
    with open(file, 'r', encoding="utf-8") as f:
        raw_file = f.read()
    
    processed_file = raw_file.replace(old,new)

    with open(file, 'w', encoding="utf-8") as f:
        f.write(processed_file)

