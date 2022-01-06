import React, { Component } from "react";
import axios from "axios";

import { Form, Button, Col, Row } from "react-bootstrap";

class UserAccountManage extends Component {
  state = {
    employeeData: [],
    employeeMonth: [],
    employeeYear: [],
    employee_name: "",
    name: "NA",
    department: "NA",
    month: "",
    username_info : "",
    year: "",
    sqtft: "",
    username: "",
    role : "",
    password: "",


  }

  loadEmployeeInfo = () => {
    axios
      .get('/employee_list')
      .then(response => {
        this.setState({ employeeData: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };


  loadMonth = () => {
    axios
      .get('/salary_month')
      .then(response => {
        this.setState({ employeeMonth: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };

  loaduseraccounts = () => {
    axios
      .get('/active_user_details')
      .then(response => {
        this.setState({ employeeMonth: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };

  check_user = () => {
    axios
      .put('/check_user_account',{'user_name':this.state.username})
      .then(response => {
        console.log(response.data);
        if (response.data == '1'){
          alert('user already exist')
        }
      })
      .catch(error => {
        console.log(error);
      });
  }

  loadYear = () => {
    axios
      .get('/salary_year')
      .then(response => {
        this.setState({ employeeYear: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };

  componentWillMount() {
    this.loadEmployeeInfo();
    this.loaduseraccounts();
    this.loadYear();

    // this.loadPositionInfo();
    // this.loadDepartmentInfo();
  }


  async postemployeename(e) {
    console.log(e.target.value);
    this.setState({ employee_name: e.target.value });
    await axios
      .put('/get_selected_employee_details', { 'employee_name': e.target.value, 'month': this.state.month, 'year': this.state.year })
      .then(response => {
        //this.setState({ employeeYear: response.data });
        console.log(response.data['department']);
        console.log(response.data[0]['department']);
        this.setState({ name: response.data[0]['employee_name'] });
        this.setState({ department: response.data[0]['department'] });

      })
      .catch(error => {
        console.log(error);
      });

  }

 async onusername(e) {
   await this.setState({ username: e.target.value });
   this.check_user();
  }

  onuserrole(e) {
    this.setState({role : e.target.value });
  }

  onuserpassword(e) {
    this.setState({password : e.target.value });
  }

  async onmonthchange(e) {
    console.log(e.target.value);
   await  this.setState({ username_info: e.target.value });
    axios
    .put('/reterive_user_info', { user_name: this.state.username_info})
    .then(response => {
      //this.setState({ employeeYear: response.data });
      console.log(response.data['password']);
      this.setState({name:response.data['user_name'] + " - " +response.data['role'] });
      this.setState({department: response.data['password']})

      
    })
    .catch(error => {
      console.log(error);
    });
  }




  onsqtchange(e) {
    this.setState({ sqtft: e.target.value });
  }


reterive_info () {
  console.log("craete user pressed ");
    axios
      .put('/reterive_user_info', { 'username': this.state.username})
      .then(response => {
        //this.setState({ employeeYear: response.data });
        console.log(response.data);
        window.alert(response.data);
      })
      .catch(error => {
        console.log(error);
      });
}

  create_user() {
    console.log("craete user pressed ");

    if (this.state.username != "" && this.state.password != "" && this.state.role != ""){
      axios
      .put('/create_user_account', { 'username': this.state.username, 'role': this.state.role, 'password': this.state.password})
      .then(response => {
        //this.setState({ employeeYear: response.data });
        console.log(response.data);
        window.alert(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    }

   else{
     alert("Data error")
   }

    
  }



  render() {
    return (
      <div>
        <h2 id="role-form-title">User Account Manage</h2>
        <div id="role-form-outer-div">
          <Form id="form" onSubmit={this.props.onSalarySubmit}>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Select Employee
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  required
                  onChange={value => this.onmonthchange(value)}
                >
                  <option value="" disabled selected>Select User</option>
                  {this.state.employeeMonth.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["users"]}</option>
                  ))}
                </Form.Control>
              </Col>
            </Form.Group>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                User Name
              </Form.Label>
              <Col sm={10} className="form-input">

                <Form.Control
                  type="text"
                  placeholder="username"
                  required
                  onChange={value => this.onusername(value)}
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                User Role
              </Form.Label>
              <Col sm={10} className="form-input">

                <Form.Control
                  type="text"
                  placeholder="admin/user"
                  required
                  onChange={value => this.onuserrole(value)}
                />

              </Col>
            </Form.Group>







            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                User Password
              </Form.Label>
              <Col sm={10} className="form-input">

                <Form.Control
                  type="text"
                  placeholder="password"
                  required
                  onChange={value => this.onuserpassword(value)}
                />

              </Col>
            </Form.Group>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                User Name : Role
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  disabled
                  type="text" 
                  value={this.state.name}

                />
              </Col>
            </Form.Group>

            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Password
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  disabled
                  type="text"
                  placeholder="NA"
                  value={this.state.department}
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row} id="form-submit-button">
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit" onClick={() => this.create_user()} >create User</Button>
              </Col>
            </Form.Group>
            <Form.Group as={Row} id="form-cancel-button">
              <Col sm={{ span: 10, offset: 2 }} id="form-cancel-button-inner">
                <Button type="reset" onClick={this.props.onFormClose}>
                  cancel
                </Button>
              </Col>
            </Form.Group>
          </Form>


        </div>

        {/* </div>
        </div> */}
      </div>
    );
  }
}

export default UserAccountManage;
