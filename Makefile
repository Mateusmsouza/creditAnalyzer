run-server:
	uvicorn server:app

unit:
	pytest tests/unit