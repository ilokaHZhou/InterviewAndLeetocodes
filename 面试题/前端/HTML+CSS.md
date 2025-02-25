# CSS

## 如何实现两栏布局？

在 CSS 中实现两栏布局有多种方式，下面为你详细介绍常见的几种实现方法：

### 1. 使用浮动（Float）
浮动是实现两栏布局比较传统的方法，通过设置元素的 `float` 属性让元素脱离文档流并向左或向右浮动。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
       .left {
            float: left;
            width: 30%;
            background-color: lightblue;
        }

       .right {
            float: left;
            width: 70%;
            background-color: lightgreen;
        }

       .clearfix::after {
            content: "";
            display: table;
            clear: both;
        }
    </style>
</head>

<body>
    <div class="clearfix">
        <div class="left">左侧栏</div>
        <div class="right">右侧栏</div>
    </div>
</body>

</html>
```
**解释**：
- `float: left` 使 `.left` 和 `.right` 元素向左浮动。
- `width` 属性分别设置左右两栏的宽度。
- `.clearfix` 类用于清除浮动，避免父元素高度塌陷。

### 2. 使用 Flexbox
Flexbox 是一种弹性布局模型，它提供了强大的布局能力，能轻松实现两栏布局。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
       .container {
            display: flex;
        }

       .left {
            flex: 0 0 30%;
            background-color: lightblue;
        }

       .right {
            flex: 0 0 70%;
            background-color: lightgreen;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="left">左侧栏</div>
        <div class="right">右侧栏</div>
    </div>
</body>

</html>
```
**解释**：
- `display: flex` 将 `.container` 元素设置为 Flex 容器。
- `flex: 0 0 30%` 和 `flex: 0 0 70%` 分别设置左右两栏的初始大小。

### 3. 使用 Grid 布局
Grid 布局是一种二维布局模型，它可以将页面划分为行和列，方便实现复杂的布局。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
       .container {
            display: grid;
            grid-template-columns: 30% 70%;
        }

       .left {
            background-color: lightblue;
        }

       .right {
            background-color: lightgreen;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="left">左侧栏</div>
        <div class="right">右侧栏</div>
    </div>
</body>

</html>
```
**解释**：
- `display: grid` 将 `.container` 元素设置为 Grid 容器。
- `grid-template-columns: 30% 70%` 定义了两列的宽度。

### 4. 使用绝对定位
通过设置元素的 `position` 属性为 `absolute` 来实现两栏布局。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
       .container {
            position: relative;
            height: 200px;
        }

       .left {
            position: absolute;
            left: 0;
            width: 30%;
            height: 100%;
            background-color: lightblue;
        }

       .right {
            position: absolute;
            right: 0;
            width: 70%;
            height: 100%;
            background-color: lightgreen;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="left">左侧栏</div>
        <div class="right">右侧栏</div>
    </div>
</body>

</html>
```
**解释**：
- `.container` 设置为 `position: relative`，作为定位的参考元素。
- `.left` 和 `.right` 设置为 `position: absolute`，通过 `left` 和 `right` 属性确定位置。

以上几种方法都可以实现两栏布局，其中 Flexbox 和 Grid 布局是比较现代和推荐的方式，它们提供了更强大和灵活的布局能力。


## CSS什么是BFC，怎么开启BFC
### BFC 定义
BFC即块级格式化上下文，是一个独立的渲染区域，规定了内部块级元素的布局方式，并且与外部元素相互隔离。其内部元素布局不受外部影响，也不会影响外部元素。

### 开启 BFC 的方式
1. **浮动元素**：设置 `float` 值为 `left` 或 `right`。
2. **绝对定位元素**：`position` 值设为 `absolute` 或 `fixed`。
3. **行内块元素**：`display` 为 `inline - block`。
4. **表格单元格**：`display` 是 `table - cell`。
5. **弹性项目**：作为 `display` 为 `flex` 或 `inline - flex` 容器的子元素。
6. **网格项目**：作为 `display` 为 `grid` 或 `inline - grid` 容器的子元素。
7. **设置 `overflow`**：`overflow` 值不为 `visible`，如 `auto`、`hidden` 等。 





## 