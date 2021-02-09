import os 
import json

CATEGORIES_PATH = 'categories'


# Generates an absolute path for a string or a list of strings
def get_abs_path(paths):
	if type(paths) is list:
		return os.path.abspath(os.path.join(*paths))
	elif type(paths) is str:
		return os.path.abspath(paths)
	else:
		raise FileNotFoundError


# Loads the meta data for a specific category
def load_meta(category):
	path = get_abs_path([CATEGORIES_PATH, category, 'meta.json'])
	with open(path) as file:
		return json.load(file)


def get_category_translation(category, lang):
	try:
		return load_meta(category).get(lang).get("category_name")
	except KeyError:
		return ''

def get_category_color(category):
	try:
		return load_meta(category).get("color").upper()
	except KeyError:
		return "0x000000"


def get_categories():
	return sorted(os.listdir(get_abs_path(['templates', CATEGORIES_PATH])))


# Get projects in form of {Category: 	[{name: project name with spaces, 
#										path: project filetree name, 
#										category: The category of the project}]}
def get_projects():
	projects_dict = {}
	for category in get_categories():
		projects_dict[category] = []
		projects = os.listdir(get_abs_path(['templates', CATEGORIES_PATH, category]))
		for project in projects:
			if os.path.isdir(get_abs_path(['templates', CATEGORIES_PATH, category, project])):
				projects_dict[category].append({
					'category': {'en': load_meta(category).get('en').get('category_name'),
						'sv': load_meta(category).get('sv').get('category_name')},
					'path': project,
					'name': {'en': load_meta(category).get('en').get('project_name').get(project),
						'sv': load_meta(category).get('sv').get('project_name').get(project)}
				})
		projects_dict[category].sort()
	return projects_dict


# Filters the project by path and returns the project
def get_project_by_path(category, path):
	try:
		return list(filter(lambda project: project.get('path') == path, get_projects().get(category)))[0]
	except IndexError:
		return 0


def get_lang(request):
	lang = request.args.get('language', None)
	if not lang in ['en', 'sv']:
		return 'en'
	return lang
