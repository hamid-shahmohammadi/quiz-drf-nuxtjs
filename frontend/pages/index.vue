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
            <button type="button" class="w-100 btn btn-lg btn-outline-primary">Go to quiz</button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  middleware: 'auth',
  async asyncData({ $axios }) {    
    const quiz = await $axios.$get('quiz')
    console.log(quiz)
    return { quiz }
  },
  async mounted(){
    
    
  },
  methods:{
    
  }
 
}
</script>
<style scope>
.queez-list{
  margin-top: 80px;
}
</style>
