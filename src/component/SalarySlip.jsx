import React, { Component } from "react";
import axios from "axios";
import { Form, Button, Col, Row } from "react-bootstrap";
import html2canvas from "html2canvas";
import { jsPDF } from "jspdf";

class SalarySlip extends Component {
  state = {
    employeeData: [],
    employeeMonth: [],
    employeeYear: [],
    employee_name: "",
    name: "NA",
    department: "NA",
    month: "",
    year: "",
    sqtft: ""


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

  componentWillMount() {
    this.loadEmployeeInfo();
    this.loadMonth();
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


  onmonthchange(e) {
    this.setState({ month: e.target.value });
  }


  onyearchange(e) {
    this.setState({ year: e.target.value });
  }

  onsqtchange(e) {
    this.setState({ sqtft: e.target.value });
  }


  downloadPdfDocument = (ele, file_name) => {

    var doc = jsPDF('p', 'px', 'letter');

    doc.html(ele.toString(), {
      callback: function (doc) {
        doc.save(file_name);
      }
    });

  }



  async salaryslip_download() {
    console.log("salary download pressed");
    await axios
      .put('/salary_slip_download', { 'employee_name': this.state.employee_name, 'month': this.state.month, 'year': this.state.year })
      .then(response => {
        this.downloadPdfDocument(response.data, this.state.employee_name + "_" + this.state.month + "_" + this.state.year + "_salary_slip.pdf");

      })
      .catch(error => {
        console.log(error);
      });
  }



  render() {
    return (
      <div>
        <h2 id="role-form-title">Salary Slip Download</h2>
        <div id="role-form-outer-div">
          <Form id="form" onSubmit={this.props.onSalarySubmit}>



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Select Month
              </Form.Label>
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



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Select Year
              </Form.Label>
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


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Select Employee
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  required
                  onChange={value => this.postemployeename(value)}
                >
                  <option value="" disabled selected>Select Employee</option>
                  {this.state.employeeData.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["employee_name"]}</option>
                  ))}
                </Form.Control>
              </Col>
            </Form.Group>










            <Form.Group as={Row} id="form-submit-button">
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit" onClick={() => this.salaryslip_download()} >Submit</Button>
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

export default SalarySlip;
