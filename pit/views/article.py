from pit.views.base import View
from pit.models import Pit, Topic


class ArticleView(View):

    def get(self):
        pits = Pit.query.all()
        pit = Pit.query.first()
        topics = Topic.query.all()
        return self.render(
            'article/pits.html', pits=pits, pit=pit, topics=topics)
