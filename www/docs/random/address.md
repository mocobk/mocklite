## @region

* @region()

随机生成一个（中国）大区。

```js
@region()
// => "华北"
```

## @province

* @province()

随机生成一个（中国）省（或直辖市、自治区、特别行政区）。

```js
@province()
// => "黑龙江省"
```

## @city

* @city()
* @city( prefix )

随机生成一个（中国）市。

#### prefix <span class="no-needed">`可选`</span>

布尔值。指示是否生成所属的省。

```js
@city()
// => "唐山市"
@city(true)
// => "福建省 漳州市"
```

## @county

* @county()
* @county( prefix )

随机生成一个（中国）县。

#### prefix <span class="no-needed">`可选`</span>

布尔值。指示是否生成所属的省、市。

```js
@county()
// => "上杭县"
@county(true)
// => "甘肃省 白银市 会宁县"
```

## @zip

* @zip()

随机生成一个邮政编码（六位数字）。

```js
@zip()
// => "908812"
```
