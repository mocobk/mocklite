## @paragraph

* @paragraph()
* @paragraph( len )
* @paragraph( min, max )

随机生成一段文本。

#### len <span class="no-needed">`可选`</span>

指示文本中句子的个数。默认值为 3 到 7 之间的随机数。

#### min <span class="no-needed">`可选`</span>

指示文本中句子的最小个数。默认值为 3。

#### max <span class="no-needed">`可选`</span>

指示文本中句子的最大个数。默认值为 7。


```js
@paragraph()
// => "Yohbjjz psxwibxd jijiccj kvemj eidnus disnrst rcconm bcjrof tpzhdo ncxc yjws jnmdmty. Dkmiwza ibudbufrnh ndmcpz tomdyh oqoonsn jhoy rueieihtt vsrjpudcm sotfqsfyv mjeat shnqmslfo oirnzu cru qmpt ggvgxwv jbu kjde. Kzegfq kigj dtzdd ngtytgm comwwoox fgtee ywdrnbam utu nyvlyiv tubouw lezpkmyq fkoa jlygdgf pgv gyerges wbykcxhwe bcpmt beqtkq. Mfxcqyh vhvpovktvl hrmsgfxnt jmnhyndk qohnlmgc sicmlnsq nwku dxtbmwrta omikpmajv qda qrn cwoyfaykxa xqnbv bwbnyov hbrskzt. Pdfqwzpb hypvtknt bovxx noramu xhzam kfb ympmebhqxw gbtaszonqo zmsdgcku mjkjc widrymjzj nytudruhfr uudsitbst cgmwewxpi bye. Eyseox wyef ikdnws weoyof dqecfwokkv svyjdyulk glusauosnu achmrakky kdcfp kujrqcq xojqbxrp mpfv vmw tahxtnw fhe lcitj."
    
@paragraph(2)
// => "Dlpec hnwvovvnq slfehkf zimy qpxqgy vwrbi mok wozddpol umkek nffjcmk gnqhhvm ztqkvjm kvukg dqubvqn xqbmoda. Vdkceijr fhhyemx hgkruvxuvr kuez wmkfv lusfksuj oewvvf cyw tfpo jswpseupm ypybap kwbofwg uuwn rvoxti ydpeeerf."
    
@paragraph(1, 3)
// => "Qdgfqm puhxle twi lbeqjqfi bcxeeecu pqeqr srsx tjlnew oqtqx zhxhkvq pnjns eblxhzzta hifj csvndh ylechtyu."
```

## @cparagraph

* @cparagraph()
* @cparagraph( len )
* @cparagraph( min, max )

随机生成一段中文文本。

参数的含义和默认值同 **@paragraph**

```js
@cparagraph()
// => "给日数时化周作少情者美制论。到先争劳今已美变江以好较正新深。族国般建难出就金感基酸转。任部四那响成族利标铁导术一或已于。省元切世权往着路积会其区素白思断。加把他位间存定国工取除许热规先法方。"
    
@cparagraph(2)
// => "去话起时为无子议气根复即传月广。题林里油步不约认山形两标命导社干。"
    
@cparagraph(1, 3)
// => "候无部社心性有构员其深例矿取民为。须被亲需报每完认支这明复几下在铁需连。省备可离展五斗器就石正队除解动。"
```

## @sentence

* @sentence()
* @sentence( len )
* @sentence( min, max )

随机生成一个句子，第一个单词的首字母大写。

#### len <span class="no-needed">`可选`</span>

指示句子中单词的个数。默认值为 12 到 18 之间的随机数。

#### min <span class="no-needed">`可选`</span>

指示句子中单词的最小个数。默认值为 12。

#### max <span class="no-needed">`可选`</span>

指示句子中单词的最大个数。默认值为 18。

```js
@sentence()
// => "Jovasojt qopupwh plciewh dryir zsqsvlkga yeam."
@sentence(5)
// => "Fwlymyyw htccsrgdk rgemfpyt cffydvvpc ycgvno."
@sentence(3, 5)
// => "Mgl qhrprwkhb etvwfbixm jbqmg."
```

## @csentence

* @csentence()
* @csentence( len )
* @csentence( min, max )

