# Tz portal groups

## Run

1. Git clone: `git clone https://github.com/odi1n/tz_portal_group_2.git`
2. Open directory: `cd tz_portal_group_2`
3. Change file env: `mv .env.example .env`
4. Get `CURRATE_API_KEY` on [service](https://currate.ru/)
5. Set `CURRATE_API_KEY` in file .env
6. Docker build-run: `docker-compose up --build`

## Infomation

Link - `localhost:8000`

|Link|Request|Info|
|:---|:---|:---|
|/api/v1/rates/|get|Currentcy exchange|
