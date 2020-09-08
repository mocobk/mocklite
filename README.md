docker build -t mock-lite .

docker run -it -d --name mock-lite -v `pwd`/sqlite3.db:/usr/src/sqlite3.db -p 8090:8090 -p 80:80 -p 8080:8080 mock-lite
