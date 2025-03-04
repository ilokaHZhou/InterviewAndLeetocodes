<template>
    <div>
      <p>原始数字: {{ num }}</p>
      <p>计算后的数字: {{ squaredNum }}</p>
      <button @click="increment">增加数字</button>
    </div>
  </template>
  
  <script>
  export default {
    // data 选项，用于定义组件的数据
    data() {
      return {
        num: 0
      };
    },
    // computed 选项，用于定义计算属性
    computed: {
      squaredNum() {
        return this.num * this.num;
      }
    },
    // methods 选项，用于定义组件的方法
    methods: {
      increment() {
        this.num++;
      }
    },
    // watch 选项，用于监听数据的变化
    watch: {
      num(newValue, oldValue) {
        console.log(`数字从 ${oldValue} 变成了 ${newValue}`);
      }
    }
  };
  </script>