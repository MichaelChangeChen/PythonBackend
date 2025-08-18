import uuid
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database import Base

class DaVinciCodeResult(Base):
	__tablename__ = "daVinciCode_results"

	# default=lambda 當欄位沒給值時，就去呼叫這個函式的回傳值當預設值。
	id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
	name = Column(String(50), nullable=False)
	guess_time = Column(Integer, nullable=False)
	play_date = Column(DateTime, default=datetime.utcnow)