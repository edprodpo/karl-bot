DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = karl-vk-bot
PROJECT_NAME = karl


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} -p ${PROJECT_NAME} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} ${ENV} -p ${PROJECT_NAME} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest
