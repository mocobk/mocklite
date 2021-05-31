## @boolean

- @boolean()
- @boolean( min, max, current )

返回一个随机的布尔值。

#### min <span class="no-needed">`可选`</span>

指示参数 current 出现的概率。概率计算公式为 `min / (min + max)`。该参数的默认值为 1，即有 50% 的概率返回参数 current。

#### max <span class="no-needed">`可选`</span>

指示参数 current 的相反值 `!current` 出现的概率。概率计算公式为 `max / (min + max)`。该参数的默认值为 `1`，即有 50% 的概率返回参数 `!current`。

#### current <span class="no-needed">`可选`</span>

可选值为布尔值 `true` 或 `false`。如果未传入任何参数，则返回 `true` 和 `false` 的概率各为 50%。该参数没有默认值。在该方法的内部，依据原生方法 Math.random() 返回的（浮点）数来计算和返回布尔值，例如在最简单的情况下，返回值是表达式 `Math.random() >= 0.5` 的执行结果。

```js
@boolean()
// => true
@boolean(1, 9, true)
// => false
@bool()
// => false
@bool(1, 9, false)
// => true
```

## @natural

- @natural()
- @natural( min )
- @natural( min, max )

返回一个随机的自然数（大于等于 0 的整数）。

#### min <span class="no-needed">`可选`</span>

指示随机自然数的最小值。默认值为 0。

#### max <span class="no-needed">`可选`</span>

指示随机自然数的最大值。默认值为 9007199254740992。

```js
@natural()
// => 1002794054057984
@natural(10000)
// => 71529071126209
@natural(60, 100)
// => 77
```

## @integer

- @integer()
- @integer( min )
- @integer( min, max )

返回一个随机的整数。

#### min <span class="no-needed">`可选`</span>

指示随机整数的最小值。默认值为 -9007199254740992。

#### max <span class="no-needed">`可选`</span>

指示随机整数的最大值。默认值为 9007199254740992。

```js
@integer()
// => -3815311811805184
@integer(10000)
// => 4303764511003750
@integer(60, 100)
// => 96
```

## @float

- @float()
- @float( min )
- @float( min, max )
- @float( min, max, dmin )
- @float( min, max, dmin, dmax )

返回一个随机的浮点数。

#### min <span class="no-needed">`可选`</span>

整数部分的最小值。默认值为 -9007199254740992。

#### max <span class="no-needed">`可选`</span>

整数部分的最大值。默认值为 9007199254740992。

#### dmin <span class="no-needed">`可选`</span>

小数部分位数的最小值。默认值为 0。

#### dmax <span class="no-needed">`可选`</span>

小数部分位数的最大值。默认值为 17。

```js
@float()
// => -1766114241544192.8
@float(0)
// => 556530504040448.25
@float(60, 100)
// => 82.56779679549358
@float(60, 100, 3)
// => 61.718533677927894
@float(60, 100, 3, 5)
// => 70.6849
```

## @character

- @character()
- @character('lower' | 'upper' | 'number' | 'symbol' )
- @character( pool )

返回一个随机字符。

#### pool <span class="no-needed">`可选`</span>

字符串。表示字符池，将从中选择一个字符返回。

如果传入了 `'lower'` 或 `'upper'`、`'number'`、`'symbol'`，表示从内置的字符池从选取：

```js
{
  lower: "abcdefghijklmnopqrstuvwxyz",
  upper: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
  number: "0123456789",
  symbol: "!@#$%^&*()[]"
}
```

如果未传入该参数，则从 `lower + upper + number + symbol` 中随机选取一个字符返回。

```js
@character()
// => "P"
@character('lower')
// => "y"
@character('upper')
// => "X"
@character('number')
// => "1"
@character('symbol')
// => "&"
```

## @string

- @string()
- @string( length )
- @string( pool, length )
- @string( min, max )
- @string( pool, min, max )

返回一个随机字符串。

#### pool <span class="no-needed">`可选`</span>

字符串。表示字符池，将从中选择一个字符返回。

如果传入 `'lower'` 或 `'upper'`、`'number'`、`'symbol'`，表示从内置的字符池从选取：

```js
{
    lower: "abcdefghijklmnopqrstuvwxyz",
    upper: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    number: "0123456789",
    symbol: "!@#$%^&*()[]"
}
```

如果未传入该参数，则从 `lower + upper + number + symbol` 中随机选取一个字符返回。

#### min <span class="no-needed">`可选`</span>

随机字符串的最小长度。默认值为 3。

#### max <span class="no-needed">`可选`</span>

随机字符串的最大长度。默认值为 7。

```js
@string()
// => "pJjDUe"
@string(5)
// => "GaadY"
@string('lower', 5)
// => "jseqj"
@string(7, 10)
// => "UuGQgSYk"
@string('aeiou', 1, 3)
// => "ea"
@string('壹贰叁肆伍陆柒捌玖拾', 3, 5)
// => "肆捌伍叁"
```

## @range

- @range( stop )
- @range( start, stop )
- @range( start, stop, step )

返回一个整型数组。

#### start <span class="no-needed">`可选`</span>

数组中整数的起始值，默认 0 开始。

#### stop <span class="needed">`必选`</span>

数组中整数的结束值（不包含在返回值中）。

#### step <span class="no-needed">`可选`</span>

数组中整数之间的步长。默认值为 1。

```js
@range(10)
// => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
@range(3, 7)
// => [3, 4, 5, 6]
@range(1, 10, 2)
// => [1, 3, 5, 7, 9]
@range(1, 10, 3)
// => [1, 4, 7]
```
