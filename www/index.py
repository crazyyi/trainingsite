import bottle
from bottle import TEMPLATE_PATH, route, run, jinja2_view, jinja2_template as template

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
	return {'title':'RedSunflowers'}

@route('/3-columns')
@jinja2_view('3-columns.html')
def three_columns():
	return {'title':'RedSunflowers'}

@route('/full-width')
@jinja2_view('full-width.html')
def full_width():
	return {'title':'RedSunflowers'}

@route('/gallery')
@jinja2_view('gallery.html')
def gallery():
	return {'title':'RedSunflowers'}

@route('/corporation')
@jinja2_view('corporation.html')
def corporation():
	return {'title':'RedSunflowers'}

@route('/aboutus')
@jinja2_view('aboutus.html')
def style_demo():
	return {'title':'RedSunflowers'}

@route('/contactus')
@jinja2_view('contactus.html')
def contactus():
	return {'title':'RedSunflowers'}

@route('/resources')
@jinja2_view('resources.html')
def resources():
	return {'title':'RedSunflowers'}

@route('/faq')
@jinja2_view('faq.html')
def faq():
	return {'title':'RedSunflowers'}

if __name__ == "__main__":
	run(host='localhost', port=8000, reloader=True)

app = bottle.default_app()




