<template>
  
</template>

<script>
export default {
    data(){
        return {
            q_title:null
        }
    },
    mounted(){
        console.log(this.$route.params.name)
        this.q_title=this.$route.params.name       
    }
}
</script>

<style>

</style>