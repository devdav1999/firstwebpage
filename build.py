print('building static site')
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
middle_html = open('content/index.html').read()
combined_html = top_html + middle_html + bottom_html
open('docs/index.html', 'w+').write(combined html)

print('building static site')
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
middle_html = open('content/projects.html').read()
combined_html = top_html + middle_html + bottom_html
open('docs/projects.html', 'w+').write(combined html)

print('building static site')
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()
middle_html = open('content/contact.html').read()
combined_html = top_html + middle_html + bottom_html
open('docs/projects.html', 'w+').write(combined html)