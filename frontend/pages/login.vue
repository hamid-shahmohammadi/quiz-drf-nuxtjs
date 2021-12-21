<template>
  <div class="text-center login-area">
      <main class="form-signin">
        <form @submit.prevent="login">
            <!-- <img class="mb-4" src="/docs/5.1/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"> -->
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
            <input v-model="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
            <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
            <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
            <label for="floatingPassword">Password</label>
            </div>

            <div class="checkbox mb-3">
            
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
           
        </form>
        </main>
  </div>
</template>

<script>
export default {
  
  data(){
        return{ 
            email:'',
            password:''
        }
    },
    methods:{
        async login(){
            // var response=await fetch('http://localhost:8000/users/login',{
            //     method:'POST',
            //     headers:{'Content-Type':'application/json'},
            //     credentials:'include',
            //     body:JSON.stringify({   
            //         email:this.email,
            //         password:this.password
            //     })
            // });
            // var data=await response.json()
            // console.log(data.jwt)
            // this.saveJwt(data.jwt)
            // this.$auth.setUser(data.user)
            
            // await this.$router.push('/');

            const data = { 'email': this.email, 'password': this.password }
            console.log(data);
            try{
                const response = await this.$auth.loginWith('local', { data: data})
                console.log(response)
                this.$auth.$storage.setUniversal('email', response.data.email)
                await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)

                await this.$router.push('/');
            } catch(e) {
                console.log(e.message)
            }

           
        },
        saveJwt(jwt){
          this.$store.dispatch('storeJWT', jwt)
        }
    },
    mounted(){
      
    }
}
</script>

<style>
.login-area{
    display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>