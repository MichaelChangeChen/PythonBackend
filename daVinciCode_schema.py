from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# 進入遊戲前要給前端的完整資料（抓最少 guess_time 用）
class DaVinciCodeResultBase(BaseModel):
	id: str
	name: str
	guess_time: int
	play_date: datetime

	class Config:
		from_attributes = True  # 讓 Pydantic 支援 SQLAlchemy ORM 物件

# 新增紀錄用（遊戲結束時傳給後端）
class DaVinciCodeResultCreate(BaseModel):
	name: str
	guess_time: int
	play_date: Optional[datetime] = None  # 不給的話後端會用 default=datetime.utcnow

# 回傳用（新增後或查詢後的完整資料）
class DaVinciCodeResultResponse(BaseModel):
	id: str
	name: str
	guess_time: int
	play_date: datetime

	class Config:
		from_attributes = True    #讓你在回傳 ORM 物件時，不需要手動轉成字典