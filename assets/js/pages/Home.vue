<script setup>
import { ref } from "vue";
let count = ref(0);
const props = defineProps({
    messages: Array,
});
let message = ref("");
let author = ref("");

const handleClick = () => {
    if (message.value.length > 0) {
        alert("Meow!" + message.value);
    }
};
</script>

<template>
    <div class="container">
        <div class="centerer">
            <div class="box">
                <div class="items">
                    <div
                        class="message-root"
                        v-for="message in props.messages"
                        :key="message.created_at"
                    >
                        <span class="message">{{ message.content }}</span>
                        <span class="author">{{ message.author }}</span>
                    </div>
                </div>
            </div>
        </div>
        <div style="display: flex; gap: 10px">
            <input type="text" v-model="message" placeholder="Enter message" />
            <input type="text" v-model="author" placeholder="your name" />
            <button type="button" @click="handleClick">Meow</button>
        </div>
    </div>
</template>

<style scoped>
.message-root {
    padding: 5px;
    margin-top: 5px;
    margin-bottom: 5px;
    width: 100%;
    border: 1px solid #880202;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.message {
    font-size: 1rem;
    color: #0055ff;
    font-weight: bold;
}
.author {
    font-size: 0.8rem;
    color: #333;
    font-style: italic;
}
.container {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    padding: 20px;
    max-width: 960px;
}
.centerer {
    display: flex;
    justify-content: center;
    width: 100%;
}
.box {
    height: 80vh;
    width: 40vw;
}
.items {
    display: flex;
    flex-direction: column;
    align-items: center;
}
h1 {
    font-family: Helvetica, Arial, sans-serif;
}
p {
    font-family: Arial, sans-serif;
    font-size: 1rem;
}
a {
    font-family: Helvetica, Arial, sans-serif;
    font-weight: lighter;
    color: #880202;
    text-decoration: none;
}
a:visited {
    color: #880202;
    text-decoration: none;
}
a:hover {
    color: #20b3ff;
}
</style>