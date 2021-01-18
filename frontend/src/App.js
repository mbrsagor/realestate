import React, { Component } from "react";
import { Provider } from "react-redux";

import Header from "./components/layout/Header";
import Dashboard from "./components/leads/Dashboard";
import store from "./store/store";

class App extends Component {
  render() {
    return (
      <>
        <Provider store={store}>
          <Header />
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <Dashboard />
              </div>
            </div>
          </div>
        </Provider>
      </>
    );
  }
}

export default App;
