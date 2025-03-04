// 定义一个函数，该函数返回一个 Promise 对象
function fetchData() {
    return new Promise((resolve, reject) => {
        // 模拟异步操作，比如网络请求
        setTimeout(() => {
            const isSuccess = Math.random() > 0.5;
            if (isSuccess) {
                // 操作成功，调用 resolve 并传递成功的数据
                resolve('数据获取成功');
            } else {
                // 操作失败，调用 reject 并传递错误信息
                reject(new Error('数据获取失败'));
            }
        }, 2000);
    });
}

// 调用 fetchData 函数，并处理 Promise 的结果
fetchData()
   .then((data) => {
        // 当 Promise 状态变为 resolved 时执行这里的代码
        console.log(data);
    })
   .catch((error) => {
        // 当 Promise 状态变为 rejected 时执行这里的代码
        console.error(error.message);
    });