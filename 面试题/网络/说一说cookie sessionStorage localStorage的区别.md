`cookie`、`sessionStorage` 和 `localStorage` 都是前端用于存储数据的方式，它们的区别如下：

### 数据生命周期
- **cookie**：可设置过期时间，若未设置，会话结束（浏览器关闭）时失效。
- **sessionStorage**：仅在当前会话期间有效，关闭页面或浏览器窗口数据即清除。
- **localStorage**：除非手动清除，否则数据不会过期。

### 数据存储大小
- **cookie**：一般单个 `cookie` 存储数据不能超过 4KB，过多使用会影响性能。
- **sessionStorage**：通常支持 5MB 左右的数据存储。
- **localStorage**：和 `sessionStorage` 类似，大约支持 5MB 存储容量。

### 数据传输
- **cookie**：会随 HTTP 请求发送到服务器端，在客户端和服务器间来回传递，可能带来额外的流量和安全风险。
- **sessionStorage**：仅在客户端存储，不会随请求发送到服务器。
- **localStorage**：同样只在客户端存储，不参与与服务器的数据传输。

### 访问权限
- **cookie**：在同源的不同窗口和页面间共享，可通过 `document.cookie` 操作。
- **sessionStorage**：数据是会话级别的，不同窗口或标签页（即使同源）间数据不共享。
- **localStorage**：在同源的所有窗口和页面间共享数据。

### 使用场景
- **cookie**：常用于身份验证、记录用户偏好等需要在客户端和服务器间传递数据的场景。
- **sessionStorage**：适合临时保存同一窗口（或标签页）的数据，在关闭窗口或标签页后无需保留的情况。
- **localStorage**：可用于长期保存数据，如缓存一些不常更新的信息，减少重复请求。 