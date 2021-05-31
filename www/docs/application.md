## 场景一：Mock 未开发的接口
<span class="no-needed">`前端开发` `后端开发`</span>

我们在进行前端或后端开发时，需要依赖某一个接口，但该接口可能同时也在开发，为了实现并行开发，我们可以根据
接口文档 Mock 该接口。

![](./_media/20201014192407659.jpg ':size=30%')
![](./_media/20201014192235201.jpg ':size=30%')

## 场景二：Mock 大量的数据
<span class="no-needed">`测试`</span>

有时我们在测试数据展示时需要有大量数据的场景，我们可以借助 Mock 功能快速生成大量的数据响应。

![](./_media/20201014193846668.jpg  ':size=30%')
![](./_media/20201014194128051.jpg  ':size=40%')

## 场景三：Mock 异常响应
<span class="no-needed">`测试`</span>

一般情况下接口会响应正常的数据，当我们想验证异常场景时的响应时，可以使用 Mock 拦截。

![](./_media/20201014200757179.jpg  ':size=30%')
![](./_media/20201014200639036.jpg  ':size=30%')

## 场景四：Mock 特殊数据
<span class="no-needed">`测试`</span>

测试移动 APP、H5、Web页面时经常需要验证一些特殊数据的渲染，如超长字符、特殊字符、emoji表情等。

![](./_media/20201014202200228.jpg ':size=30%')
![](./_media/20201014202133559.jpg ':size=30%')

## 场景五：Mock GraphQL 接口
<span class="no-needed">`测试`</span>

GraphQL 接口一般 URL 都是同一个，大部分 Mock 工具无法区分拦截。MockLite 支持匹配 GraphQL 中的 `operationName` 或 `queryName`，从而可以针对不同 GraphQL 进行拦截匹配。

![](./_media/20210531202910962.png ':size=30%')

## 更多场景等你发现
