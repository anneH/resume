import glob
import os
import sys
from jinja2 import Template
all_html_files = glob.glob("content/*.html")

#Prompts for a system argument
def select_command():
    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        create_html_file(get_pages())
    elif command == "new":
        print("New page was specified")
        new_content= '''
        <h1>New Content!</h1>
        <p>New content...</p>
        '''
        open('content/new_content_page.html', 'w+').write(new_content)
    else:
        print("Please specify ’build’ or ’new’")
 
# Gets the file name from the file path
def get_file_name(path):
        file_name = os.path.basename(path)
        name_only = os.path.splitext(file_name)
        return name_only

# Gets the file name and extension from the file path
def get_file_name_and_extension(path):
        file_name = os.path.basename(path)
        name_only, extension = os.path.splitext(file_name)
        return name_only + extension

# Creates the pages array from the files in the content directory
def get_pages():
        pages = []
        for file in all_html_files:
            pages.append({
                "filename": file,
                "title": get_file_name(file),
                "output": "docs/" + get_file_name_and_extension(file),
                "link" : "./"+get_file_name_and_extension(file),
            })
        return pages

#Creates the new html file for each page
def create_html_file(pages):
        for page in pages:
            content_html = open(page['filename']).read()
            template_html = open('./templates/base.html').read()
            template = Template(template_html)
            new_template = template.render(
                title=page['title'],
                content=content_html,
                pages=pages,
            )
            open(page['output'], 'w+').write(new_template)