import React, { useState, useEffect } from 'react';

// 定义组件的 props 类型
interface CounterProps {
    initialCount: number;
}

// 定义组件
const Counter: React.FC<CounterProps> = ({ initialCount }) => {
    // 使用 useState 来管理状态
    const [count, setCount] = useState(initialCount);

    // 使用 useEffect 来处理副作用
    useEffect(() => {
        // 组件挂载时执行的代码
        console.log('Component is mounted');

        // 返回一个清理函数，在组件卸载时执行
        return () => {
            console.log('Component is unmounted');
        };
    }, []); // 空依赖数组表示只在组件挂载和卸载时执行

    // 另一个 useEffect 用于监听 count 的变化
    useEffect(() => {
        console.log(`Count has changed to: ${count}`);
    }, [count]); // 依赖数组包含 count，表示 count 变化时执行

    // 定义增加计数的函数
    const increment = () => {
        setCount(count + 1);
    };

    // 定义减少计数的函数
    const decrement = () => {
        setCount(count - 1);
    };

    return (
        <div>
            <h1>Counter: {count}</h1>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
        </div>
    );
};

export default Counter;