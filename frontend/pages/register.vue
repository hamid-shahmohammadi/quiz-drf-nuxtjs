<template>
  <div class="text-center login-area">
      <main class="form-signin">
        <form @submit.prevent="register">
            <!-- <img class="mb-4" src="/docs/5.1/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"> -->
            <h1 class="h3 mb-3 fw-normal">Please Register</h1>

            <div class="form-floating">
                <input v-model="name" class="form-control" id="floatingInput" placeholder="name">
                <label for="floatingInput">Name</label>
            </div>
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
        return {
            name:'',
            email:'',
            password:''
        }
    },
    methods:{
        async register(){
            await fetch('http://localhost:8000/users/register',{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify({
                    name:this.name,
                    email:this.email,
                    password:this.password
                })
            });
            await this.$router.push('/login');
        }
    }

}
</script>

<style>
.login-area{
  margin-top: 60px;
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