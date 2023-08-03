from db_worker import insert_to_db, delete
from parser import parser
delete()
auction_data = parser()
insert_to_db(auction_data)