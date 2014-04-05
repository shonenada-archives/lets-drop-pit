from tornado.web import URLSpec

from pit.views.master import IndexView
# from pit.views.account import SignInView
from pit.views.article import ArticleView


url_list = [
    URLSpec(r'/', IndexView, name='index'),
    # URLSpec(r'/account/signin', SignInView, name='account_sign_in'),
    URLSpec(r'/article/list', ArticleView, name='article_list'),
]
 