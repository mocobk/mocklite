## @date

* @date()
* @date(format)

返回一个随机的日期字符串。

#### format <span class="no-needed">`可选`</span>

指示生成的日期字符串的格式。默认值为 `yyyy-MM-dd`。

可选的占位符参考自 [Ext.Date](http://docs.sencha.com/ext-js/4-1/#!/api/Ext.Date)，如下所示：

| Format  | Description                                                 | Example
| ------- | ----------------------------------------------------------- | --------------
| yyyy    | A full numeric representation of a year, 4 digits           | 1999 or 2003
| yy      | A two digit representation of a year                        | 99 or 03
| y       | A two digit representation of a year                        | 99 or 03
| MM      | Numeric representation of a month, with leading zeros       | 01 to 12
| M       | Numeric representation of a month, without leading zeros    | 1 to 12
| dd      | Day of the month, 2 digits with leading zeros               | 01 to 31
| d       | Day of the month without leading zeros                      | 1 to 31
| HH      | 24-hour format of an hour with leading zeros                | 00 to 23
| H       | 24-hour format of an hour without leading zeros             | 0 to 23
| hh      | 12-hour format of an hour without leading zeros             | 1 to 12
| h       | 12-hour format of an hour with leading zeros                | 01 to 12
| mm      | Minutes, with leading zeros                                 | 00 to 59
| m       | Minutes, without leading zeros                              | 0 to 59
| ss      | Seconds, with leading zeros                                 | 00 to 59
| s       | Seconds, without leading zeros                              | 0 to 59
| SS      | Milliseconds, with leading zeros                            | 000 to 999
| S       | Milliseconds, without leading zeros                         | 0 to 999
| A       | Uppercase Ante meridiem and Post meridiem                   | AM or PM
| a       | Lowercase Ante meridiem and Post meridiem                   | am or pm
| T       | Milliseconds, since 1970-1-1 00:00:00 UTC                   | 759883437303

```js
@date()
// => "2002-10-23"
@date('yyyy-MM-dd')
// => "1983-01-29"
@date('yy-MM-dd')
// => "79-02-14"
@date('y-MM-dd')
// => "81-05-17"
@date('y-M-d')
// => "84-6-5"
```

## @time

* @time()
* @time( format )

返回一个随机的时间字符串。

#### format <span class="no-needed">`可选`</span>

指示生成的时间字符串的格式。默认值为 `HH:mm:ss`。

可选的占位符参考自 [Ext.Date](http://docs.sencha.com/ext-js/4-1/#!/api/Ext.Date)，请参见 @date( format? )。

```js
@time()
// => "00:14:47"
@time('A HH:mm:ss')
// => "PM 20:47:37"
@time('a HH:mm:ss')
// => "pm 17:40:00"
@time('HH:mm:ss')
// => "03:57:53"
@time('H:m:s')
// => "3:5:13"
```

## @datetime

* @datetime()
* @datetime( format )

返回一个随机的日期和时间字符串。

#### format <span class="no-needed">`可选`</span>

指示生成的日期和时间字符串的格式。默认值为 `yyyy-MM-dd HH:mm:ss`。

可选的占位符参考自 [Ext.Date](http://docs.sencha.com/ext-js/4-1/#!/api/Ext.Date)，请参见 @date( format? )。

```js
@datetime()
// => "1977-11-17 03:50:15"
@datetime('yyyy-MM-dd A HH:mm:ss')
// => "1976-04-24 AM 03:48:25"
@datetime('yy-MM-dd a HH:mm:ss')
// => "73-01-18 pm 22:12:32"
@datetime('y-MM-dd HH:mm:ss')
// => "79-06-24 04:45:16"
@datetime('y-M-d H:m:s')
// => "02-4-23 2:49:40"
```

## @timestamp

* @timestamp()

返回一个随机的时间戳。

## @now

* @now()
* @now( unit, format )
* @now( format )
* @now( unit )

返回当前的日期和时间字符串。

#### unit <span class="no-needed">`可选`</span>

表示时间单位，用于对当前日期和时间进行格式化。可选值有：`year`、`month`、`week`、`day`、`hour`、`minute`、`second`、`week`，默认不会格式化。

#### format <span class="no-needed">`可选`</span>

指示生成的日期和时间字符串的格式。默认值为 `yyyy-MM-dd HH:mm:ss`。可选的占位符参考自 [Ext.Date](http://docs.sencha.com/ext-js/4-1/#!/api/Ext.Date)，请参见 [@date(format)](#date)。

```js
@now()
// => "2014-04-29 20:08:38 "
@now('day', 'yyyy-MM-dd HH:mm:ss SS')
// => "2014-04-29 00:00:00 000"
@now('day')
// => "2014-04-29 00:00:00 "
@now('yyyy-MM-dd HH:mm:ss SS')
// => "2014-04-29 20:08:38 157"
@now('year')
// => "2014-01-01 00:00:00"
@now('month')
// => "2014-04-01 00:00:00"
@now('week')
// => "2014-04-27 00:00:00"
@now('day')
// => "2014-04-29 00:00:00"
@now('hour')
// => "2014-04-29 20:00:00"
@now('minute')
// => "2014-04-29 20:08:00"
@now('second')
// => "2014-04-29 20:08:38"
```
