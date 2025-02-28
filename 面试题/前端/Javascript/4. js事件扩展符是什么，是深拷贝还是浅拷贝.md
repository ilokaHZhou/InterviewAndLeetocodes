JavaScript中的**扩展运算符（Spread Operator）**是`...`，用于展开数组、对象或函数参数。

---

### **1. 扩展运算符的作用**
- **数组**：展开数组元素。
  ```javascript
  const arr1 = [1, 2, 3];
  const arr2 = [...arr1]; // 展开数组
  ```
- **对象**：展开对象属性。
  ```javascript
  const obj1 = { a: 1, b: 2 };
  const obj2 = { ...obj1 }; // 展开对象
  ```
- **函数参数**：将数组展开为函数参数。
  ```javascript
  function sum(a, b, c) { return a + b + c; }
  const nums = [1, 2, 3];
  sum(...nums); // 展开为 sum(1, 2, 3)
  ```

---

### **2. 深拷贝还是浅拷贝？**
- **数组和对象的扩展运算符是浅拷贝**：
  - 只复制第一层属性，嵌套的引用类型（如对象、数组）仍然是共享的。
  ```javascript
  const obj1 = { a: 1, b: { c: 2 } };
  const obj2 = { ...obj1 };
  obj2.b.c = 3;
  console.log(obj1.b.c); // 3（共享嵌套对象）
  ```

- **实现深拷贝**：需要结合其他方法，如`JSON.parse(JSON.stringify())`或递归拷贝。

---

### **总结**
扩展运算符`...`是**浅拷贝**，适用于展开数组、对象或函数参数，但嵌套的引用类型仍然是共享的。