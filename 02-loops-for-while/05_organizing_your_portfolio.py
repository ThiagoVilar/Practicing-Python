# Activity 05: Organizing your portfolio
# Goes through a list of projects and shows each valid name.
# If an item is None, shows the message "Missing project".

projects = ['website', 'game', 'data analysis', None, 'mobile app']

for project in projects:
    if project is None:
        print('Missing project')
    else:
        print(project)