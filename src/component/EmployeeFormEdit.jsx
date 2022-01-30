import React, { Component } from "react";
import "./EmployeeFormEdit.css";
import axios from "axios";
import { Form, Button, Col, Row } from "react-bootstrap";

class EmployeeFormEdit extends Component {
  state = {
    roleData: [],
    positionData: [],
    departmentData: [],
    GenderData: this.props.editData["Gender"],

  //  EmailData: this.props.editData["Email"],
   // PasswordData: "",

    FirstNameData: this.props.editData["FirstName"],
    MiddleNameData: this.props.editData["MiddleName"],
    LastNameData: this.props.editData["LastName"],
    DOBData: this.props.editData["DOB"],
    ContactNoData: this.props.editData["ContactNo"],
    EmployeeCodeData: this.props.editData["EmployeeCode"],
    RoleData: this.props.editData["role"],
    positionData: this.props.editData["position"],
    departmentData: this.props.editData["department"],
    DateOfJoiningData: this.props.editData["DateOfJoining"],
    TerminateDateData: this.props.editData["TerminateDate"],
    EmailData: this.props.editData["Email"],
    BloodgroupData: this.props.editData["Bloodgroup"],
    EmergencyContactData: this.props.editData["EmergencyContact"],
    ESIData : this.props.editData['ESINumber'],
    EPFData : this.props.editData['EPFNumber']

    // value={this.state.EmployeeTitleData}
    // onChange={value => this.onEmployeeTitleDataChange(value)}
  };
  onEmailDataChange(e) {
    this.setState({ EmailData: e.target.value });
  }

  onFirstNameDataChange(e) {
    this.setState({ FirstNameData: e.target.value });
  }
  onMiddleNameDataChange(e) {
    this.setState({ MiddleNameData: e.target.value });
  }
  onLastNameDataChange(e) {
    this.setState({ LastNameData: e.target.value });
  }
  onContactNoDataChange(e) {
    this.setState({ ContactNoData: e.target.value });
  }
  onEmployeeCodeDataChange(e) {
    this.setState({ EmployeeCodeData: e.target.value });
  }
  onPasswordDataChange(e) {
    this.setState({ PasswordData: e.target.value });
  }
  
   onroleChange(e) {
    this.setState({ RoleData: e.target.value });
  }
   onpositionChange(e) {
    this.setState({ positionData: e.target.value });
  }
   ondepartmentChange(e) {
    this.setState({ departmentData: e.target.value });
  }
  


 onBloodgroupDataChange(e){
  
  this.setState({BloodgroupData: e.target.value});
  
 }

onEmailDataChange(e){

this.setState({EmailData: e.target.value});

}

onEmergencyContactDataChange(e){
this.setState({EmergencyContactData: e.target.value});

}

onESIDataChange(e){
  this.setState({ESIData: e.target.value});
  
  }


  onEPFDataChange(e){
    this.setState({EPFData: e.target.value});
    
    }

  onGenderChange = e => {
    this.setState({ GenderData: e.target.value });
    this.props.onGenderChange(e);
  };
  onDOBDataChange = e => {
    console.log(e.target.value);
    this.setState({ DOBData: e.target.value });
  };
  onDateOfJoiningDataChange = e => {
    console.log(e.target.value);
    this.setState({ DateOfJoiningData: e.target.value });
  };
  onTerminateDateDataChange = e => {
    console.log(e.target.value);
    this.setState({ TerminateDateData: e.target.value });
  };
  onGenderChange = e => {
    this.setState({ GenderData: e.target.value });
    this.props.onGenderChange(e);
  };
 
