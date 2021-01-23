from flask import Flask, render_template, abort, request
import os 
import json

app = Flask(__name__)

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


app.jinja_env.globals.update(get_category_translation=get_category_translation)


def get_categories():
	return os.listdir(get_abs_path(['templates', CATEGORIES_PATH]))


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


@app.route('/', methods=['GET'])
def home():
	lang = get_lang(request)

	print(load_meta('Music'))

	return render_template(f'home/home_{lang}.html', 
		projects=get_projects(), 
		lang=lang)


@app.route('/category/<category>', methods=['GET'])
def render_category(category):
	lang = get_lang(request)

	if category in get_projects():
		return render_template('category/category_en.html', 
			category=category, 
			projects=get_projects(), 
			lang=lang)
	else:
		abort(404)


@app.route('/category/<category>/<project_path>', methods=['GET'])
def render_project(category, project_path):
	lang = get_lang(request)
	projects = get_projects()

	if category in projects and get_project_by_path(category, project_path):
		return render_template(os.path.join(CATEGORIES_PATH, category, project_path, 'page.html'), 
			projects=projects, 
			lang=lang)
	else:
		abort(404)