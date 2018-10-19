<template>
  <div>
    <div v-for="(post, index) in listData" v-bind:key="index">
      <Card
        v-bind:id="post.id"
        v-bind:title="post.title"
        v-bind:content="post.content"
        v-bind:created_at="post.created_at"
      />
    </div>
  </div>
</template>

<script>
  import axios from "axios"
  import Card from "../components/Card"

  export default {
    components:{
      Card
    },
    async asyncData(){
      let {data} = await axios.get(`http://211.114.88.77/blog/api/`)
      return { listData: data}
    }

  }
</script>

<style scoped>

</style>
