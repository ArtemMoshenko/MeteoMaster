metadata = MetaData()
engine = create_engine('sqlite:///user_database', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()
