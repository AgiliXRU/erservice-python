<template>
    <header>
    <nav>
      <ul>
        <li class="nav-item">
          <router-link to="/" exact>Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/inbound" exact>Inbound Patients</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/beds" exact>Show beds</router-link>
        </li>
      </ul>
    </nav>
    </header>
  <main>
    <router-view />
  </main>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.nav-item {
  display: inline-block;
  padding: 5px 10px;
  font-size: 22px;
}
</style>
