export const state = () => ({
    jwt: '',
    user:{},
    loggedIn:false
  })
  
  export const mutations = {
    STORE_JWT(state, jwt) {
      state.jwt = jwt
      state.loggedIn=true
      localStorage.setItem("loggedIn",true)
      
    },
    STORE_USER(state,user){
        state.user=user
        state.loggedIn=true
        localStorage.setItem("loggedIn",true)
        
        localStorage.setItem("user",user)
        

    },
    REMOVE_USER(state){
        state.user=null
        state.loggedIn=false
        state.jwt=''
        localStorage.setItem("loggedIn",false)
        localStorage.setItem("user",null)
    }
  }
  
  export const actions = {
    storeJWT({commit}, jwt) {
      commit('STORE_JWT', jwt)
    },
    storeUser({commit},user){
        commit('STORE_USER',user)
    },
    removeUser({commit}){
        commit('REMOVE_USER')
    },

  }
  
  export const getters = {
    getJWT(state) {
      return state.JWT
    },
    getUser(state){
        return state.user
    },
    getLoggedIn(state){
        return state.loggedIn
    }
  }