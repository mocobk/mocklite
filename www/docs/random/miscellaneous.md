## @guid

* @guid()

随机生成一个 GUID。

```js
@guid()
// => "662C63B4-FD43-66F4-3328-C54E3FF0D56E"
```

`@guid()` 的实现参考了 [UUID 规范](http://www.ietf.org/rfc/rfc4122.txt)。

## @id

* @id()

随机生成一个 18 位身份证。

```js
@id()
// => "420000200710091854"
```

## @version

* @version()
* @version(depth)

随机生成一个版本号，每一位的最大值不超过10

#### depth <span class="no-needed">`可选`</span>

版本号的层级，默认为 3

```js
@version()
// => 3.6.1
@version(4)
// => 4.9.1.8
```

## @increment

* @increment()
* @increment( step )

生成一个全局的自增整数。

#### step <span class="no-needed">`可选`</span>

整数自增的步长。默认值为 1。

```js
@increment()
// => 1
@increment(100)
// => 101
@increment(1000)
// => 1101
```

## @phone

* @phone()

生成一个中国的手机号。

```js
@phone()
// => 13088757656
```
