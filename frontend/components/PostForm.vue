<template>
  <v-card style="max-width: 600px;" class="mx-auto">
    <v-system-bar
      color="blue darken-4"
      dark
    >
      <v-spacer></v-spacer>
    </v-system-bar>
    <v-toolbar
      color="blue grey accent-4"
      cards
      dark
      flat
    >
      <v-card-title class="title font-weight-regular">글쓰기</v-card-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-form ref="form" v-model="form" class="pa-3 pt-4" v-on:submit.prevent>
      <v-text-field
        v-model="title"
        :rules="[rules.required, rules.length(3)]"
        label="제목"
        outline
      ></v-text-field>
      <v-textarea
        v-model="content"
        :rules="[rules.length(2), rules.required]"
        label="내용"
        outline
      ></v-textarea>
      <v-btn
        :disabled="!form"
        :loading="isLoading"
        v-on:click="submit"
      >글쓰기</v-btn>
    </v-form>
  </v-card>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        title: '',
        content: '',
        form: false,
        isLoading: false,
        rules: {
          length: len => v => (v || '').length >= len || ` ${len}자 이상 입력해주세요`,
          required: v => !!v || '입력해주세요'
        },
      }
    },
    methods:{
      // submit(){
      //   if(this.form){
      //     console.log('ok')
      //     axios.post(`http://localhost:8000/blog/api/`,{
      //       title: this.title,
      //       content: this.content,
      //     }).then(res =>{
      //       console.log(res)
      //     })
      //       .catch(err =>{
      //         console.log(err)
      //       })
      //   }
      // }
      async submit() {
        this.isLoading=true;
        let res = await axios.post(`http://localhost:8000/blog/api/`, {
          title: this.title,
          content: this.content,
        })
        console.log(res.status)
        if (res.status === 201) {
          console.log('성공')

          this.title = '';
          this.content='';
          this.isLoading = false;
          window.location.reload(true)
        }
      }
    }
  }
</script>

<style scoped>

</style>
