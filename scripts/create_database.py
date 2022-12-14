
import os
from orchestra.database.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine(os.environ['ORCHESTRA_DATABASE_HOST'])
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
session.commit()
session.close()


