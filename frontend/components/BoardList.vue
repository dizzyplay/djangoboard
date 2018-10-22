<template>
  <v-content>
    <v-container fluid>
      <v-card>
      <v-card-title>삽질하는 게시판</v-card-title>
  <v-data-table
    v-bind:headers="headers"
    v-bind:items="blogData"
    class="elevation-1"
    v-bind:expand="true"
  >
    <template slot="items" slot-scope="props">
      <tr v-on:click="props.expanded = !props.expanded">
          <td>{{props.item.id}}</td>
          <td>{{props.item.title}}</td>
          <td>{{props.item.short_date}}</td>
      </tr>
    </template>
    <template slot="expand" slot-scope="props">
      <v-card class="elevation-0">
        <v-card-text>
          <div>
            {{props.item.content}}
          </div>
        </v-card-text>
      </v-card>
    </template>
  </v-data-table>
      </v-card>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    props: ['blogData'],
    data() {
      return {
        headers: [
          {text: '글번호', value: 'id', sortable:false},
          {text: '글제목', value: 'title', sortable: false},
          {text: '날짜', value: 'short_date', sortable: false}
        ],
      }
    },
    computed:{
      posts:{
        get(){
          return this.blogData
        }
      }
    },
    methods:{
      goToPost(postId){
        console.log(`go to ${postId} !!!`)
      }
    }
  }
</script>

<style scoped>

</style>
