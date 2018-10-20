from chatbot.views.base import View


class IndexView(View):
    def __init__(self):
        super(IndexView, self).__init__()
        self.template_name = 'index'

    def render(self):
        path_file = self.get_template_path()

        with open(path_file, 'r') as f:
            html = f.read()

        return html
