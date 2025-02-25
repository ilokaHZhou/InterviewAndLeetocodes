要实现可过期的 `localStorage` 数据，核心思路是在存储数据时同时记录过期时间，在读取数据时检查是否过期，若过期则删除数据。以下是简单的实现步骤和示例代码：

### 实现步骤
1. **存储数据**：存储数据时，将数据和过期时间封装成一个对象，再将该对象转换为 JSON 字符串存入 `localStorage`。
2. **读取数据**：读取数据时，先从 `localStorage` 中获取存储的 JSON 字符串，解析为对象，检查其中的过期时间，若未过期则返回数据，若已过期则删除该数据并返回 `null`。

### 示例代码
```javascript
// 封装设置可过期数据的函数
function setLocalStorageWithExpiry(key, value, expirationMinutes) {
    const now = new Date();
    // 计算过期时间戳
    const expirationTime = now.getTime() + expirationMinutes * 60 * 1000;
    const item = {
        value: value,
        expiration: expirationTime
    };
    // 将对象转换为 JSON 字符串存入 localStorage
    localStorage.setItem(key, JSON.stringify(item));
}

// 封装获取可过期数据的函数
function getLocalStorageWithExpiry(key) {
    const itemStr = localStorage.getItem(key);
    if (!itemStr) {
        return null;
    }
    const item = JSON.parse(itemStr);
    const now = new Date();
    // 检查是否过期
    if (now.getTime() > item.expiration) {
        // 若过期，删除该数据
        localStorage.removeItem(key);
        return null;
    }
    return item.value;
}

// 使用示例
// 设置一个 1 分钟后过期的数据
setLocalStorageWithExpiry('myData', '这是示例数据', 1);
// 获取数据
const data = getLocalStorageWithExpiry('myData');
console.log(data); 
```

### 代码解释
- `setLocalStorageWithExpiry` 函数：接收键、值和过期分钟数作为参数，计算过期时间戳，将数据和过期时间封装成对象，再存入 `localStorage`。
- `getLocalStorageWithExpiry` 函数：接收键作为参数，从 `localStorage` 中获取数据，解析为对象后检查是否过期，根据情况返回数据或 `null`。

通过上述方法，就可以实现 `localStorage` 数据的过期功能。 