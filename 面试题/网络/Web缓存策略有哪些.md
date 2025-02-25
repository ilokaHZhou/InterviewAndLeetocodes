## Web缓存策略有哪些？
### 内存缓存
在内存中用变量或对象存储数据，读写快但页面刷新或关闭后数据丢失。如：
```javascript
const cache = {};
function getData(key) {
  if (cache[key]) return cache[key];
  const data = fetchData(); 
  cache[key] = data;
  return data;
}
```

### 本地存储缓存
- **localStorage**：可长期存储数据，除非手动删除。
```javascript
localStorage.setItem('key', JSON.stringify(data));
const cachedData = JSON.parse(localStorage.getItem('key'));
```
- **sessionStorage**：数据在会话期间有效，关闭窗口即清除。用法同 `localStorage`。

### IndexedDB
适合存储大量结构化数据，支持事务操作。如打开数据库、存储和读取数据：
```javascript
const request = indexedDB.open('db', 1);
request.onsuccess = (e) => {
  const db = e.target.result;
  const tx = db.transaction('store', 'readwrite');
  const store = tx.objectStore('store');
  store.put({ id: 1, data: 'value' });
  const getReq = store.get(1);
  getReq.onsuccess = (ev) => console.log(ev.target.result);
};
```

### Service Worker 缓存
拦截网络请求，可实现离线缓存和资源缓存。如安装时缓存资源、拦截请求优先从缓存取：
```javascript
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('cache-v1').then(cache => cache.addAll(['/','/index.html'])));
});
self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then(resp => resp || fetch(e.request)));
});
``` 

