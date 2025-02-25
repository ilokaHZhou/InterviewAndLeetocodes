# Javascript



## 栈内存和堆内存是什么？

栈内存和堆内存是JavaScript中用于存储数据的两种内存区域，主要区别如下：

---

### **1. 栈内存（Stack Memory）**
- **存储内容**：基本数据类型（如`Number`、`String`、`Boolean`等）和函数调用时的执行上下文。
- **特点**：
  - 内存分配和释放由系统自动管理。
  - 按值访问，数据大小固定。
  - 访问速度快，但空间有限。
- **示例**：
  ```javascript
  let a = 10; // 变量a的值直接存储在栈内存中
  ```

---

### **2. 堆内存（Heap Memory）**
- **存储内容**：引用数据类型（如`Object`、`Array`、`Function`等）。
- **特点**：
  - 内存分配和释放需要手动管理（通过垃圾回收机制）。
  - 按引用访问，数据大小不固定。
  - 访问速度相对较慢，但空间较大。
- **示例**：
  ```javascript
  let obj = { name: "Alice" }; // 对象存储在堆内存中，栈内存中存储的是对象的引用地址
  ```

---

### **总结**
- **栈内存**：存储基本数据类型和函数调用，速度快但空间有限。
- **堆内存**：存储引用数据类型，空间大但访问速度较慢。

两者共同协作，确保JavaScript程序的高效运行。


## 简单说一下set，symbol数据结构

### **1. Set**
- **定义**：`Set`是ES6引入的一种**集合数据结构**，用于存储**唯一值**（无重复元素）。
- **特点**：
  - 值唯一：自动去重。
  - 可迭代：支持`for...of`遍历。
  - 方法：`add()`、`delete()`、`has()`、`clear()`等。
- **示例**：
  ```javascript
  let set = new Set();
  set.add(1); // 添加元素
  set.add(2);
  set.add(1); // 重复添加，无效
  console.log(set); // 输出: Set { 1, 2 }
  ```

---

### **2. Symbol**
- **定义**：`Symbol`是ES6引入的一种**基本数据类型**，表示**唯一且不可变的值**。
- **特点**：
  - 唯一性：每个`Symbol`值都是唯一的，即使描述相同。
  - 不可变性：创建后无法修改。
  - 用途：常用于对象属性的键，避免命名冲突。
- **示例**：
  ```javascript
  let sym1 = Symbol('key');
  let sym2 = Symbol('key');
  console.log(sym1 === sym2); // 输出: false（唯一性）

  let obj = {
    [sym1]: 'value' // 使用Symbol作为键
  };
  console.log(obj[sym1]); // 输出: value
  ```

---

### **总结**
- **Set**：用于存储唯一值的集合，适合去重场景。
- **Symbol**：用于创建唯一标识符，适合避免属性名冲突的场景。



## 包装类是什么？
**包装类**是JavaScript为基本数据类型（如`String`、`Number`、`Boolean`）提供的临时对象，用于在需要时调用方法或访问属性。

---

### **特点**
1. **自动装箱**：当对基本类型调用方法或访问属性时，JavaScript会自动将其转换为对应的包装对象。
   ```javascript
   let str = "hello";
   console.log(str.length); // 5（自动转换为String对象）
   ```
2. **自动拆箱**：操作完成后，包装对象会被丢弃，恢复为基本类型。
3. **手动创建**：可以通过构造函数显式创建包装对象（不推荐）。
   ```javascript
   let strObj = new String("hello"); // 手动创建String对象
   ```

---

### **示例**
```javascript
let num = 42;
console.log(num.toFixed(2)); // "42.00"（自动装箱为Number对象）

let bool = true;
console.log(bool.toString()); // "true"（自动装箱为Boolean对象）
```

---

### **总结**
包装类是JavaScript为基本类型提供的一种临时对象机制，使其能够调用方法或访问属性，但通常不需要显式使用。


## 简述一下JS的垃圾回收机制

JavaScript的垃圾回收机制主要基于以下两种算法：

