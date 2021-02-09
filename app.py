from internal import *
from flask import Flask, render_template, abort, request

app = Flask(__name__)
app.jinja_env.globals.update(get_category_translation=get_category_translation, 
	get_category_color=get_category_color)

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
	print(f'category/category_{lang}.html')
	if category in get_projects():
		return render_template(f'category/category_{lang}.html', 
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
		return render_template(os.path.join(CATEGORIES_PATH, category, project_path, f'page_{lang}.html'), 
			projects=projects, 
			lang=lang)
	else:
		abort(404)