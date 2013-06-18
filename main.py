#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import os
import jinja2
import urllib
import urllib2
import json
from google.appengine.ext import db

jinja_environment=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')), autoescape=True)

class MainHandler(webapp2.RequestHandler):
	def get(self):
		reviews=db.GqlQuery("Select * from Reviewss order by created desc")
		self.write(reviews=reviews)
		
	def write(self, **params):
		template = jinja_environment.get_template('home7.html')
		self.response.out.write(template.render(params))
		
	def post(self):
		reviews=db.GqlQuery("Select * from Reviewss order by created desc")
		self.write(reviews=reviews)
		
			
			
class ReviewsHandler(webapp2.RequestHandler):
	def get(self):
		reviews=db.GqlQuery("Select * from Reviewss order by created desc")
		self.write(reviews=reviews)
		
	def write(self, **params):
		template = jinja_environment.get_template('reviews2.html')
		self.response.out.write(template.render(params))
		
	def post(self):
		self.response.headers['Content-Type']='text/plain'
		content=self.request.get("content")
		user = self.request.get("user")
		if content:
			a=Reviewss(content=content, user=user)
			a.put()
			self.response.out.write("success")
		else:
			self.response.out.write("failure")
			
			
class DevHandler(webapp2.RequestHandler):
	def get(self):
		self.write()
		
	def write(self, **params):
		template = jinja_environment.get_template('dev.html')
		self.response.out.write(template.render(params))
		
		
class DemoHandler(webapp2.RequestHandler):
	def get(self):
		self.write()
		
	def write(self, **params):
		template = jinja_environment.get_template('demo.html')
		self.response.out.write(template.render(params))
		
			
			
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

jinja_environment.filters['datetimeformat'] = datetimeformat
		
		
class Reviewss(db.Model):
	user=db.StringProperty()
	content=db.TextProperty(required=True)
	created=db.DateTimeProperty(auto_now_add=True)
	

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/reviews', ReviewsHandler),
	('/dev', DevHandler),
	('/demo', DemoHandler)
], debug=True)
