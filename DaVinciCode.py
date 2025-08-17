from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
import daVinciCode_schema as schemas
from daVinciCode_models import DaVinciCodeResult

import random

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
	allow_credentials=True,
)

# 初始化遊戲
guess_num = random.randint(0, 100)
max_num = 100
min_num = 1
guess_time = 0

# 例外處理 ====================
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	return JSONResponse(
		status_code=422,
		content={
			"message": "error~",
			"errors": exc.errors(),
		},
	)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
	# 可以寫 log
	return JSONResponse(
	    status_code=500,
	    content={"message": "伺服器內部錯誤，請稍後再試"},
	)
# ===============================

@app.post('/checkName')
async def check_name(
	data: schemas.PostDaVinciCodeName,
	db: AsyncSession = Depends(get_db)
):
	print("1. 開始 resetGame")
	result = await db.execute( select(DaVinciCodeResult).where(DaVinciCodeResult.name == data.name) )
	existing = result.scalar_one_or_none()
	if existing:
		return {
			'message': 'This name is already in use.',
			'statusCode': 2
		}
	else:
		return {
			'message': 'What a owson name!',
			'statusCode': 1
		}

@app.get('/resetGame', response_model=schemas.GetResetGame)
async def reset():
	global guess_time, min_num, max_num, guess_num
	guess_num = random.randint(0, 100)
	max_num = 100
	min_num = 1
	guess_time = 0
	return {
		'message': 'START',
		'tips': f'select number {min_num} to {max_num} .',
		'max_num': max_num,
		'guess_time': guess_time,
		'statusCode': 1
	}

@app.get('/getScore', response_model=schemas.GetScore)
async def reset(db: AsyncSession = Depends(get_db)):
	result = await db.execute(
		select(DaVinciCodeResult).order_by(DaVinciCodeResult.guess_time.desc()).limit(1)
	)
	best = result.scalar_one_or_none()
	best_time = schemas.DaVinciCodeResultBase.from_orm(best) if best else None

	score_list_result = await db.execute(
		select(DaVinciCodeResult).order_by(DaVinciCodeResult.guess_time.desc()).limit(5)
	)
	score_list = score_list_result.scalars().all()

	return {
		'best_time': best_time,
		'score_list': score_list,
		'statusCode': 1
	}

@app.post('/guessGame')
def guess_game(data: schemas.PostDaVinciCode):
	global guess_time, min_num, max_num, guess_num
	print(data.guess)
	user_guess = data.guess

	if user_guess < min_num or user_guess > max_num:
		return {
			'message': '?????',
			'tips': f'select number {min_num} to {max_num} .',
			'guess_time': guess_time,
			'statusCode': 1
		}

	guess_time += 1

	if user_guess == guess_num:
		return {
			'tips': f'BOOOOM! the number is {guess_num}. you got {guess_time} safe time！',
			'message': 'BOOOM',
			'status': 'boom',
			'guess_num': guess_num,
			'guess_time': guess_time,
			'statusCode': 1
		}
	else:
		if user_guess < guess_num:
			min_num = user_guess
		else:
			max_num = user_guess

		return {
			'message': 'SAFE',
			'tips': f'select number {min_num} to {max_num} .',
			'status': 'safe',
			'min_num': min_num,
			'max_num': max_num,
			'guess_time': guess_time,
			'statusCode': 1
		}

# [4] 遊戲結束後新增紀錄
@app.post("/saveRecord")
async def add_record(data: schemas.PostDaVinciCodeSave, db: AsyncSession = Depends(get_db)):
	print("1. 開始 resetGame")
	new_record = DaVinciCodeResult(
		name=data.name,
		guess_time=data.guess_time,
	)
	db.add(new_record)
	await db.commit()
	await db.refresh(new_record)
	return new_record