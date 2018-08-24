# pythonToZtree
ztree的json标准格式
`{name:"第一层级",children:[{name:"第二层级",id:2,childred:[{}]}],id:1}`

当遇到json层级多嵌套多，数据复杂时，一般会选择由后端来处理ztree的json格式

当我们从MongoDB获取到json数据后，想要返回给前端做树型结构的页面展示时，可能你也会用到此函数


