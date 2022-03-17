all:
	@echo "make lint	 - Check code with flake8"
	@echo "make local	 - Run app locally"
	@echo "make docker   - Run docker container"
	@echo "make down     - Disable docker container"
	@exit 0

lint:
	flake8 app --count --exit-zero --exclude=app/db/migrations/ --max-complexity=10 --max-line-length=127 --statistics
	flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

local:
	uvicorn app.app:app --reload

docker:
	docker-compose up -d --build

down:
	docker-compose down