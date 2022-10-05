<script>
    export let persona;
</script>

<div id="container">
    <div id="tag">
        <h2>{persona.surname} {persona.name}</h2>
    </div>

    <ul>
        <li><b>Sesso: </b>{persona.sex}</li>
        <li><b>Data di Nascita: </b>{persona.birthdate}</li>
        <li><b>Luogo di Nascità: </b>{persona.birthplace}</li>
    </ul>
    <p><b>{persona.codice_fiscale}</b></p>
</div>

<style>
    #container {
        border-radius: 2rem;
        padding: 2rem;
        box-shadow: -4px 0px 15px -4px rgba(0, 0, 0, 0.73);
        margin: 2rem;

        color: gray;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    ul {
        list-style-type: none;
    }

    #tag {
        display: flex;
    }

    ul {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }

    h2,
    b {
        color: #535bf2;
    }
</style>
