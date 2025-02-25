关于BFC：
1.定义：块级格式化上下文，独立的渲染区域，不会影响边界外的元素
2.形成条件：①浮动  ②非静态定位static  ③overflow: hidden;  ④display: table
3.布局规则：①区域内容box从上到下排列 
                    ②box垂直方向的距离由margin决定 
                    ③同一个BFC内 box的margin会重叠
                    ④BFC不会与float元素重叠
                    ⑤BFC计算高度也会计算float元素
4.解决的问题：①解决浮动元素重叠问题
                       ②解决父元素高度塌陷问题
                       ③解决margin重叠问题 

