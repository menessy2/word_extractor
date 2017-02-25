import logging
from .models import WordDB, Base
from sqlalchemy.engine.reflection import Inspector
import sys
import sqlalchemy
from sqlalchemy import create_engine, orm


logger = logging.getLogger(__name__)


class DBWrapper:

    """
    Current support is for mysql , however it can be easily extended to the other sql databases
    """
    def __init__(self, username, password,  hostname, port, db_name):
        mysql_str = "mysql://%s:%s@%s:%s" % ( username, password,
                                                 hostname, port)
        full_mysql_str = mysql_str + '/' + db_name
        self.engine = create_engine(full_mysql_str,pool_recycle=1)

        try:
            self.connection =  self.engine.connect()
        except sqlalchemy.exc.OperationalError as err:
            if ' (1049,' in err.args[0]:        # means database not defined , accordingly create it
                self.engine = create_engine(mysql_str,pool_recycle=1)
                self.connection =  self.engine.connect()
                self.connection.execute("CREATE DATABASE %s" % db_name)
                self.engine = create_engine(full_mysql_str,pool_recycle=1)
                self.connection =  self.engine.connect()
                self.create_schema()
            else:
                logging.error("Could not connect to the database given the provided credentials")
                logging.error("Please make sure the credentials are correct")
                sys.exit(1)

        self.check_tables()

        sm = orm.sessionmaker(bind=self.engine, autoflush=True, autocommit=True, expire_on_commit=True)
        self.session = orm.scoped_session(sm)


    def check_tables(self):
        inspector = Inspector.from_engine(self.engine)
        if WordDB.__tablename__ not in inspector.get_table_names():
            WordDB.metadata.create_all(self.engine)


    def create_schema(self):
        Base.metadata.create_all(self.engine)


    def save_object(self, obj):
        self.session.add(obj)
        self.session.flush()


