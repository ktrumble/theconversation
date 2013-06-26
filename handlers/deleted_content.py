from base import BaseHandler
from lib.auth import admin_only
from models import Content

class DeletedContentHandler(BaseHandler):
    @admin_only
    def get(self):
        cur_page = 0
        length = 50
        import pdb
        pdb.set_trace()
        deleted_content = Content.objects(deleted=True)[cur_page*length:cur_page+length]
        self.vars.update({
            'deleted_content': deleted_content,
        })
        self.render('deleted_content/index.html', **self.vars)