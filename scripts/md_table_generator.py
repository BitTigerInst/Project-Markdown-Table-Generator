#!/usr/bin/python

import os
import re
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/lib")
import markdown2

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

with open(current_dir + '/projects.json') as data_file:
    projects = json.load(data_file)

if projects['projects'] == []:
    print 'No Data!'
    sys.exit()

project_categories = ["full stack", "mobile", "big data"]

# markdown2 module requires no spaces between '|' and '\n' each line
base_table = "| Projects | Teams | Description |Stacks |\n" + \
             "| :-------------: |:-------------:| :----: |:-----:|\n"

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

output_files = []
md_file_name = "OutStandingProjects.md"
md_file = open(current_dir + "/../" + md_file_name, 'w')

for key, value in tables.iteritems():
    if (value != base_table):

        # generate markdown table
        md_file.write("## " + key.upper() + "\n\n")
        md_file.write(value.encode('utf8') + "\n\n")

        # generate html table
        html_file_name = key.replace (" ", "_") + ".html"
        html_file = open(current_dir + "/../" + html_file_name, 'w')
        html_table = markdown2.markdown(value.encode('utf8'), extras=["tables"])
        html_file.write(html_table.encode('utf8'))
        html_file.close()
        output_files.append(html_file_name)

md_file.close()
output_files.append(md_file_name)


print "** Please check out the output files:"
for file in output_files:
    print "- " + file