1. **标记清除（Mark-and-Sweep）**：
   - 从根对象（如全局对象）出发，标记所有可达对象。
   - 清除未被标记的对象（即不可达的垃圾）。

2. **引用计数（Reference Counting）**：
   - 记录每个对象的引用次数。
   - 当引用次数为0时，回收该对象。
   - 缺点：无法处理循环引用。

现代JavaScript引擎（如V8）主要使用**标记清除**及其优化版本（如分代回收、增量回收等），高效管理内存，自动释放不再使用的对象。


## 可以用JS手动实现一个instanceof嘛？

可以手动实现一个`instanceof`，其核心原理是通过递归检查对象的原型链是否包含目标构造函数的`prototype`。以下是实现代码：

---

### **手动实现`instanceof`**
```javascript
function myInstanceof(obj, constructor) {
  // 基本类型直接返回false
  if (obj === null || typeof obj !== 'object') {
    return false;
  }

  // 获取对象的原型
  let proto = Object.getPrototypeOf(obj);

  // 递归检查原型链
  while (proto) {
    // 如果找到目标构造函数的prototype，返回true
    if (proto === constructor.prototype) {
      return true;
    }
    // 继续向上查找原型链
    proto = Object.getPrototypeOf(proto);
  }

  // 未找到，返回false
  return false;
}
```

---

### **使用示例**
```javascript
class Person {}
class Student extends Person {}

const student = new Student();

console.log(myInstanceof(student, Student)); // true
console.log(myInstanceof(student, Person)); // true
console.log(myInstanceof(student, Object)); // true
console.log(myInstanceof(student, Array)); // false
```

---

### **原理**
1. 检查`obj`是否为对象（基本类型直接返回`false`）。
2. 获取`obj`的原型（`Object.getPrototypeOf(obj)`）。
3. 递归检查原型链，直到找到目标构造函数的`prototype`或到达原型链顶端（`null`）。
4. 找到则返回`true`，否则返回`false`。

---


## 说一下闭包吧? 闭包概念 -> 闭包代码解析 -> 闭包本质 (AO,GO结合执行器上下文)->垃圾回收机制->闭包优缺点等

### **闭包总结**

1. **概念**：
   - 闭包是指**函数与其词法环境的组合**，即使函数在其词法环境外执行，也能访问其词法作用域中的变量。

2. **代码解析**：
   ```javascript
   function outer() {
     let count = 0;
     return function inner() {
       count++;
       console.log(count);
     };
   }
   const counter = outer();
   counter(); // 1
   counter(); // 2
   ```
   - `inner`函数形成了闭包，能够访问`outer`函数的`count`变量。

3. **本质**：
   - 闭包的本质是**函数执行时的作用域链**，结合了**AO（活动对象）**和**GO（全局对象）**。
   - 每次函数执行时，会创建一个新的执行上下文，闭包保留了对外部函数作用域的引用。

4. **垃圾回收机制**：
   - 闭包会导致外部函数的变量无法被垃圾回收，即使外部函数执行完毕，只要闭包存在，相关变量仍会保留在内存中。

5. **优缺点**：
   - **优点**：
     - 实现数据私有化，避免全局污染。
     - 支持函数式编程（如柯里化、高阶函数）。
   - **缺点**：
     - 内存泄漏风险（闭包未释放时，外部变量会一直占用内存）。
     - 过度使用可能导致性能问题。

---

### **总结**
闭包是JavaScript中强大的特性，能够访问词法作用域中的变量，但需谨慎使用以避免内存泄漏和性能问题。


## js跨域问题 为什么会出现跨域问题？
跨域问题是由于浏览器的**同源策略**（Same-Origin Policy）限制，阻止网页从一个源（协议、域名、端口）向另一个源发起请求，以防止恶意行为。


## js跨域问题怎么解决？

解决跨域问题的常见方法包括：**CORS（跨域资源共享）**、**JSONP**、**代理服务器**、**WebSocket**、**postMessage**等。

以下是常见的跨域解决方案及其实现方式：

---

