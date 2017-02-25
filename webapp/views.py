import tornado
import urllib
import validators
from webapp import return_most_frequent_n, return_words_from_remote_url_page


class MainHandler(tornado.web.RequestHandler):

    DB_MANAGER = None


    def get(self):
        self.render("index.html", error_msg=None, result='')

    def post(self):
        try:
            url = urllib.parse.parse_qsl(self.request.body)[0][1].decode("utf-8")
            if not validators.url(url):
                self.render("index.html", error_msg="Supplied URL is not valid", result='')
        except IndexError:
            self.render("index.html", error_msg="Supplied URL is not valid", result='')

        words = return_words_from_remote_url_page(url)
        result = return_most_frequent_n(words,100)

        text = ''

        for key, count in result:
            MainHandler.DB_MANAGER.add_word(key, count, url)
            word = key + ' '            # not efficient , can be implemented in much better way given more time
            text += word*count          # not efficient , can be implemented in much better way given more time

        self.render("index.html", error_msg=None, result=text)