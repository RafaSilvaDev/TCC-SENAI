<template>
<div class="app">
    <img src="@/assets/img/robot.png"/>

    <div class="text">
        <p style="font-size:45px;">NOT FOUND</p>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{

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

    img{
        width: 500px;
        height: 500px;
    }
}

</style>
