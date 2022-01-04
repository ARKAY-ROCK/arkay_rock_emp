import React, { Component } from "react";
import axios from "axios";

import { Form, Button, Col, Row } from "react-bootstrap";

class MonthlySalaryForm extends Component {
  state = {
    employeeData : [],
    
    
  }
 
  loadEmployeeInfo = () => {
    axios
      .get('/get_esi_epf_share')
      .then(response => {
        console.log(response.data);
      
      })
      .catch(error => {
        console.log(error);
      });
  };
  
  componentWillMount() {
    this.loadEmployeeInfo();
    // this.loadPositionInfo();
    // this.loadDepartmentInfo();
  }

  render() {
    return (
      <div>
        <h2 id="role-form-title">Update ESI EPF Shares</h2>
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
                >
                   <option value="" >Select your option</option>
                  {this.state.employeeData.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["basic_pay"]}</option>
                  ))}

                </Form.Control>
              </Col>
            </Form.Group>


             <Form.Group as={Row}>
              <Form.Label column sm={2}>
               demo
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  required
                >

                   
                   

                  {this.state.employeeData.map((data, index) => (

                    <option key={index} value={data["_id"]}>

                    {data["basic_pay"]}
                    </option>


                  ))}

                </Form.Control>
              </Col>
            </Form.Group> 


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
               ESI Employeer Share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  placeholder="share"
              
                  required
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              ESI Employee share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="ESI Employee share"
                  required
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              EPF Employeer Pension
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="EPF Employeer Pension"
                  required
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              EPF Employee
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="EPF Employee"
                  required
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Basic  Pay %
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Basic Pay Percentage"
                  required
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              WL Allowence %
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="WL Allowence"
                  required
                />
              </Col>
            </Form.Group>
           
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              HRA %
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="HRA"
                  required
                />
              </Col>
            </Form.Group>
            
            
                <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Conveyence %
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Conveyence %"
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

export default MonthlySalaryForm;
