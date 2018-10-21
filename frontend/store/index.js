import Vuex from 'vuex'
import axios from 'axios'


const createStore = () => {
  return new Vuex.Store({
    state:{
      blogData: undefined,
    },
    mutations:{
      async getData(state) {
        let {data} = await axios.get('http://211.114.88.77/blog/api')
        state.blogData = data
     }
    }
  })
}

export default createStore
