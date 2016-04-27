import json
import os
from sys import exit

# Compose a markdown inline-style link
def compose_markdown_link( name, url ):
    return "[" + name + "]" + "(" + url + ")"

# Compose a group of html image tags
def compose_html_image_tags(stack):
    tech_stacks = ""
    for tech in stack:
        tech_stacks += "<img src='./resource/icons/" + tech + ".png' height='35px'> "
    return tech_stacks

# ----------- Starts here -----------
current_dir = os.path.dirname(os.path.realpath(__file__))
print current_dir

with open(current_dir + '/projects.json') as data_file:
    projects = json.load(data_file)

if projects['projects'] == []:
    print 'No Data!'
    exit()

project_categories = ["full stack", "mobile", "big data"]

base_table = "| Projects | Teams | Description |Stacks | \n" + \
             "| :-------------: |:-------------:| :----: |:-----:| \n"

tables = {}
for category in project_categories:
    tables[category] = base_table

for project in projects['projects']:

    categories = project['category']
    project_with_url = compose_markdown_link(project['name'], project['project_url'])
    tech_stacks = compose_html_image_tags(project['stack'])

    row = "|" + project_with_url + \
          "|" + project['team'] + \
          "|" + project['description'] + \
          "|" + tech_stacks + \
          "|" + '\n'

    for category in categories:
        if tables.has_key(category):
            tables[category] = tables[category] + row


f = open(current_dir + "/../OutStandingProjects.md",'w')
for key, value in tables.iteritems():
    if (value != base_table):
        f.write("## " + key.upper() + "\n\n")
        f.write(value.encode('utf8') + "\n\n")
f.close()
