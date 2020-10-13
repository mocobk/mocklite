docker build -t mock-lite .

docker run -d --name mock-lite --restart=always -v `pwd`/../mock-lite-data/db:/usr/src/db -v `pwd`/../mock-lite-data/mitmproxy:/root/.mitmproxy -p 80:80 -p 8888:8888 mock-lite
