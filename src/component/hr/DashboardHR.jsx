import React, { Component } from "react";
import "./DashboardHR.css";
import { HashRouter as Router, Route, Link } from "react-router-dom";
import { Switch } from "react-router";
import NavBar from "../NavBar.jsx";
import Attendence from "../Attendence.jsx";
import UploadSquareFeet from "../UploadSquareFeet.jsx";
import UploadAttendence from "../UploadAttendence.jsx";
import UserAccountManage from "../UserAccountManage";
import SalarySlip from "../SalarySlip";
import Salary from "../Salary.jsx";
import MannualAttendence from "../MannualAttendence";
import Employee from "../Employee.jsx";
import Esi from "../Esi.jsx";
import MonthlySalary from "../MonthlySalary.jsx";
import NotFound404 from "../NotFound404.jsx";


import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUsers,
  faRupeeSign,
  faFingerprint,
  faMoneyCheckAlt,
  faUserEdit,
  faFileUpload,
  faFileImport,
  faUserCircle,
  faPrint,
  faEdit,
  faUserShield

} from "@fortawesome/free-solid-svg-icons";



function MannualAttendenceF() {
  return <MannualAttendence />
}


function SalaryF() {
  return <Salary />
}

function SalarySlipF() {
  return <SalarySlip />
}

function EsiF() {
  return <Esi />
}

function UploadSquareFeetF() {
  return <UploadSquareFeet />;
}

function UserAccountManageF() {
  return <UserAccountManage />
}

function UploadAttendenceF() {
  return <UploadAttendence />;
}


function EmployeeTableF() {
  return <Employee />
}

function monthlysalaryF() {
  return <MonthlySalary />;
}

function AttendenceF() {
  return <Attendence />;
}


class DashboardHR extends Component {
  state = {
    redirect: true,
    checked: true
  };
  handleChange = (checked) => {
    console.log("switch");
    // var sidebarV = this.refs.sidebar;
    // var sidebarV = React.findDOMNode( this.refs.sidebar);
    // sidebarV.style.disply="none";

    if (this.state.checked == true) {
      // document.getElementById("sidebar").setAttribute("style", "display:none")
      document.getElementById("sidebar").setAttribute("class", "display-none");
    }
    // document.getElementById("sidebar").setAttribute("style", "display:block");
    else { document.getElementById("sidebar").setAttribute("class", "display-block"); }
    this.setState({ checked });
  }

  render() {
    return (
      <Router>
        {/* <Redirect to='/login'  /> */}

        <div id="outer-main-div">
          <div id="outer-nav">

            <NavBar loginInfo={this.props.data} checked={this.state.checked} handleChange={this.handleChange} onLogout={this.props.onLogout} />

          </div>

          <div id="main-non-nav" style={{ color: "#616161" }}>
            <div id="sidebar" style={{ backgroundColor: "#616161" }} >
              <div id="sidebar-top-content" />
              <div id="main-title">

                <FontAwesomeIcon icon={faUserShield} className="sidebar-icon" />
                {localStorage.getItem("show_role")} {localStorage.getItem("user_name")}


              </div>
              <ul className="navbar-ul">

                <li>
                  <Link to="/hr/employee">
                    <FontAwesomeIcon icon={faUsers} className="sidebar-icon" />
                    Employees
                  </Link>
                </li>



                <li>
                  <Link to="/hr/salary">
                    <FontAwesomeIcon icon={faRupeeSign} className="sidebar-icon" />
                    Salary
                  </Link>
                </li>


                <li>
                  <Link to="/hr/attendence">
                    <FontAwesomeIcon icon={faFingerprint} className="sidebar-icon" />
                    Attendence
                  </Link>
                </li>

                <li>
                  <Link to="/hr/monthlysalary">
                    <FontAwesomeIcon icon={faMoneyCheckAlt} className="sidebar-icon" />
                    Monthly Salary
                  </Link>
                </li>



                <li>
                  <Link to="/hr/editattendence">
                    <FontAwesomeIcon icon={faUserEdit} className="sidebar-icon" />
                    Edit Attendence
                  </Link>
                </li>



                <li>
                  <Link to="/hr/attendenceupload">
                    <FontAwesomeIcon icon={faFileUpload} className="sidebar-icon" />
                    Upload Attendence


                  </Link>
                </li>

                <li>
                  <Link to="/hr/uploadsquarefeet">
                    <FontAwesomeIcon
                      icon={faFileImport}
                      className="sidebar-icon"
                    />
                    Upload Square feet


                  </Link>
                </li>


                <li>
                  <Link to="/hr/useraccountmanage">
                    <FontAwesomeIcon
                      icon={faUserCircle}
                      className="sidebar-icon"
                    />
                    User Accounts


                  </Link>
                </li>

              


                <li>
                  <Link to="/hr/salaryslip">
                    <FontAwesomeIcon
                      icon={faPrint}
                      className="sidebar-icon"
                    />
                    Salary Slip


                  </Link>
                </li>

                <li>
                  <Link to="/hr/percentagesetter">
                    <FontAwesomeIcon
                      icon={faEdit}
                      className="sidebar-icon"
                    />
                    Percentage Setter


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
                  path="/hr/employee"
                  // exact
                  component={EmployeeTableF}
                />
                <Route
                  path="/hr/salary"
                  exact
                  component={SalaryF}
                />

                <Route
                  path="/hr/monthlysalary"
                  // exact
                  component={monthlysalaryF}
                />


                <Route
                  path="/hr/uploadsquarefeet"
                  // exact
                  component={UploadSquareFeetF}
                />

                <Route
                  path="/hr/percentagesetter"
                  // exact
                  component={EsiF}
                />


                <Route
                  path="/hr/useraccountmanage"
                  exact
                  component={UserAccountManageF}
                />
                <Route
                  path="/hr/salaryslip"
                  exact
                  component={SalarySlipF}
                />


                <Route
                  path="/hr/editattendence"
                  exact
                  component={MannualAttendenceF}
                />
                <Route
                  path="/hr/attendenceupload"
                  exact
                  component={UploadAttendenceF}
                />
                <Route
                  path="/hr/attendence"
                  exact
                  component={AttendenceF}
                />

                <Route render={() => <NotFound404 />} />

              </Switch>
            </div>
          </div>
        </div>
      </Router>
    );
  }
}

export default DashboardHR;
