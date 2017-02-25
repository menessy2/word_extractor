import logging
from .models import WordDB
import _mysql_exceptions
import sqlalchemy
import hashlib
from webapp.settings import HASH_SALT, ASYMMETRIC_PUB_KEY, ASYMMETRIC_PRIVATE_KEY
from .db_wrapper import DBWrapper
import base64

logger = logging.getLogger(__name__)

class ModelManager:

    def __init__(self, MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB_NAME):
        self.db_wrapper = DBWrapper(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB_NAME)

    def hash_word(self, word):
        m = hashlib.sha512()
        m.update(HASH_SALT.encode('utf-8'))
        m.update(word.encode('utf-8'))
        return m.hexdigest()

    def encrypt_word(self, word):
        result = ASYMMETRIC_PUB_KEY.encrypt(word.encode('utf-8'), 32)[0]
        print(result)
        return base64.b64encode(result)


    def decrypt_word(self, word):
        pass

    def is_word_already_exists(self, word, website_page):
        return self.db_wrapper.session.query(WordDB).filter_by(word_hash=self.hash_word(word),
                                                                website_page=website_page).first()

    def add_word(self, word, count, website):
        client = WordDB(word_hash=self.hash_word(word), count=count, website_page=website,
                        word_enc=self.encrypt_word(word) )
        try:
            self.db_wrapper.save_object(client)
        except ( _mysql_exceptions.IntegrityError, sqlalchemy.exc.IntegrityError) :
            logger.debug("Word already exists in DB, overriding it")
            self.db_wrapper.session.query(WordDB).filter_by(word_hash=self.hash_word(word),website_page=website).update({
                'count' : count,
            })
            self.db_wrapper.session.flush()