<template>
  <div>
    <v-toolbar>
      <v-toolbar-title>Trade Actions</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">User Profile</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field label="Legal first name*" required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Legal middle name"
                    hint="example of helper text only on focus"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    label="Legal last name*"
                    hint="example of persistent helper text"
                    persistent-hint
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="Email*" required></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field label="Password*" type="password" required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-select :items="['0-17', '18-29', '30-54', '54+']" label="Age*" required></v-select>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-autocomplete
                    :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                    label="Interests"
                    multiple
                  ></v-autocomplete>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-toolbar>
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
              <v-row>Trade Total</v-row>
              <v-row class="underlying">${{trade.trade_total}}</v-row>
            </v-col>
            <v-col :md="2" :sm="4">
              <v-row align="right">Trade Status</v-row>
              <v-row>
                <v-chip color="green" text-color="white" label>{{trade.status_display}}</v-chip>
              </v-row>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-spacer></v-spacer>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>Details</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-data-table :headers="headers" :items="trade.trade_set" class="elevation-1">
              <template v-slot:top>
                <v-toolbar>
                  <v-toolbar-title>Trade Actions</v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-dialog v-model="dialog" max-width="500px">
                    <template v-slot:activator="{ on }">
                      <v-btn color="primary" v-on="on">New Trade Action</v-btn>
                    </template>
                    <v-card>
                      <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.action_executed_date"
                                label="Action Executed Data"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field v-model="editedItem.amount" label="Amount ($)"></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field v-model="editedItem.action_type" label="Action Type"></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                        <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
                <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
              </template>
              <template v-slot:no-data>
                <v-btn color="primary" @click="initialize">Reset</v-btn>
              </template>
            </v-data-table>
          </v-expansion-panel-content>
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
      loading: true,
      dialog: false,
      headers: [
        {
          text: "Action Type",
          align: "start",
          sortable: false,
          value: "action_type_display"
        },
        { text: "Action Executed Date", value: "action_executed_date" },
        { text: "Amount ($)", value: "amount" },
        { text: "Actions", value: "actions", sortable: false }
      ],
      editedIndex: -1,
      editedItem: {
        action_executed_date: "",
        amount: 0,
        action_type: ""
      }
    };
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Trade Action" : "Edit Trade Action";
    }
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
    },
    editItem(item) {
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
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