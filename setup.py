from sqlalchemy import create_engine

class SkeleSetup:
    def __init__(self):
        initdb()

    def initdb(self):
        db = create_engine('sqlite:///./db/skeleblog.db', echo = True)
        return "Db initialised"


