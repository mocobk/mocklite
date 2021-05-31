## @capitalize

* @capitalize(word)

把字符串的第一个字母转换为大写。

```js
@capitalize('hello')
// => "Hello"
```

## @upper

* @upper( str )

把字符串转换为大写。

```js
@upper('hello')
// => "HELLO"
```

## @lower

* @lower( str )

把字符串转换为小写。

```js
@lower('HELLO')
// => "hello"
```

## @pick

* @pick( arr )

从数组中随机选取一个元素，并返回。

```js
@pick(['a', 'e', 'i', 'o', 'u'])
// => "o"
```

## @shuffle

* @shuffle( arr )
* @shuffle( arr, length )
* @shuffle( arr, min, max )

打乱数组中元素的顺序，并返回。

#### length <span class="no-needed">`可选`</span>

返回后的数组长度。

#### min <span class="no-needed">`可选`</span>

返回后的数组最小长度。

#### max <span class="no-needed">`可选`</span>

返回后的数组最大长度。

```js
@shuffle(['a', 'e', 'i', 'o', 'u'])
// => ["o", "u", "e", "i", "a"]

@shuffle(['a', 'e', 'i', 'o', 'u'], 3)
// => ["o", "u", "i"]

@shuffle(['a', 'e', 'i', 'o', 'u'], 2, 4)
// => ["o", "u"]
```
