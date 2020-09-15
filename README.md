docker build -t mock-lite .

docker run -it -d --name mock-lite -v `pwd`/../mock-lite-sqlite3.db:/usr/src/sqlite3.db -p 80:80 -p 8080:8080 mock-lite
docker run -it -d --name mock-lite -v `pwd`/../mock-lite-sqlite3.db:/usr/src/sqlite3.db -p 80:80 -p 8080:8080 -p 9001:9001 mock-lite
