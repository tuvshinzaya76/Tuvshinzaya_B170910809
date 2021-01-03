<template>
  <div class="row w-100">
    <div class="col-md-5 col-xl-3">
        <!-- Toggle Tasks Navigation on mobile -->
        <button type="button" class="btn btn-block btn-primary d-md-none mb-10" data-toggle="class-toggle" data-target=".js-tasks-nav" data-class="d-none d-md-block">Menu</button>
        <!-- Collapsible Tasks Navigation -->
        <div class="js-tasks-nav d-none d-md-block">
          <!-- Tasks Info -->
          <div class="block block-rounded">
              <div class="block-header block-header-default">
                <h3 class="block-title">Tasks</h3>
              </div>
              <div class="block-content">
                <ul class="list-group push">
                    <li class="list-group-item">
                      <span class="js-task-badge badge badge-primary float-right animated bounceIn">{{countActiveTask}}</span>
                      <i class="fa fa-fw fa-tasks mr-5"></i> Active
                    </li>
                    <li class="list-group-item">
                      <span class="js-task-badge-starred badge badge-warning float-right animated bounceIn">{{countStarredTask}}</span>
                      <i class="fa fa-fw fa-star mr-5"></i> Starred
                    </li>
                    <li class="list-group-item">
                      <span class="js-task-badge-completed badge badge-success float-right animated bounceIn">{{countCompletedTask}}</span>
                      <i class="fa fa-fw fa-check mr-5"></i> Completed
                    </li>
                </ul>
              </div>
          </div>
          <!-- END Tasks Info -->
          <!-- People -->
          <!--div class="block block-rounded">
              <div class="block-header block-header-default">
                <h3 class="block-title">People</h3>
                <div class="block-options">
                    <div class="dropdown">
                      <button type="button" class="btn-block-option" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      <i class="si si-settings"></i>
                      </button>
                      <div class="dropdown-menu dropdown-menu-right">
                          <a class="dropdown-item" href="javascript:void(0)">
                          <i class="fa fa-fw fa-eye mr-5"></i>Make Private
                          </a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:void(0)">
                          <i class="fa fa-fw fa-pencil mr-5"></i>Edit People
                          </a>
                      </div>
                    </div>
                </div>
              </div>
              <div class="block-content">
                <ul class="nav-users push">
                    <li>
                      <a href="be_pages_generic_profile.html">
                          <img class="img-avatar" src="assets/media/avatars/avatar6.jpg" alt="">
                          <i class="fa fa-circle text-success"></i> Lori Moore
                          <div class="font-w400 font-size-xs text-muted"><i class="fa fa-location-arrow"></i> New York</div>
                      </a>
                    </li>
                    <li>
                      <a href="be_pages_generic_profile.html">
                          <img class="img-avatar" src="assets/media/avatars/avatar11.jpg" alt="">
                          <i class="fa fa-circle text-success"></i> Carl Wells
                          <div class="font-w400 font-size-xs text-muted"><i class="fa fa-location-arrow"></i> San Fransisco</div>
                      </a>
                    </li>
                    <li>
                      <a href="be_pages_generic_profile.html">
                          <img class="img-avatar" src="assets/media/avatars/avatar8.jpg" alt="">
                          <i class="fa fa-circle text-warning"></i> Carol White
                          <div class="font-w400 font-size-xs text-muted"><i class="fa fa-location-arrow"></i> Beijing</div>
                      </a>
                    </li>
                    <li>
                      <a href="be_pages_generic_profile.html">
                          <img class="img-avatar" src="assets/media/avatars/avatar11.jpg" alt="">
                          <i class="fa fa-circle text-warning"></i> Wayne Garcia
                          <div class="font-w400 font-size-xs text-muted"><i class="fa fa-location-arrow"></i> Tokyo</div>
                      </a>
                    </li>
                    <li>
                      <a href="be_pages_generic_profile.html">
                          <img class="img-avatar" src="assets/media/avatars/avatar15.jpg" alt="">
                          <i class="fa fa-circle text-danger"></i> Scott Young
                          <div class="font-w400 font-size-xs text-muted"><i class="fa fa-location-arrow"></i> London</div>
                      </a>
                    </li>
                </ul>
                <form class="push" action="be_pages_generic_todo.html" method="post" onsubmit="return false;">
                    <div class="input-group">
                      <input class="form-control" type="text" placeholder="Invite more people..">
                      <div class="input-group-append">
                          <button class="btn btn-secondary" type="submit">
                          <i class="fa fa-plus"></i>
                          </button>
                      </div>
                    </div>
                </form>
              </div>
          </div-->
          <!-- END People -->
        </div>
        <!-- END Collapsible Tasks Navigation -->
    </div>
    <div class="col-md-7 col-xl-9">
        <!-- Tasks -->
        <!-- Tasks functionality is initialized in js/pages/be_pages_generic_todo.min.js which was auto compiled from _es6/pages/be_pages_generic_todo.js -->
        <div class="js-tasks">
          <!-- Add task -->
          <div id="js-task-form">
              <div class="input-group input-group-lg">
                <input class="form-control" type="text" v-model="new_task" @keyup.enter="createNewTask()" id="js-task-input" name="js-task-input" placeholder="Add a task and press enter..">
                <div class="input-group-append">
                    <span class="input-group-text" v-on:click="createNewTask()">
                      <i class="fa fa-plus"></i>
                    </span>
                </div>
              </div>
          </div>
          <!-- END Add task -->
          <!-- Tasks List -->
          <h2 class="content-heading mb-10">Active</h2>
          <div class="js-task-list">
              <Task v-for="(val,index) in task_list" :key="index" v-if="isActiveTask(val)" :task_list="task_list" :task="val">
                <button v-on:click="cancelTask(val)" class="js-task-remove btn btn-sm btn-alt-danger" type="button">
                  <i class="fa fa-times"></i>
                </button>
              </Task>
          </div>
          <!-- END Tasks List -->
          <!-- Starred Tasks List -->
          <h2 class="content-heading mb-10">Starred</h2>
          <div class="js-task-list-starred">
              <Task v-for="(val,index) in task_list" :key="index" v-if="isStarredTask(val)" :task_list="task_list" :task="val">
                <button v-on:click="cancelTask(val)" class="js-task-remove btn btn-sm btn-alt-danger" type="button">
                  <i class="fa fa-times"></i>
                </button>
              </Task>
              <!-- Task -->
              <!-- END Task -->
          </div>
          <!-- END Starred Tasks List -->

          <!-- Tasks List Completed -->
          <h2 class="content-heading mb-10">Completed</h2>
          <div class="js-task-list-completed">
            <Task v-for="(val,index) in task_list" :key="index" v-if="isCompletedTask(val)" :task_list="task_list" :task="val">
                <button v-on:click="cancelTask(val)" class="js-task-remove btn btn-sm btn-alt-danger" type="button">
                  <i class="fa fa-times"></i>
                </button>
            </Task>
              <!-- END Completed Task -->
          </div>
          <!-- END Tasks List Completed -->
        </div>
        <!-- END Tasks -->
    </div>
  </div>
