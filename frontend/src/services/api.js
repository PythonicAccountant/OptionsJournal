// api.js
import axios from "axios";
const HTTP = axios.create({
  baseURL: "http://127.0.0.1:8181/api/v1"
});

export default {
  getTradeData() {
    return HTTP.get("/trades").then(response => response.data);
  }
};
