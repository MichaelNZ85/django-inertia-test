<script setup>
import { Link } from "@inertiajs/inertia-vue3";
</script>

<template>
    <nav>
        <ul class="navbar">
            <li><Link href="/">Home</Link></li>
            <li><Link href="/events">Events</Link></li>
            <li><Link href="/contact/">Contact</Link></li>
        </ul>
    </nav>
    <div class="containa">
        <slot />
    </div>
</template>


<style scoped>
.containa {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

a {
    color: #880202;
    text-decoration: none;
}

.navbar {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
</style>
