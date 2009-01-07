#!/usr/bin/env python
## not_found.py --  Not found handler -*- Python -*-
## Time-stamp: "2009-01-07 20:19:08 ghoseb"

## Copyright (c) 2009, Baishampayan Ghose <b.ghose@gmail.com>
## Copyright (c) 2009, oCricket.com

import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class NotFound(webapp.RequestHandler):
    """Raise an HTTP 404
    """

    def get(self):
        """
        """
        self.error(404)

def main():
  application = webapp.WSGIApplication([('/', NotFound)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
        
    
        