</template>
<script>
import Task from './Task'
export default {
  name: 'todo',
  props: ['task_list'],
  components:{  Task,  },
  created(){
  },
  data () {
    return {
      new_task:"",
    }
  },
  computed:{
    countActiveTask: function(){
      let count = 0;
      this.task_list.map(el=>{
        if(this.isActiveTask(el)){
          count++;
        }
      });
      return count;
    },
    countStarredTask: function(){
      let count = 0;
      this.task_list.map(el=>{
        if(this.isStarredTask(el)){
          count++;
        }
      });
      return count;
    },
    countCompletedTask:function(){
      let count = 0;
      this.task_list.map(el=>{
        if(this.isCompletedTask(el)){
          count++;
        }
      });
      return count;
    }
  },
  methods:{
    cancelTask: function(el){
      this.task_list.map((task,index)=>{
        if(el.text == task.text){
           this.task_list.splice(index, 1);
        }
      });
    },
    isActiveTask: function(task){
      return !task.active && !task.starred;
    },
    isStarredTask: function(task){
      return !task.active && task.starred;
    },
    isCompletedTask: function(task){
      return task.active;
    },
    createNewTask: function(){
      this.task_list.push( {
          starred: false,
          completed: false,
          active: false,
          text: this.new_task,
      });
      this.new_task = "";
    }
  }
}
</script>
