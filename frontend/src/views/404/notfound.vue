<template>
<div class="app">
    <img src="@/assets/robot.png"/>

    <div class="text">
        <p style="font-size:45px;">NOT FOUND</p>
        <button @click="repath" class="back_btn">GO BACK</button>

    </div>
</div>
</template>

<script>
import Button from '../../components/button/Button.vue'
export default {
  components: { Button },
    
    data(){
        return{

        }
    },
    methods:{
        repath: function(){
            this.$router.push("Home")
        }
    }
}
</script>

<style lang="scss" scoped>
.app{
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;


    .text{
        text-align: center;
        color: #353b3e;
    }
    
    .back_btn{
        width: 100px;
        height: 40px;
        background-color: rgb(86, 86, 240);
        border: none;
        border-radius: 5px;
        color:  white;
    }

    img{
        width: 500px;
        height: 500px;
    }
}

</style>