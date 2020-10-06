
def main():

# Page information
    pages = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title":  "About Me",

        },

        {
            "filename": "content/resume.html",
            "output": "docs/resume.html",
            "title": "Resume",

        },

        {
            "filename": "content/blog.html",
            "output": "docs/blog.html",
            "title": "Blog",
        }
    ]

# Reads base template
    template_base = open('./templates/base.html').read()

# Creates a new template by adding content to the base template
    def create_template(filename):
        template_content = open(filename).read()
        template = template_base.replace("{{content}}", template_content)
        return template

# Writes the template created to a file
    def writeToTemplateFile(output, template):
        open(output, 'w+').write(template)

# Loops through each page in pages to create a template and write it to the output file
    for page in pages:
       output = page['output']
       filename = page['filename']
       template = create_template(filename)
       writeToTemplateFile(output, template)

if __name__ == "__main__":
  main()
