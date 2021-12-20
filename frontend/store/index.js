export const state = () => ({
    jwt: '',
    user:{},
    loggedIn:false
  })
  
  export const mutations = {
    STORE_JWT(state, jwt) {
      state.jwt = jwt
      state.loggedIn=true
    },
    STORE_USER(state,user){
        state.user=user
        state.loggedIn=true

    }
  }
  
  export const actions = {
    storeJWT({commit}, jwt) {
      commit('STORE_JWT', jwt)
    },
    storeUser({commit},user){
        commit('STORE_USER',user)
    }
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