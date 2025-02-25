## JS变量类型检测怎么做？
JavaScript变量类型检测主要有以下几种方法：

---

### **1. `typeof`**
- **用途**：检测基本数据类型。
- **特点**：
  - 对`null`返回`"object"`（历史遗留问题）。
  - 对函数返回`"function"`。
- **示例**：
  ```javascript
  typeof 42; // "number"
  typeof "hello"; // "string"
  typeof null; // "object"
  typeof function() {}; // "function"
  ```

---

### **2. `instanceof`**
- **用途**：检测对象是否为某个构造函数的实例。
- **特点**：适用于引用类型（如数组、对象）。
- **示例**：
  ```javascript
  [] instanceof Array; // true
  {} instanceof Object; // true
  ```

---

### **3. `Object.prototype.toString.call()`**
- **用途**：精确检测所有数据类型。
- **特点**：返回`[object Type]`格式的字符串。
- **示例**：
  ```javascript
  Object.prototype.toString.call(42); // "[object Number]"
  Object.prototype.toString.call([]); // "[object Array]"
  Object.prototype.toString.call(null); // "[object Null]"
  ```

---

### **总结**
- **基本类型**：用`typeof`。
- **引用类型**：用`instanceof`。
- **精确检测**：用`Object.prototype.toString.call()`。

