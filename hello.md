.MD语法入法

# requests module 标题
## h2标题
### h3标题 ###
#### h4标题
##### h5标题
###### h6标题

### 列表
//形式一
+ a
+ b
+ c

//形式二
- d
- e 
- f

//形式三
* g
* h
* i

//正常形式
1. abc
2. bcd
3. cde

//错序效果
2. fgh
4. ghj
9. hij

//嵌套列表
+ 123
    + abc
    + bcd
    + cde
        + hello
        + world
+ 456
+ 789

## 引用
> 我们都一样的是的吗? 魏主的明略
>> 不可能取得胜利的

## 代码块
```
    import sys
    path = sys.argv[0]
```

## 链接
[简书](https://www.jianshu.com "创作你的创作")

[简书]: https://www.jianshu.com '创作你的创作'
[简书]是一个创作社区，任何人都可以在其上进行创作。

## 图片
![my-logo.png](https://upload-images.jianshu.io/upload_images/13623636-6d878e3d3ef63825.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240 "my-logo")

[my-logo.png]: <https://upload-images.jianshu.io/upload_images/13623636-6d878e3d3ef63825.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240> "my-logo"

## 分割线
---
- - -

## 其它
### 强调字体
*md*
**md**
_md_
__md__

### 转义
\\
\*
\+
\-
\`
\_

###删除线
~~删除~~

###表格
|123|234|345|
|:-|:-:|-:|
|abc|bcd|cde|
|abc|bcd|cde|
|abc|bcd|cde|

### 颜色
$\color{red}{talk}$ is cheap, $\color{rgba(0,255,0,.8)}{show}me the $\color{#ff0000}{code}$