## 6. Javascript中原型链和原型继承是什么？
### 原型链
在 JavaScript 中，每个对象都有一个内部属性 `[[Prototype]]`（在代码中可通过 `__proto__` 访问，不过不推荐直接使用），它指向该对象的原型对象。当访问一个对象的属性或方法时，JavaScript 首先会在该对象本身查找，如果找不到，就会沿着 `[[Prototype]]` 指向的原型对象继续查找，这个原型对象又可能有自己的原型对象，以此类推，直到找到该属性或方法，或者到达原型链的末尾（即 `Object.prototype`），这种查找机制形成的链条就是原型链。

### 原型继承
原型继承是 JavaScript 中实现继承的一种方式，它利用原型链的特性，让一个对象可以继承另一个对象的属性和方法。实现原型继承的基本思路是将子类对象的原型指向父类对象，这样子类对象就可以访问父类对象的属性和方法。常见的实现方式有以下几种：

- **通过原型对象赋值**：直接将子类的 `prototype` 属性设置为父类的实例：
```javascript
function Parent() {
    this.parentProperty = 'parent value';
}
Parent.prototype.parentMethod = function() {
    console.log('This is a parent method');
};

function Child() {}
Child.prototype = new Parent();

const child = new Child();
console.log(child.parentProperty); // 输出: 'parent value'
child.parentMethod(); // 输出: 'This is a parent method'
```
- **使用 `Object.create()`**：该方法会创建一个新对象，使用现有的对象来提供新创建对象的 `[[Prototype]]`：
```javascript
const parent = {
    parentProperty: 'parent value',
    parentMethod() {
        console.log('This is a parent method');
    }
};

const child = Object.create(parent);
console.log(child.parentProperty); // 输出: 'parent value'
child.parentMethod(); // 输出: 'This is a parent method'
```

原型继承的优点是简单直接，能让对象之间共享属性和方法，减少内存开销；缺点是所有实例会共享原型上的引用类型属性，修改一个实例的引用类型属性会影响其他实例。 