  render() {
    return (
      <React.Fragment>
        <h2 id="role-form-title">Edit Employee Details</h2>
        <div id="role-form-outer-div">
          <Form
            id="form"
            onSubmit={e =>
              this.props.onEmployeeEditUpdate(this.props.editData, e)
            }
          >
          
    
     <Form.Group as={Row}>
              <Form.Label column sm={2}>
                First Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="First Name"
                  required
                  value={this.state.FirstNameData}
                  disabled={true}
                  onChange={value => this.onFirstNameDataChange(value)}
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
                  value={this.state.MiddleNameData}
                  onChange={value => this.onMiddleNameDataChange(value)}
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
                  disabled={true}
                  value={this.state.LastNameData}
                  onChange={value => this.onLastNameDataChange(value)}
                />
              </Col>
            </Form.Group>



  <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Role
              </Form.Label>
             <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Role"
                  required
                  
                  
                        value={this.state.RoleData}
                  onChange={value => this.onroleChange(value)}
                  
                />
              </Col>

            </Form.Group>
            
            
              <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Blood group
              </Form.Label>
             <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Blood group"
                  required
                  
                  
                        value={this.state.BloodgroupData}
                  onChange={value => this.onBloodgroupDataChange(value)}
                  
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
                  placeholder="Email"
                  required
                  
                  
                        value={this.state.EmailData}
                  onChange={value => this.onEmailDataChange(value)}
                  
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
                  placeholder="Emergency Contact"
                  required
                  
                  
                        value={this.state.EmergencyContactData}
                  onChange={value => this.onEmergencyContactDataChange(value)}
                  
                />
              </Col>

            </Form.Group>
            
           
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                DOB
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="DOB"
                  required
                  //   value={this.props.editData["DOB"].slice(0, 10)}
                  value={this.state.DOBData}
                  onChange={value => this.onDOBDataChange(value)}
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
                  value={this.state.ContactNoData}
                  onChange={value => this.onContactNoDataChange(value)}
                />
              </Col>
            </Form.Group>
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Employee Code
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Employee Code"
                  required
                  disabled={true}
                  value={this.state.EmployeeCodeData}
                  onChange={value => this.onEmployeeCodeDataChange(value)}
                />
              </Col>
            </Form.Group>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Department
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Department"
                  required
                  value={this.state.departmentData}
                  onChange={value => this.ondepartmentChange(value)}
                />
              </Col>
            </Form.Group>





            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Position
              </Form.Label>
              <Col sm={10} className="form-input">
             <Form.Control
                  type="text"
                  placeholder="position"
                  required
                  value={this.state.positionData}
                  onChange={value => this.onpositionChange(value)}
                />
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
                  //   value={this.props.editData["DateOfJoining"].slice(0, 10)}
                  value={this.state.DateOfJoiningData}
                  onChange={value => this.onDateOfJoiningDataChange(value)}
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
                  //   value={this.props.editData["TerminateDate"].slice(0, 10)}
                  value={this.state.TerminateDateData}
                  onChange={value => this.onTerminateDateDataChange(value)}
                />
              </Col>
            </Form.Group>

            
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                ESI Number 
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  placeholder="1 to not detect"
                  //   value={this.props.editData["TerminateDate"].slice(0, 10)}
                  value={this.state.ESIData}
                  onChange={value => this.onESIDataChange(value)}
                />
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                EPF Number
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  placeholder="1 to not detect"
                  //   value={this.props.editData["TerminateDate"].slice(0, 10)}
                  value={this.state.EPFData}
                  onChange={value => this.onEPFDataChange(value)}
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
                  onChange={this.onGenderChange}
                  checked={this.state.GenderData == "male"}
                  required
                />
                <Form.Check
                  inline
                  type="radio"
                  label="Female"
                  value="female"
                  name="gender"
                  onChange={this.onGenderChange}
                  checked={this.state.GenderData == "female"}
                  required
                />
              </Col>
            </Form.Group>
            
            

            <Form.Group as={Row} id="form-submit-button">
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit">Submit</Button>
              </Col>
            </Form.Group>
            <Form.Group as={Row} id="form-cancel-button">
              <Col sm={{ span: 10, offset: 2 }} id="form-cancel-button-inner">
                <Button type="reset" onClick={this.props.onFormEditClose}>
                  cancel
                </Button>
              </Col>
            </Form.Group>
          </Form>
        </div>
      </React.Fragment>
    );
  }
}

export default EmployeeFormEdit;
