<template>
  <div>
    <v-container fluid v-for="trade in tradeData" :key="trade.id">
      <v-card>
        <v-card-text>
          <v-row align="start">
            <v-col :md="2" :sm="4">
              <v-row class="underlying">{{trade.underlying.ticker_symbol}}</v-row>
              <v-row class="execdate">Opened: {{formatDate(trade.trade_executed_date)}}</v-row>
            </v-col>
            <v-col :md="2" :sm="4">
              <v-row>Strategy</v-row>
              <v-row class="strategy">{{trade.strategy_name}}</v-row>
            </v-col>
            <v-col :md="2" :sm="4">
              <v-row>Trade Status</v-row>
              <v-row>
                <v-chip color="green" text-color="white" label>{{trade.status_display}}</v-chip>
              </v-row>
            </v-col>
            <v-col :md="2" :sm="4">
              <v-row>Trade Total</v-row>
              <v-row class="underlying">${{trade.trade_total}}</v-row>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-spacer></v-spacer>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>Details</v-expansion-panel-header>
          <v-expansion-panel-content
            v-for="trade_action in trade.trade_set"
            :key="trade_action.id"
          >{{trade_action.action_type}}</v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
import api from "../services/api";
export default {
  name: "Trades",
  data() {
    return {
      tradeData: null,
      loading: true
    };
  },
  methods: {
    getTradeData() {
      api
        .getTradeData()
        .then(data => {
          this.tradeData = data;
        })
        .catch(error => console.log(error))
        .finally(() => {
          this.loading = false;
        });
    },
    formatDate(dateString) {
      let dt = new Date(dateString);
      let options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
      };
      return dt.toLocaleDateString("en-US", options);
    }
  },
  beforeMount() {
    this.getTradeData();
  }
};
</script>

<style scoped>
.underlying {
  font-size: 22pt;
  color: white;
  font-weight: bolder;
}

.strategy {
  font-size: 14pt;
  color: white;
  font-weight: bolder;
}

.execdate {
  font-size: 7pt;
  color: lightblue;
}
</style>