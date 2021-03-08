<template>
  <div class="hello">
    <a href="/tables">Tabless</a>
    <list>
        <!-- <li v-for="t of tables">
            {t}
        </li> -->
        {{tables}}
    </list>
  </div>
</template>

<script>
export default {
  name: 'Tables',
  data() {return{
        tables: [
          "yo",
        ]
    }},
  created() {
      this.tables.push("Hey")
      this.tables.push("You")
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
