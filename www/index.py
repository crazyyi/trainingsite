import bottle
from bottle import TEMPLATE_PATH, redirect, request, route, run, jinja2_view, jinja2_template as template

TEMPLATE_PATH.append('./templates')

@route('/images/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='images')

@bottle.route('/styles/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='styles')

@bottle.route('/scripts/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='scripts')

@route('/')
@jinja2_view('index.html')
def index():
	return {'title':'TheRedSunflowers'}

@route('/courses_intro')
@jinja2_view('courses_intro.html')
def courses_intro():
	return {'title':'TheRedSunflowers'}

@route('/activities')
@jinja2_view('activities.html')
def activities():
	return {'title':'TheRedSunflowers'}

@route('/gallery')
@jinja2_view('gallery.html')
def gallery():
	return {'title':'TheRedSunflowers'}

@route('/corporation')
@jinja2_view('corporation.html')
def corporation():
	return {'title':'RedSunflowers'}

@route('/aboutus')
@jinja2_view('aboutus.html')
def style_demo():
	return {'title':'TheRedSunflowers'}

@route('/contactus')
@jinja2_view('contactus.html')
def contactus():
	return {'title':'TheRedSunflowers'}

@route('/resources')
@jinja2_view('resources.html')
def resources():
	return {'title':'RedSunflowers'}

@route('/faq')
@jinja2_view('faq.html')
def faq():
	return {'title':'TheRedSunflowers'}

@route('/submit_comment', method='POST')
def submit_comment():
	name = request.forms.get("name").decode("utf-8")
	email = request.forms.get("email").decode("utf-8")
	comment = request.forms.get("comment").decode("utf-8")

	redirect("/contactus")

if __name__ == "__main__":
	run(host='localhost', port=8000, reloader=True)

app = bottle.default_app()




