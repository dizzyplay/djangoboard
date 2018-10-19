<template>
  <div id="e3" style="max-width: 600px; margin: auto;" class="grey lighten-3">
    <v-container fluid stype="min-height:0;" grid-list-lg>
      <v-layout row wrap>
        <v-flex xs12>
          <v-card target="_blank" class="black--text">
            <v-layout>
              <v-flex>
                <v-card-title primary-title>
                  <div>
                    <div class="headline">{{id}} - {{title}}</div>
                    <div>
                      {{content}}
                    </div>
                    <div>
                      {{created_at}}
                    </div>
                  </div>
                </v-card-title>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

  </div>
</template>

<script>
  export default {
    props:['id', 'title','content','created_at']
  }
</script>

<style scoped>

</style>