随机生成一段中文文本。

参数的含义和默认值同 **@sentence**

```js
@csentence()
// => "第任人九同段形位第律认得。"
    
@csentence(2)
// => "维总。"
    
@csentence(1, 3)
// => "厂存。"
```

## @word

* @word()
* @word( len )
* @word( min, max )

随机生成一个单词。

#### len <span class="no-needed">`可选`</span>

指示单词中字符的个数。默认值为 3 到 10 之间的随机数。

#### min <span class="no-needed">`可选`</span>

指示单词中字符的最小个数。默认值为 3。

#### max <span class="no-needed">`可选`</span>

指示单词中字符的最大个数。默认值为 10。

```js
@word()
// => "fxpocl"
@word(5)
// => "xfqjb"
@word(3, 5)
// => "kemh"
```

## @cword

* @cword()
* @cword( pool )
* @cword( length )
* @cword( pool, length )
* @cword( min, max )
* @cword( pool, min, max )

随机生成一个汉字。

#### pool <span class="no-needed">`可选`</span>

汉字字符串。表示汉字字符池，将从中选择一个汉字字符返回。

#### min <span class="no-needed">`可选`</span>

随机汉字字符串的最小长度。默认值为 1。

#### max <span class="no-needed">`可选`</span>

随机汉字字符串的最大长度。默认值为 1。

```js
@cword()
// => "干"
@cword('零一二三四五六七八九十')
// => "六"
@cword(3)
// => "别金提"
@cword('零一二三四五六七八九十', 3)
// => ""七七七""
@cword(5, 7)
// => "设过证全争听"
@cword('零一二三四五六七八九十', 5, 7)
// => "九七七零四"
```

## @emoji

* @emoji()
* @emoji( pool )
* @emoji( length )
* @emoji( pool, length )
* @emoji( min, max )
* @emoji( pool, min, max )

随机生成一个或多个 emoji 表情字符。

#### pool <span class="no-needed">`可选`</span>

可以是任意字符串，如常用字符、特殊字符、emoji等，将从中选择一个或多个字符返回。

#### min <span class="no-needed">`可选`</span>

随机 emoji 字符串的最小长度。默认值为 1。

#### max <span class="no-needed">`可选`</span>

随机 emoji 字符串的最大长度。默认值为 1。

```js
@emoji()
// => "😷"
@emoji('😀😁😂😃😄')
// => "😁"
@emoji(3)
// => "😂😃😄"
@emoji('😀😁😂😃😄', 2)
// => ""😃😀""
@emoji(3, 6)
// => "🐥🐄🍪🌘😷🙊"
@emoji('123🌘😷🙊★♠♫', 3, 6)
// => "★2🌘😷"
```

## @title

* @title()
* @title( len )
* @title( min, max )

随机生成一句标题，其中每个单词的首字母大写。

#### len <span class="no-needed">`可选`</span>

指示单词中字符的个数。默认值为 3 到 7 之间的随机数。

#### min <span class="no-needed">`可选`</span>

指示单词中字符的最小个数。默认值为 3。

#### max <span class="no-needed">`可选`</span>

指示单词中字符的最大个数。默认值为 7。

```js
@title()
// => "Rduqzr Muwlmmlg Siekwvo Ktn Nkl Orn"
@title(5)
// => "Ahknzf Btpehy Xmpc Gonehbnsm Mecfec"
@title(3, 5)
// => "Hvjexiondr Pyickubll Owlorjvzys Xfnfwbfk"
```

## @ctitle

* @ctitle()
* @ctitle( len )
* @ctitle( min, max )

随机生成一句中文标题。

参数的含义和默认值同 **@title**

#### len <span class="no-needed">`可选`</span>

指示单词中字符的个数。默认值为 3 到 7 之间的随机数。

#### min <span class="no-needed">`可选`</span>

指示单词中字符的最小个数。默认值为 3。

#### max <span class="no-needed">`可选`</span>

指示单词中字符的最大个数。默认值为 7。

```js
@ctitle()
// => "证构动必作"
@ctitle(5)
// => "应青次影育"
@ctitle(3, 5)
// => "出料阶相"
```
