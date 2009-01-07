#!/usr/bin/env python
## main.py --  -*- Python -*-
## Time-stamp: "2009-01-07 20:19:47 ghoseb"

## Copyright (c) 2009, Baishampayan Ghose <b.ghose@gmail.com>
## Copyright (c) 2009, oCricket.com

import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):

  def get(self):
    user = users.get_current_user()
    if user:
      logout_url = users.create_logout_url('/')
      login_url = False
      is_admin = users.is_current_user_admin()
    else:
      logout_url = False
      login_url = users.create_login_url("/")
      is_admin = False

    template_values = {'user':user,
                       'login_url':login_url,
                       'logout_url':logout_url,
                       'is_admin':is_admin}

    path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    self.response.out.write(template.render(path, template_values))


class DummyHandler(webapp.RequestHandler):
    """A simple dummy handler
    """

    def get(self):
        """Show the page
        """
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'templates', 'dummy.html')
        self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/request/', DummyHandler),
                                        ('/manage/', DummyHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
