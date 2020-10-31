## @image

* @image()
* @image( size )
* @image( size, text )
* @image( size, background, text )
* @image( size, background, foreground, text )
* @image( size, background, foreground, format, text )

生成一个随机的图片地址。

#### size <span class="no-needed">`可选`</span>

指示图片的宽高，格式为 `'宽x高'`。默认从下面的数组中随机读取一个：

```js
[
  '150x100', '300x200', '400x300', '600x450', '800X600',
  '100x150', '200x300', '300x400', '450x600', '600x800',
  '100x100', '200x200', '300x300', '450x450', '600x600'
]
```

#### background <span class="no-needed">`可选`</span>

指示图片的背景色。。

#### foreground <span class="no-needed">`可选`</span>

指示图片的前景色（文字）。。

#### format <span class="no-needed">`可选`</span>

指示图片的格式。可选值包括：`'png'`、`'gif'`、`'jpg'`。

#### text <span class="no-needed">`可选`</span>

指示图片上的文字。默认值为参数 size。

```js
@image()
// => "https://iph.href.lu/450x600?bg=&fg=&text="
@image('300x400')
// => "https://iph.href.lu/300x400?bg=&fg=&text="
@image('300x400', '图片文字')
// => "https://iph.href.lu/300x400?bg=&fg=&text=图片文字"
@image('300x400', '#234567', '图片文字')
// => "https://iph.href.lu/300x400?bg=234567&fg=&text=图片文字"
@image('300x400', '#234567', '#FFFFFF', '图片文字')
// => "https://iph.href.lu/300x400?bg=234567&fg=FFFFFF&text=图片文字"
@image('300x400', '#234567', '#FFFFFF', 'png', '图片文字')
// => "http://dummyimage.com/300x400/234567/FFFFFF.png&text=图片文字"
```
