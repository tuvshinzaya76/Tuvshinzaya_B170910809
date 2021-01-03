<template>
  <div id="app">
    <Todo :task_list="task_list"></Todo>
  </div>
</template>

<script>
import Todo from './components/Todo'
export default {
  name: 'app',
  components:{
    Todo,
  },
  data () {
    return {
      task_list:[
        {
          starred: false,
          completed: false,
          active: false,
          text: "Mobile wireframes",
        },
        {
          starred: false,
          completed: false,
          active: false,
          text: "Mobile wireframes 1",
        },
        {
          starred: false,
          completed: false,
          active: false,
          text: "Mobile wireframes 2",
        },
      ],
    }
  }
}
</script>

<style>
@import '/src/css/codebase.css';
@import '/src/css/codebase.min.css';

</style>
