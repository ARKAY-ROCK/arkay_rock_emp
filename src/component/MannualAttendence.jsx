import React, { Component } from "react";
import axios from "axios";

import { Form, Container, Table, Button, Col, Row } from "react-bootstrap";

class MannualAttendence extends Component {
  state = {
    employeeData: [],
    employeeMonth: [],
    employeeYear: [],
    employee_name: "",
    name: "",
    month: "",
    year: "",
    date: "",
    department: "Cutting",
    in_time: "",
    out_time: "",
    advance: " ",
    over_time: "",
    delay: "",
    present: "",
    absent: "",
    over_all_ot: "",
    new_date : "",
    new_in_time : "",
    new_out_time : "",
    new_advance : "",
    new_delay : "",
    new_over_time : ""
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


  get_overall_present_absent_monthly = () => {
    axios
      .put('/get_overall_present_absent_overtime', {
        employee_name: this.state.name,
        month: this.state.month,
        year: this.state.year
      })
      .then(response => {
        console.log(response.data.overtime);
        console.log(response.data.present_day);
        this.setState({ over_all_ot: response.data.overtime });
        this.setState({ present: response.data.present_day });
        this.setState({ absent: response.data.absent_day })
      })
      .catch(error => {
        console.log(error);
      });
  }


 async onDateChenge(e) {

   await this.setState({date: e.target.value});
    console.log(this.state.date)

  await  axios
      .put('/get_selected_day_details', {
        employee_name: this.state.name,
        date: this.state.date,
      })
      .then(response => {
        console.log(response.data);
       
        this.setState({ in_time: response.data.in_time });
        this.setState({ out_time: response.data.out_time });
        this.setState({ delay: response.data.delay });
        this.setState({ advance: response.data.advance });
        this.setState({ over_time: response.data.overtime })
      })
      .catch(error => {
        console.log(error);
      });
  }

  componentWillMount() {
    this.loadEmployeeInfo();
    this.loadMonth();
    this.loadYear();
  }


  onempnamechange(e) {
    this.setState({ name: e.target.value });
  }
  onmonthchange(e) {
    this.setState({ month: e.target.value });
  }

  onyearchange(e) {
    this.setState({ year: e.target.value });
  }


  in_timechange = (e) => {
    this.setState({new_in_time : e.target.value}) 
  }
  out_timechange =(e) => {
    console.log(e.target.value)
    this.setState({new_out_time : e.target.value}) 
  }

  over_timechange = (e) => {
    this.setState({new_over_time : e.target.value}) 
  }
advance_timechange = (e) => {
  this.setState({new_advance : e.target.value}) 
}

delay_timechange = (e) => {
  this.setState({new_delay : e.target.value}) 
}

addAttendenceDetails = () => {
  console.log("updateAttendenceDetails");

  axios
  .put('/add_mannual_attendence_new', {
    employee_name : this.state.name,
    date: this.state.date,
    in_time: this.state.new_in_time,
    out_time: this.state.new_out_time,
    delay : this.state.new_delay,
    advance : this.state.new_advance,
    overtime : this.state.new_over_time
  })
  .then(response => {
   if (response.data == 'success') {
     alert('attendence added')
   }
   if (response.data == 'error') {
    alert('Error ')
  }
  
  })
  .catch(error => {
    console.log(error);
  });

}


  render() {
    return (
      <div>
        <h2 id="role-form-title">Mannual Attendence :  &nbsp;  &nbsp; {this.state.date}</h2>
        <div id="role-form-outer-div">

          <Container>
            <Row>
              <Col>
                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      as="select"
                      required
                      onChange={value => this.onempnamechange(value)}
                    >
                      <option value="" disabled selected> Employee</option>
                      {this.state.employeeData.map((data, index) => (

                        <option key={index} value={data["_id"]}>{data["employee_name"]}</option>
                      ))}
                    </Form.Control>
                  </Col>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      as="select"
                      required
                      onChange={value => this.onmonthchange(value)}
                    >
                      <option value="" disabled selected>Select Month</option>
                      {this.state.employeeMonth.map((data, index) => (

                        <option key={index} value={data["_id"]}>{data["month"]}</option>
                      ))}
                    </Form.Control>
                  </Col>
                </Form.Group>

              </Col>
              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      as="select"
                      required
                      onChange={value => this.onyearchange(value)}

                    >
                      <option value="" disabled selected>Select Year</option>
                      {this.state.employeeYear.map((data, index) => (

                        <option key={index} value={data["_id"]}>{data["year"]}</option>
                      ))}
                    </Form.Control>
                  </Col>
                </Form.Group>

              </Col>

              <Col>
                <Form.Group as={Row}>
                  <Form.Label column sm={2}>

                  </Form.Label>
                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="date"
                      placeholder="Date Of Joining"
                      required
                      onChange={value => this.onDateChenge(value)}
                    />
                  </Col>
                </Form.Group>
              </Col>

              <Col>
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10, offset: 2 }}>
                    <Button type="submit" onClick={this.get_overall_present_absent_monthly} >GET</Button>
                  </Col>
                </Form.Group>
              </Col>

            </Row>
          </Container>

          <Container>
            <Row>
              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="text"
                      placeholder="In Time"
                      required
                      onChange={this.in_timechange}
                    />
                  </Col>

                </Form.Group>

              </Col>
              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="text"
                      placeholder="Out Time"
                      required
                      onChange={this.out_timechange}
                    />
                  </Col>

                </Form.Group>

              </Col>
              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="text"
                      placeholder="Over Time"
                      required
                      onChange={this.over_timechange}
                    />
                  </Col>

                </Form.Group>

              </Col>

              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="text"
                      placeholder="Advance"
                      required
                      onChange={this.advance_timechange}
                    />
                  </Col>

                </Form.Group>

              </Col>
              <Col>

                <Form.Group as={Row}>

                  <Col sm={10} className="form-input">
                    <Form.Control
                      type="text"
                      placeholder="Delay"
                      required
                      onChange={this.delay_timechange}
                    />
                  </Col>

                </Form.Group>

              </Col>


              <Col>
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10, offset: 2 }}>
                    <Button type="submit" onClick={this.addAttendenceDetails} >ADD</Button>
                  </Col>
                </Form.Group>
              </Col>

            </Row>
          </Container>

          <br />

          <Container>
            <Table >
              <thead>

              </thead>
              <tbody>
                <tr>

                  <td>Present Days</td>
                  <td> :  &nbsp;  &nbsp; {this.state.present}</td>

                </tr>
                <tr>

                  <td>Over All OT</td>
                  <td> :  &nbsp;  &nbsp; {this.state.over_all_ot}</td>

                </tr>

                <tr>

                  <td>Absent Days</td>
                  <td> :  &nbsp;  &nbsp; {this.state.absent}</td>

                </tr>
                <tr>

                  <td>In Time</td>
                  <td> :  &nbsp;  &nbsp; {this.state.in_time}</td>

                </tr>
                <tr>

                  <td>Out Time</td>
                  <td> :  &nbsp;  &nbsp; {this.state.out_time}</td>

                </tr>
                <tr>

                  <td>Delay</td>
                  <td> :  &nbsp;  &nbsp; {this.state.delay}</td>

                </tr>
                <tr>

                  <td>Advance</td>
                  <td> :  &nbsp;  &nbsp; {this.state.advance}</td>

                </tr>
                <tr>

                  <td>Over Time</td>
                  <td>  :  &nbsp;  &nbsp; {this.state.over_time}</td>

                </tr>

              </tbody>
            </Table>
          </Container>





        </div>

        {/* </div>
        </div> */}
      </div>
    );
  }
}

export default MannualAttendence;
