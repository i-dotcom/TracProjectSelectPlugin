# -*- ocding: utf-8 -*-
"""
= !ProjectSelect: switch between projects in multiproject environment =
"""

from trac.core import Component, implements
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_script
from genshi.builder import tag
from trac.web.api import IRequestFilter
import ConfigParser

import os
import posixpath

class ProjectSelect(Component):
    
    implements(INavigationContributor, ITemplateProvider, IRequestFilter)
    
    # IRequestFilter methods
    def pre_process_request(self, req, handler):
        add_script(req, 'projectselect/projectselect.js')
        return handler

    def post_process_request(self, req, template, content_type):
        return(template, content_type)
    
    # INavigationProvider methods
    def get_navigation_items(self, req):
        projects = []
        projects_names = []
        search_path, this_project = os.path.split(self.env.path)
        base_url, _ = posixpath.split(req.abs_href())
        
        for project in os.listdir(search_path):
            proj_conf = "%s/conf/trac.ini" % (posixpath.join(search_path, project))

            config = ConfigParser.ConfigParser()
            config.read( proj_conf )

            try:
                projects_names.append((config.get("project", "name"), project))
            except ConfigParser.NoSectionError, e:
                pass

        projects_names.sort(lambda a,b: cmp(a[0].lower(),b[0].lower()))

        for p_name, p_dir in projects_names:
                projects.append((tag.option(p_name, selected = (p_dir == this_project or None), value=posixpath.join(base_url, p_dir)), p_dir))

        yield 'metanav', 'projectselect', tag.select([e for e,_ in projects],
                name='projectselect', id='projectselect', onchange='return on_projectselect_change();')
        
    def get_active_navigation_item(self, req):
        return ''
        
    # ITemplateProvider methods
    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('projectselect', resource_filename(__name__, 'htdocs'))]
        
    def get_templates_dirs(self):
        return []
