import React, { Component } from "react";
// import { Provider } from "react-redux";

import Header from "./components/layout/Nav";
import Dashboard from "./components/leads/Dashboard";

class App extends Component {
  render() {
    return (
      <>
        <Header />
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <Dashboard />
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default App;
