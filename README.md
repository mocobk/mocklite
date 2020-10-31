MockLite 使用 python 开发，并复用了 Mock.js 模板语法和随机数据生成，使用过程中需配置网络代理以拦截接口数据，
最终返回生成的 Mock 数据。

## MockLite 是如何工作的 (How Works)
假如我们在测试一个电商项目，用 App 访问商品列表，这时我们配置了商品列表接口的 Mock 拦截，当我们设置拦截状态为
打开，然后在 App 中访问商品列表，此时商品列表接口请求会先进入我们的代理服务器，代理服务识别到该接口需要拦截，
继而生成对应的 Mock 数据并直接返回 HTTP 响应，而 App 请求其他接口时，代理服务会将原请求直接转发到原目标地址，
获取真实的响应数据。

![](https://i.loli.net/2020/10/30/R5HFol17tAqVjGW.png)


## 特性 (Features)

* 拥有多项目 Web 管理界面
* 支持自定义 HTTP 响应码、响应头、响应体
* 快速测试拦截匹配
* 一键开启、关闭 Mock 接口
* 支持同一接口配置多个响应内容
* 支持所有 HTTP/HTTPS 协议接口
* 支持 Mock.js 模板语法和随机数据生成
* 支持模板语法智能提示、补全
* 适用全终端: Web | H5 | PC | Android | iOS
* 提供 Docker 容器部署，方便快捷


## 安装部署 (Install)
```bash
docker pull mocklite
```

```bash
docker run -d --name mocklite --restart=always \
-v `pwd`/db:/usr/src/db \
-v `pwd`/mitmproxy:/root/.mitmproxy \
-p 80:80 \
-p 8888:8888 \
mocobk/mocklite
```

* ``-v `pwd`/db:/usr/src/db``  持久化数据库
* ``-v `pwd`/mitmproxy:/root/.mitmproxy``  持久化 HTTPS 证书秘钥
* `-p 80:80`  映射 web 管理地址端口为 80
* `-p 8888:8888`  映射代理服务器端口为 8888

> 假如你部署的服务器 IP 为 172.22.102.102，管理后台端口映射为 80，代理服务端口映射为 8888, 那么启动后可以访问 [http://172.22.102.102]()来打开 web 配置后台，
在你的浏览器或手机端配置代理 172.22.102.102:8888 来使用 Mock 拦截。

## 文档 (Documents)
[docs](https://mocobk.github.io/mocklite)  | [国内访问](https://mocobk.gitee.io/mocklite)