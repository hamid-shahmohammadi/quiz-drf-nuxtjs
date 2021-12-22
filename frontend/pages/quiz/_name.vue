<template>
  <div class="question mt-5">
      <h1>{{q}}</h1>
      <div>
        <form @submit.prevent="submit">
            <div v-for="a in answers" :key="a.id" class="form-check">
            <input v-model="answer_select[a.id]" class="form-check-input" type="checkbox" :value="a.id" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
                {{a.answer_text}}
            </label>
            </div>
            <button type="submit" class="btn btn-primary">Answer</button>
        </form>
      </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            q:null,
            answers:[],
            answer_select:[],
            ac:null
        }
    },
    async mounted(){
       
        this.q_title=this.$route.params.name;
        
       
        const res = await this.$axios.$get('quiz/r/'+this.q_title)
        this.question=res
        
        
            const a=res.flatMap((q)=>q.answer)
            const q=res.flatMap((q)=>q.title)
            this.ac=a.length
            
            
          
            
            this.q=q[0]
            this.answers=a
        this.question=res.results
    },
    methods:{
        submit(){
            var ll_arr=[]
            this.answers.forEach((val,index)=>{
                if(this.answer_select[val.id]==true){
                    ll_arr.push(true)
                }else{
                    ll_arr.push(false)
                }
            })
            console.log(ll_arr)

            var z=Object.values(this.answer_select);

            let n=this.answers.map((obj)=>obj.is_right)
           console.log(n)

            let ch=n.every((val,index)=>val===ll_arr[index])
            console.log(ch)
       
        }
    }
}
</script>

<style>
.question{
   display: flex;
	flex-direction: column;
	flex-wrap: nowrap;
	justify-content: center;
	align-items: center;
	align-content: flex-start;
}
</style>