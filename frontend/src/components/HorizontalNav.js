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
    <nav className="navbar navbar-expand-sm navbar-light bg-light">
      <a className="navbar-brand" href="#">Space Monitor</a>
      <button className="navbar-toggler" type="button" onClick={ this.toggleMenu }>
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className={"collapse navbar-collapse " + show}>
        <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
          <li className="nav-item active">
            <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">placeholder</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">placeholder</a>
          </li>
        </ul>
      </div>
      <form className="form-inline my-2 my-lg-0">
          <button className="btn btn-outline-success my-2 my-sm-0 mr-2" type="submit">login</button>
          <button className="btn btn-outline-success my-2 my-sm-0" type="submit">signup</button>
        </form>
    </nav>
      );
    }
  }

export default HorizontalNav;