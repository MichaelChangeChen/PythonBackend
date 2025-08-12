from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import random

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# 初始化遊戲
guess_num = random.randint(0, 100)
max_num = 100
min_num = 1
guess_time = 0

# 定義前端送過來的資料格式
class GuessRequest(BaseModel):
	guess: int	# 前端要傳入的數字欄位


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	return JSONResponse(
		status_code=422,
		content={
			"message": "請輸入正確的整數數字！",
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


@app.get('/resetGame')
def reset():
	global guess_time, min_num, max_num, guess_num
	guess_num = random.randint(0, 100)
	max_num = 100
	min_num = 1
	guess_time = 0
	return ({
		'message': 'START',
		'tips': f'select number {min_num} to {max_num} .',
		'max_num': max_num,
		'guess_time': guess_time,
		'statusCode': 1
	})


@app.post('/guessGame')
def guess_game(data: GuessRequest):
	global guess_time, min_num, max_num, guess_num
	print(data.guess)
	user_guess = data.guess

	if user_guess < min_num or user_guess > max_num:
		return ({
			'message': '?????',
			'tips': f'select number {min_num} to {max_num} .',
			'guess_time': guess_time,
			'statusCode': 1
		})

	guess_time += 1

	if user_guess == guess_num:
		return ({
			'tips': f'BOOOOM! the number is {guess_num}. you got {guess_time} safe time！',
			'message': 'BOOOM',
			'status': 'boom',
			'guess_num': guess_num,
			'guess_time': guess_time,
			'statusCode': 1
		})
	elif user_guess < guess_num or user_guess > guess_num:
		if user_guess < guess_num:
			min_num = user_guess
		elif user_guess > guess_num:
			max_num = user_guess

		return ({
			'message': 'SAFE',
			'tips': f'select number {min_num} to {max_num} .',
			'status': 'safe',
			'min_num': min_num,
			'max_num': max_num,
			'guess_time': guess_time,
			'statusCode': 1
		})