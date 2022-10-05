<script lang="ts">
    import Card from "./lib/Card.svelte";
    import { onMount } from "svelte";

    let listaPersone = [];

    onMount(() => {
        fetch("http://127.0.0.1:8000/persone/")
            .then((response) => response.json())
            .then((data) => (listaPersone = data));
    });
</script>

{#each listaPersone as persona (persona.id)}
    <Card {persona} />
{/each}
