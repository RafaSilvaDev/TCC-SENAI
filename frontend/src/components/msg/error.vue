<template>
    <Message v-for="msg of messages" :severity="msg.severity" :key="msg.content">{{msg.content}}</Message>
</template>
<script>
import Message from 'primevue/message';

export default{
    data(){
        return{ 
        messages: [
			{severity: 'info', content: 'Dynamic Info Message'},
			{severity: 'success', content: 'Dynamic Success Message'},
			{severity: 'warn', content: 'Dynamic Warning Message'},
            {severity: 'error', content: 'Dynamic Error Message'}
		]
        }
    },
    components: {
    Message,
    }
}


</script>
