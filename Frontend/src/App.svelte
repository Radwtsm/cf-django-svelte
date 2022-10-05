<script>
  import IoMdHome from "svelte-icons/io/IoMdHome.svelte";
  import IoIosAddCircle from "svelte-icons/io/IoIosAddCircle.svelte";

  import Crea from "./Crea.svelte";
  import { Router, Route, Link } from "svelte-routing";

  import Persone from "./Persone.svelte";

  export let url = "";
</script>

<h1>ciao</h1>
<Router {url}>
  <nav>
    <Link to="/"><div class="icon"><IoMdHome /></div></Link>
    <Link to="crea"><div class="icon"><IoIosAddCircle /></div></Link>
  </nav>
  <div>
    <Route path="/"><Persone /></Route>
    <Route path="crea"><Crea /></Route>
  </div>
</Router>

<style>
  nav {
    display: flex;
    gap: 3rem;
    justify-content: center;
    align-items: center;
  }

  .icon {
    width: 3rem;
  }
</style>
