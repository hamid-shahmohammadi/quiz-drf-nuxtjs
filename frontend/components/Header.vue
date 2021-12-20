<template>
  <div>
      <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div class="container-fluid">
            <NuxtLink to="/" class="navbar-brand" href="#">Queez</NuxtLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav me-auto mb-2 mb-md-0">
                    <li class="nav-item">
                        <NuxtLink to="/" class="nav-link active" aria-current="page" href="#">Home</NuxtLink>
                    </li>
                
                </ul>
                <ul class="navbar-nav mb-2 mb-md-0">
                    <li v-if="!$store.getters['getLoggedIn']" class="nav-item">
                        <NuxtLink to="/login" class="nav-link active" aria-current="page" href="#">Login</NuxtLink>
                    </li>
                     <li v-if="!$store.getters['getLoggedIn']" class="nav-item">
                        <NuxtLink to="/register" class="nav-link active" aria-current="page" href="#">Register</NuxtLink>
                    </li>
                    <li v-if="$store.getters['getLoggedIn']" class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#" @click="logout">Logout</a>
                    </li>
                
                </ul>
               
            </div>
            </div>
        </nav>
      </header>
  </div>
</template>

<script>
export default {
     methods:{
      async logout(){
         await fetch('http://localhost:8000/users/logout',{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                credentials:'include',
               
          });
          this.$nuxt.$emit('auth',false);
          await this.$router.push('/login');
      }
    }

}
</script>

<style>

</style>