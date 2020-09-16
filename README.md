docker build -t mock-lite .

docker run -d --name mock-lite --restart=always -v `pwd`/../mock-lite-sqlite3.db:/usr/src
/sqlite3.db -p 80:80 -p 8888:8888 mock-lite
