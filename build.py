# Read all files used for template creation
top_template = open('./templates/top.html').read()
bottom_template = open('./templates/bottom.html').read()
index_content = open('./content/index.html').read()
resume_content = open('./content/resume.html').read()
blog_content = open('./content/blog.html').read()

# Create index.html template in the docs directory
index_file = top_template + index_content + bottom_template
open('./docs/index.html', 'w+').write(index_file)


# Create resume.html template in the docs directory
resume_file = top_template + resume_content + bottom_template
open('./docs/resume.html', 'w+').write(resume_file)


# Create blog.html template in the docs directory
blog_file = top_template + resume_content + bottom_template
open('./docs/blog.html', 'w+').write(blog_file)



