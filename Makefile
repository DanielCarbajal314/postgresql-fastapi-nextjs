up:
	docker compose up
down:
	docker compose down
down-clear:
	docker compose down -v
db-gui:
	open http://localhost:8080
shell-to-server:
	docker compose exec server bash
run-migrations:
	docker compose exec server bash -c "alembic upgrade head"
add-migrations:
	docker compose exec server bash -c "alembic revision --autogenerate -m /"$(name)/""
format:
	docker compose exec server bash -c "black ./src"
