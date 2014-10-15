import bottle

from bottle import route

@bottle.route('/study_resources/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='study_resources')

@bottle.route('/images/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='images')

if __name__ == "__main__":
	run(host='localhost', port=8003, reloader=True)

mobile = bottle.default_app()
