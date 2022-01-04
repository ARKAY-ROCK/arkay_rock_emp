import React, { Component } from "react";
import "./DashboardHR.css";
import { HashRouter as Router, Route, Link } from "react-router-dom";
import { Switch } from "react-router";
import { Redirect } from "react-router-dom";
import Role from "./Role.jsx";
import NavBar from "../NavBar.jsx";
import RoleForm from "./RoleForm.jsx";
import Position from "./Position.jsx";
import Department from "./Department.jsx";
import Country from "./Country.jsx";
import State from "./State.jsx";
import City from "./City.jsx";
import Company from "./Company.jsx";
import Attendence from "./Attendence.jsx";


import Employee from "./Employee.jsx";

import Salary from "./Salary.jsx";
import Esi from "../Esi.jsx";

import MonthlySalary from "./MonthlySalary.jsx";

import LeaveApplicationHR from "./LeaveApplicationHR.jsx";
import NotFound404 from "../NotFound404.jsx";


import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUsers,
  faChair,
  faBuilding,
 faUser,
faUserTie,
faRupeeSign,
faFileAlt,
faCity,
faGlobeAmericas,
faPlaceOfWorship,
faArchway,
} from "@fortawesome/free-solid-svg-icons";

function RoleHRF() {
  return <Role />;
}



function PositionF() {
  return <Position />;
}
function DepartmentF() {
  return <Department />;
}
function CountryF() {
  return <Country />;
}
function StateF() {
  return <State />;
}
function CityF() {
  return <Esi />;
}
function CompanyF() {
  return <Company />;
}
function EmployeeF() {
  return <Employee />;
}
function SalaryF() {
  return <Salary />;
}


function monthlysalaryF() {
  return <MonthlySalary />;
}

function LeaveApplicationHRF() {
  return <Attendence />;
}

// function HRPortalF() {
//   return <HRPortal />;
// }
// function HRProjectBidF() {
//   return <HRProjectBid />;
// }

class DashboardHRroll extends Component {
  state = {
    redirect: true,
    checked: true 
  };
  handleChange=(checked)=> {
    console.log("switch");
    // var sidebarV = this.refs.sidebar;
    // var sidebarV = React.findDOMNode( this.refs.sidebar);
    // sidebarV.style.disply="none";
    
    if(this.state.checked==true){ 
       // document.getElementById("sidebar").setAttribute("style", "display:none")
      document.getElementById("sidebar").setAttribute("class", "display-none");
    }
    // document.getElementById("sidebar").setAttribute("style", "display:block");
    else{document.getElementById("sidebar").setAttribute("class", "display-block");}   
    this.setState({ checked });
  }

  render() {
    return (
      <Router>
        {/* <Redirect to='/login'  /> */}

        <div id="outer-main-div">
          <div id="outer-nav">
            {/* <NavBar loginInfo={this.props.data} /> */}
            <NavBar loginInfo={this.props.data} checked={this.state.checked} handleChange={this.handleChange} onLogout={this.props.onLogout}/>

          </div>

          <div id="main-non-nav" style={{color:"#616161"}}>
            <div id="sidebar" style={{backgroundColor:"#616161"}} >
              <div id="sidebar-top-content" />
              <div id="main-title">
                
                <FontAwesomeIcon icon={faUserTie} className="sidebar-icon" />
               Admin Rollonly 
                
                
              </div>
              <ul className="navbar-ul">
                <li>
                  <Link to="/roll/employee">

                    <FontAwesomeIcon icon={faUser} className="sidebar-icon" /> 
                    Employees
                
                
                  </Link> 
                </li>

                <li>
                  <Link to="/roll/salary">
                    <FontAwesomeIcon icon={faRupeeSign} className="sidebar-icon" /> 
                    Salary 
                
                  </Link> 
                </li>


                  <li>
                  <Link to="/roll/monthlysalary">
                    <FontAwesomeIcon icon={faRupeeSign} className="sidebar-icon" /> 
                    Monthly Salary 
                
                  </Link> 
                </li>



                <li>
                  <Link to="/roll/attendence">
                    <FontAwesomeIcon icon={faFileAlt} className="sidebar-icon" /> 
                    Attendence 
                
                
                  </Link> 
                </li>
                
                <li>
                  <Link to="/roll/city">
                    <FontAwesomeIcon icon={faUsers} className="sidebar-icon" /> 
                    ESI
                
                
                  </Link> 
                </li>
                
                <li>
                  <Link to="/roll/department">
                    <FontAwesomeIcon
                      icon={faBuilding}
                      className="sidebar-icon"
                    /> 
                    Department 
                
                
                  </Link> 
                </li>
              
                
                
                <li>
                 
                </li>
                {/* <li> <a href=""><FontAwesomeIcon icon={faChair} className="sidebar-icon"/> Position</a>   </li> */}
                {/* <li> <a href=""><FontAwesomeIcon icon={faBuilding} className="sidebar-icon"/> Department</a>   </li> */}
                {/* <li> <a href=""><FontAwesomeIcon icon={faDollarSign} className="sidebar-icon"/> Project Bidding</a>   </li> */}
                {/* <li> <a href=""><FontAwesomeIcon icon={faTasks} className="sidebar-icon"/> Portal Master</a>   </li> */}
              </ul>
            </div>
            {/* <div id="sidebar-top-content" /> */}
            <div id="main-area">
              <div id="sidebar-top-content" />
              {/* //table */}
              {/* <RoleHR/> */}
              <Switch>
                <Route
                  path="/roll/employee"
                  // exact
                  component={EmployeeF}
                />
                <Route
                  path="/roll/salary"
                  exact
                  component={SalaryF}
                />

                <Route
                  path="/roll/monthlysalary"
                  // exact
                  component={monthlysalaryF}
                />

                <Route
                  path="/roll/company"
                  exact
                  component={CompanyF}
                />
                <Route path="/hr/role" component={RoleHRF} />
                {/* <Route path="/hr/role/form" exact component={RoleFormF} /> */}
                <Route
                  path="/roll/position"
                  exact
                  component={PositionF}
                />
                <Route
                  path="/roll/department"
                  exact
                  component={DepartmentF}
                />
                
                <Route
                  path="/roll/country"
                  exact
                  component={CountryF}
                />


                
                <Route
                  path="/roll/state"
                  exact
                  component={StateF}
                />
                <Route
                  path="/roll/city"
                  exact
                  component={CityF}
                />
                <Route
                  path="/roll/attendence"
                  exact
                  component={LeaveApplicationHRF}
                />
                 {/* <Route
                  path="/hr/portal-master"
                  exact
                  component={HRPortalF}
                /> */}
                 {/* <Route
                  path="/hr/project-bid"
                  exact
                  component={HRProjectBidF}
                /> */}
                {/* <Route
                  exact
                  path="/hr"
                  render={() => <Redirect to="hr/employee" />}
                /> */}
                <Route render={() => <NotFound404/>} />
                
              </Switch>
            </div>
          </div>
        </div>
      </Router>
    );
  }
}

export default DashboardHRroll;
