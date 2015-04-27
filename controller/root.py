import cherrypy
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('template'))


class BaseController:

    def _render(self, tmpl_name, **kw):
        #tmpl_name = kw.get(tmpl_name, 'index')
        tmpl = env.get_template('.'.join([tmpl_name, 'html']))
        return tmpl.render(**kw)


class RootController(BaseController):

    @cherrypy.expose
    def index(self, **kw):
        return self._render(tmpl_name='index', name='LemonPy')
