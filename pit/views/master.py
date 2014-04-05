from pit.views.base import View


class IndexView(View):

    def get(self):
        return self.render('index.html')
