<script setup>
import { ref } from "vue";
let count = ref(0);
const props = defineProps({
    test: String,
});
</script>

<template>
    <div class="container">
        <div class="centerer">
            <div class="box"></div>
            <div class="items">
                <h1>Django + Inertia + Vite + Vue 3!</h1>
                <button class="button" @click="count = count + 1">
                    Count is {{ count }}
                </button>
                <p>
                    This random number was sent from the backend:
                    {{ props.test }}
                </p>
                <h3>Check out the technologies</h3>
            </div>
        </div>
        <h1>Django</h1>
        <p>
            <a href="https://www.djangoproject.com/">Django</a> is Python web
            framework following the model-view-template pattern (essentially the
            same as MVC but using Django's own terminology), and takes care of
            much of the hassle of writing web applications.
        </p>

        <h1>Inertia</h1>
        <p>
            <a href="https://inertiajs.com/">Inertia</a> is a new approach to
            building single-page web apps. It is essentially some 'glue' that
            joins the frontend and the backend together without the need of an
            API. Instead of returning static templates, Inertia allows you to
            return Vue, React or Svelte components directly from the backend!
        </p>

        <h1>Vite</h1>
        <p>
            <a href="https://vitejs.dev/">Vite</a>, which means "quick" in
            French, is a rapid development tool for building web projects. It
            significantly speeds up and improves the frontend development
            experience. Using Hot Module Replacement, Vite can update only the
            parts of the code that have been changed, instead of reloading the
            whole application.
        </p>

        <h1>Vue</h1>
        <p>
            <a href="https://vuejs.org/">Vue</a> is a progressive JavaScript
            frontend framework designed to be flexible. The core Vue library
            focuses on the view layer only, and additional packages are needed
            for features like state management and routing (the latter of which
            is not needed with Inertia).
        </p>
        <p><inertia-link href="/">Back to Home</inertia-link></p>
    </div>
</template>

<style scoped>
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
    display: flex;
    justify-content: center;
    align-items: center;
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