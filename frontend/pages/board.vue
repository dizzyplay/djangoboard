<template>
  <div class="container">
    <BoardList v-bind:blogData="blogData"/>
  </div>
</template>

<script>
  import BoardList from '../components/BoardList'
  export default {
    components:{
      BoardList,
    },
    computed:{
      blogData(){
        return this.$store.state.blogData
      }
    },
    created(){
      this.$store.dispatch('getBlogData')
    }
  }
</script>

<style scoped>

</style>
