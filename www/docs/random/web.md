## @url

* @url()
* @url( protocol )
* @url( protocol, host )

随机生成一个 URL。

#### protocol <span class="no-needed">`可选`</span>


指定 URL 协议。例如 `http`。

#### host <span class="no-needed">`可选`</span>

指定 URL 域名和端口号。例如 `nuysoft.com`。

```js
@url()
// => "mid://axmg.bg/bhyq"
@url('http')
// => "http://splap.yu/qxzkyoubp"
@url('http', 'nuysoft.com')
// => "http://nuysoft.com/ewacecjhe"
```

## @protocol

* @protocol()

随机生成一个 URL 协议。返回以下值之一：`'http'`、`'ftp'`、`'gopher'`、`'mailto'`、`'mid'`、`'cid'`、`'news'`、`'nntp'`、`'prospero'`、`'telnet'`、`'rlogin'`、`'tn3270'`、`'wais'`。

```js
@protocol()
// => "ftp"
```

## @domain

* @domain()

随机生成一个域名。

```js
@domain()
// => "kozfnb.org"
```

## @tld

* @tld()

随机生成一个顶级域名（Top Level Domain）。

```js
@tld()
// => "net"
```

## @email

* @email()
* @email( domain )

随机生成一个邮件地址。

#### domain <span class="no-needed">`可选`</span>

指定邮件地址的域名。例如 `nuysoft.com`。

```js
@email()
// => "x.davis@jackson.edu"
@email('nuysoft.com')
// => "h.pqpneix@nuysoft.com"
```

## @ip

* @ip()

随机生成一个 IP 地址。

```js
@ip()
// => "34.206.109.169"
```
