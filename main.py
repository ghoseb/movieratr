#!/usr/bin/env python
## main.py --  -*- Python -*-
## Time-stamp: "2009-01-07 17:00:15 ghoseb"

## Copyright (c) 2009, Baishampayan Ghose <b.ghose@gmail.com>
## Copyright (c) 2009, oCricket.com

import os
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    
    path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
