<template>
  <div class="container queez-list">
    <div v-if="quiz" class="row row-cols-1 row-cols-md-3 mb-3 text-center">

      <div class="col" v-for="q in quiz" :key="q.id">
        <div class="card mb-4 rounded-3 shadow-sm">
          <div class="card-header py-3">
            <h4 class="my-0 fw-normal">{{q.title}}</h4>
          </div>
          <div class="card-body">
           
            <ul class="list-unstyled mt-3 mb-4">
              <li>{{q.count_questions}} questions</li>
          
            </ul>
            <NuxtLink :to="{path:`/quiz/${q.title}`}" type="button" class="w-100 btn btn-lg btn-outline-primary">Go to quiz</NuxtLink>
          </div>
        </div>
      </div>

      

    </div>

    <div>
      <nav aria-label="Page navigation example">
        <ul class="pagination">
          <li v-if="previousPage" @click.prevent="previousLink()" class="page-item">
            <a class="page-link" href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          
          <li class="page-item">
            <a v-if="nextPage" @click.prevent="nextLink()" class="page-link" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>  
    </div>

  </div>
</template>

<script>
export default {
  middleware: 'auth',
  data(){
    return {
      nextPage:null,
      previousPage:null,
      quiz:[]
    }
  },
  async asyncData({ $axios }) { 
    
  },
  async mounted(){
    var quiz=null   
    const res = await this.$axios.$get('quiz')
    console.log(res)
    
    if(res.next){
      this.nextPage=res.next.slice(22)    
    }
    if(res.previous){
      this.previousPage=res.previous.slice(22)
    }
    this.quiz=res.results
  },
  methods:{
    async nextLink(){
      const res = await this.$axios.$get(this.nextPage)

      console.log(res)
    
      if(res.next){
        this.nextPage=res.next.slice(22)    
      }else{
        this.nextPage=null
      }
      if(res.previous){
        this.previousPage=res.previous.slice(22)
      }else{
        this.previousPage=null
      }
      this.quiz=res.results
    },
    async previousLink(){
      const res = await this.$axios.$get(this.previousPage)

      console.log(res)
    
      if(res.next){
        this.nextPage=res.next.slice(22)    
      }else{
        this.nextPage=null
      }
      if(res.previous){
        this.previousPage=res.previous.slice(22)
      }else{
        this.previousPage=null
      }
      this.quiz=res.results
    }
  }
 
}
</script>
<style scope>
.queez-list{
  margin-top: 80px;
}
</style>
