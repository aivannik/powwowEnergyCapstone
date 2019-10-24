import React, { Component } from 'react';

// A utility class for Horizontal nav bar
// Can be used across all pages

class HorizontalNav extends Component {
  constructor(props) {
    super(props);
    this.state = {
      menu: false
    };
    this.toggleMenu = this.toggleMenu.bind(this);
  }

  toggleMenu(){
    this.setState({ menu: !this.state.menu })
  }
  render() {

    const show = (this.state.menu) ? "show" : "" ;

    return (
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <a class="navbar-brand" href="#">Space Monitor</a>
      <button class="navbar-toggler" type="button" onClick={ this.toggleMenu }>
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class={"collapse navbar-collapse " + show}>
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">placeholder</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">placeholder</a>
          </li>
        </ul>
      </div>
      <form class="form-inline my-2 my-lg-0">
          <button class="btn btn-outline-success my-2 my-sm-0 mr-2" type="submit">login</button>
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">signup</button>
        </form>
    </nav>
      );
    }
  }

export default HorizontalNav;