### **1. CORS（跨域资源共享）**
- **原理**：服务器设置响应头`Access-Control-Allow-Origin`，允许指定源访问资源。
- **实现**：
  ```javascript
  // 服务器端设置
  res.setHeader('Access-Control-Allow-Origin', '*'); // 允许所有源
  res.setHeader('Access-Control-Allow-Origin', 'https://example.com'); // 允许特定源
  ```

---

### **2. JSONP**
- **原理**：利用`<script>`标签不受同源策略限制的特性，通过动态创建`<script>`标签加载跨域数据。
- **实现**：
  ```javascript
  function handleResponse(data) {
    console.log(data);
  }
  const script = document.createElement('script');
  script.src = 'https://example.com/api?callback=handleResponse';
  document.body.appendChild(script);
  ```

---

### **3. 代理服务器**
- **原理**：通过同源服务器转发请求，绕过浏览器的同源策略。
- **实现**：
  - 前端请求同源服务器：
    ```javascript
    fetch('/api/proxy?url=https://example.com/data');
    ```
  - 服务器端转发请求：
    ```javascript
    app.get('/api/proxy', (req, res) => {
      const url = req.query.url;
      axios.get(url).then(response => res.send(response.data));
    });
    ```

---

### **4. WebSocket**
- **原理**：WebSocket协议不受同源策略限制，支持跨域通信。
- **实现**：
  ```javascript
  const socket = new WebSocket('wss://example.com');
  socket.onmessage = (event) => {
    console.log(event.data);
  };
  ```

---

### **5. postMessage**
- **原理**：通过`window.postMessage`在不同窗口或iframe之间传递数据。
- **实现**：
  ```javascript
  // 发送方
  window.parent.postMessage('Hello', 'https://example.com');

  // 接收方
  window.addEventListener('message', (event) => {
    if (event.origin === 'https://example.com') {
      console.log(event.data); // Hello
    }
  });
  ```

---

### **总结**
- **CORS**：服务器设置响应头。
- **JSONP**：动态创建`<script>`标签。
- **代理服务器**：通过同源服务器转发请求。
- **WebSocket**：使用WebSocket协议通信。
- **postMessage**：通过`postMessage`跨窗口通信。

根据场景选择合适的跨域解决方案。



## 这段代码的输出是什么？      

```javascript
var a = function () {
    this.b = 3;
}
var c = new a();
a.prototype.b = 9;
var b = 7;
a();
console.log(b);
console.log(c.b);
```

这段代码的输出是：

```javascript
console.log(b); // 3
console.log(c.b); // 3
```

---

### **代码解析**
1. **`var a = function () { this.b = 3; }`**：
   - 定义构造函数`a`，当通过`new`调用时，会将`this.b`赋值为`3`。

2. **`var c = new a();`**：
   - 通过`new`调用构造函数`a`，创建一个新对象`c`，此时`c.b`被赋值为`3`。

3. **`a.prototype.b = 9;`**：
   - 在`a`的原型上添加属性`b`并赋值为`9`，但这不会影响已经创建的实例`c`，因为`c`自身已经有属性`b`。

4. **`var b = 7;`**：
   - 在全局作用域中声明变量`b`并赋值为`7`。

5. **`a();`**：
   - 直接调用函数`a`（非`new`调用），此时`this`指向全局对象（浏览器中为`window`），因此全局变量`b`被修改为`3`。

6. **`console.log(b);`**：
   - 输出全局变量`b`，值为`3`（被`a()`调用修改）。

7. **`console.log(c.b);`**：
   - 输出实例`c`的属性`b`，值为`3`（构造函数中直接赋值的优先级高于原型链）。

---

### **总结**
- 全局变量`b`的值为`3`（被`a()`调用修改）。
- 实例`c`的属性`b`的值为`3`，原型上的`b`不会影响已有实例的属性。


## 原型链查找过程吧？

**原型**是JavaScript中实现继承的基础，每个对象都有一个隐式原型（`__proto__`），指向其构造函数的显式原型（`prototype`），通过**原型链**查找属性时，会沿着`__proto__`逐级向上查找，直到找到或到达`null`。