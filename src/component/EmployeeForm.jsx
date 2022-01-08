import React, { Component } from "react";
import axios from "axios";

import { Form, Button, Col, Row } from "react-bootstrap";

class EmployeeForm extends Component {
  state = {
    emp_exist: "",
    emp_code : false,
    roleData: [],
    positionData: [],
    departmentData: [],

  }


  check_employee_exist = (e) => {

    console.log(e.target.value);

    axios
      .put("/check_employee_exist", {emp_code : e.target.value})
      .then(res => {
        
        console.log(res.data);
      
        if (res.data == 'exist' ){
          alert('Employee Code Exist')
          this.setState({emp_code:false})
        }
        if ( res.data == 'length'){
         
          this.setState({emp_code:false})
        }
        if ( res.data == 'user not exist'){
         
          this.setState({emp_code:true})
        }

      })
      .catch(err => {
        console.log(err);
      });


  }

  render() {
    return (
      <div>
        <h2 id="role-form-title">Add Employee </h2>
        <div id="role-form-outer-div">
          <Form id="form" onSubmit={this.props.onEmployeeSubmit}>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                First Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="First Name"
                  required
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Middle Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Middle Name"
                  required
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Last Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Last Name"

                  required
                />
              </Col>
            </Form.Group>

            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Email
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="email"
                  required
                />
              </Col>
            </Form.Group>

            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Employee Type
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  type="text"
                  placeholder="Employee Type"
                  required
                >

                  <option value="roll">Role</option>
                  <option value="unroll">UnRoll</option>

                </Form.Control>
              </Col>
            </Form.Group>




            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                DOB
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="date"
                  placeholder="DOB"
                  required
                />
              </Col>
            </Form.Group>
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Contact No
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Contact No "

                  required
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Emergency Contact
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Emergency contact"
                  required
                />
              </Col>

            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Blood Group
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="Blood group"
                  placeholder="Blood group"
                  required
                />
              </Col>

            </Form.Group>

            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Employee Code
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  onChange={this.check_employee_exist}
                  placeholder="Employee Code"
                  required
                />
              </Col>
            </Form.Group>

            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Department
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  type="text"
                  placeholder="Department"
                  required
                >

                  <option value="admin">Admin</option>
                  <option value="admin_prof">Admin Prof</option>
                  <option value="purchase_team">Purchase</option>
                  <option value="main_cutting">Main Cutting</option>
                  <option value="edge_cutting">Edge Cutting</option>
                  <option value="dry_cutting">Dry Cutting</option>
                  <option value="bed_polish">Bed Polish</option>
                  <option value="hand_polish">Hand Polish</option>
                  <option value="carving">Carving</option>
                  <option value="packing">Packing</option>
                  <option value="electrical_maintanence">Electrical Maintanence</option>
                  <option value="mechanical_maintanence">Mechanical Maintanence</option>
                  <option value="cleaning">Cleaning </option>
                  <option value="driver">Driver</option>

                </Form.Control>
              </Col>
            </Form.Group>




            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Position
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  as="select"
                  placeholder="Position"
                  required
                >
                  <option value="administration">Administration</option>
                  <option value="admin Prof">Administration Senior</option>
                  <option value="supervisor">Supervisor</option>
                  <option value="incharge">Incharge</option>
                  <option value="contractor">Contractors</option>
                  <option value="operator">Operator</option>
                  <option value="helper">Helper</option>

                </Form.Control>

              </Col>
            </Form.Group>





            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Date Of Joining
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="date"
                  placeholder="Date Of Joining"
                  required
                />
              </Col>
            </Form.Group>
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Terminate Date
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="date"
                  placeholder="Terminate Date"
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                ESI
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="ESI Number = 1 to not detect"

                  required
                />
              </Col>
            </Form.Group>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                EPF
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="EPF Number = 1 to not detect"

                  required
                />
              </Col>
            </Form.Group>



            <Form.Group as={Row}>
              <Form.Label as="legend" column sm={2}>
                Gender
              </Form.Label>
              <Col sm={10}>
                <Form.Check
                  inline
                  type="radio"
                  label="Male"
                  value="male"
                  name="gender"
                  onChange={this.props.onGenderChange}
                  required
                />
                <Form.Check
                  inline
                  type="radio"
                  label="Female"
                  value="female"
                  name="gender"
                  onChange={this.props.onGenderChange}
                  required
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row} id="form-submit-button">
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit" disabled={!this.state.emp_code}> Submit</Button>
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

export default EmployeeForm;
