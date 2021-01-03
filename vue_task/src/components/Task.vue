<template>
  <div class="js-task block block-rounded mb-5 animated fadeIn" data-task-id="6" data-task-completed="false" data-task-starred="false">
    <table class="table table-borderless table-vcenter mb-0">
        <tbody>
          <tr>
              <td class="text-center" style="width: 50px;">
                <label class="js-task-status css-control css-control-primary css-checkbox py-0">
                <input type="checkbox" class="css-control-input" v-model="task.active">
                <span class="css-control-indicator"></span>
                </label>
              </td>
              <td v-if="task.active" class="js-task-content font-w600">
                  <del>{{task.text}}</del>
              </td>
              <td v-else class="js-task-content font-w600">
                  {{task.text}}
              </td>
              <td class="text-right" style="width: 100px;">
                <button v-on:click="task.starred =! task.starred" class="js-task-star btn btn-sm btn-alt-warning" type="button">
                  <i class="fa" v-bind:class="task.starred? 'fa-star':' fa-star-o'"></i>
                </button>
                <slot>
                </slot>
              </td>
          </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
export default {
  name: 'task',
  props: ['task_list','task'],
  created(){
  },
  data () {
    return {

    }
  },
  methods:{

  }
}
</script>
