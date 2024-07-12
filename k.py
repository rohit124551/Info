import os

folder_path = 'E:\Info\cdp\cdp_report'  # Replace this with the path to your folder

html_content = '''<html>
<head>
  <title>PDF Files</title>
</head>
<body>
'''

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.pdf'):
            file_path = os.path.join(foldername, filename)
            link_text = os.path.basename(filename)
            link_href = os.path.relpath(file_path, folder_path).replace('\\', '/')

            html_content += f''' <a class="link" href="..\cdp\cdp_report\{link_href}">{link_text}</a><br>'''

html_content += '</body></html>'

with open('cdp.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file created successfully!")