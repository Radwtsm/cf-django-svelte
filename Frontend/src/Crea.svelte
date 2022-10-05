<script>
  import IoIosPerson from "svelte-icons/io/IoIosPerson.svelte";
  import { fade } from "svelte/transition";

  // isInvalidLocation = True -> Comune inserito non valido
  let isInvalidLocation = false;
  // isNuovo = True -> non esiste una persona con questi dati nel db, crea nuova persona e aggiungi al DB
  let isNuovo = false;

  let messaggio;

  //codice fiscale da mostrare
  let codicefinale = "";

  // variabili che contengono dati degli input nel form
  let surname, name, sex, birthplace, birthdate;

  // scelte del dropdown nel campo "sex"
  let sexes = [
    { id: 1, option: "M" },
    { id: 2, option: "F" },
  ];

  let persona = null;

  const onSubmit = async () => {
    // toglie la visualizzazione del cf quando il form effettua un'altro submit
    codicefinale = "";

    //richiesta post alle persone del db
    const res = await fetch("http://127.0.0.1:8000/persone/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // passare i dati del form in json alla richiesta POST
      body: JSON.stringify({
        surname,
        name,
        sex,
        birthplace,
        birthdate,
      }),
    });

    const json = await res.json();

    //stampa dei vari errori in base agli input invalidi
    if (json["messaggio"]) {
      isNuovo = true;

      setTimeout(function () {
        isNuovo = false;
      }, 4000);

      messaggio = json["messaggio"];
      codicefinale = json["codice_fiscale"];
    } else if (json["errore_comune"]) {
      isInvalidLocation = true;

      setTimeout(function () {
        isInvalidLocation = false;
      }, 4000);
    } else if (json["codice_fiscale"]) {
      codicefinale = json["codice_fiscale"];
    }
  };
</script>

<main>
  <form on:submit|preventDefault={onSubmit}>
    <h1>CF Calculator</h1>
    <label for="surname"> <strong> Surname </strong> </label>
    <input
      bind:value={surname}
      id="surname"
      name="surname"
      type="text"
      required
    />

    <label for="name"> <strong> Name </strong> </label>
    <input bind:value={name} id="name" name="name" type="text" required />

    <label for="sex"><strong>Sex</strong></label>

    <select bind:value={sex} name="sex" id="sex">
      {#each sexes as sex}
        <option value={sex.option}>{sex.option}</option>
      {/each}
    </select>

    <label for="birthdate"> <strong> Birthdate </strong> </label>
    <input
      bind:value={birthdate}
      id="birthdate"
      name="birthdate"
      type="date"
      required
    />

    <label for="birthplace"> <strong> Birthplace </strong> </label>

    <input
      bind:value={birthplace}
      id="birthplace"
      name="birthplace"
      type="text"
      required
    />

    <br />

    <!--Rendering condizionale in base agli errori nella risposta json-->
    {#if isInvalidLocation}
      <p id="error" transition:fade={{ duration: 150 }}>Comune non corretto!</p>
    {/if}
    {#if isNuovo}
      <p transition:fade={{ duration: 150 }}>{messaggio}</p>
    {/if}

    {#if codicefinale}
      <p id="cf">{codicefinale}</p>
    {/if}
    <button type="submit">
      <div id="button">
        Calcola <div class="icon"><IoIosPerson /></div>
      </div>
    </button>
  </form>
</main>

<style>
  h1 {
    color: #535bf2;
  }

  select {
    color: gray;
    background-color: white;
    border-radius: 2rem;
    margin: 1rem;
    padding: 2%;
  }

  input {
    color: gray;
    background-color: white;
    border-radius: 2rem;
    margin: 1rem;
    padding: 2%;
  }
  main {
    color: gray;
  }
  form {
    display: flex;
    flex-direction: column;
  }

  #button {
    display: flex;

    align-items: center;
    justify-content: center;
    gap: 2rem;
  }
  .icon {
    width: 3rem;
  }

  button {
    background-color: #535bf2;
    margin-top: 2rem;
    border-width: 0.4rem;
  }

  #error {
    font-size: 1rem;
    color: red;
  }

  #cf {
    color: green;
  }
</style>
