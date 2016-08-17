from google.appengine.ext import ndb

class Tag(ndb.Model):
  name = ndb.StringProperty()
  created_at = ndb.DateTimeProperty(auto_now_add=True)
