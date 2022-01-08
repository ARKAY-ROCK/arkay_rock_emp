import React, { Component } from "react";
// import "./AdminSalaryTable.css";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faTrash, faEdit, faDownload } from "@fortawesome/free-solid-svg-icons";
import { RingLoader } from "react-spinners";
import { css } from "@emotion/core";
import { Form, Container, Row, Col, Button } from "react-bootstrap";
import {saveAs} from "file-saver";


import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-balham.css";


const override = css`
  display: block;
  margin: 0 auto;
  margin-top: 45px;
  border-color: red;
`;


class AdminSalaryTable extends Component {


  state = {
    salaryData: [],
    loading: true,
    employeeMonth: [],
    employeeYear: [],
    month: '',
    year: '',



    currentdate: new Date().getMonth(),

    columnDefs: [
      {
        headerName: "Employee Name",
        field: "EmployeeName",
        sortable: true
        // filter: true ,
      },



      {
        headerName: "Month",
        field: "month",
        sortable: true
        // filter: true ,
      },



      {
        headerName: "Salary",
        field: "finalsalary",
        sortable: true
        // filter: true ,
      },


      {
        headerName: "sq.ft",
        field: "squarefeet",
        sortable: true

        // filter: true ,
      },

      {
        headerName: "Net Salary",
        field: "netsalary",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },


      {
        headerName: "Basic Salary",
        field: "BasicSalary",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },

      {
        headerName: "W Allowence",
        field: "WL",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },


      {
        headerName: "HRA",
        field: "HRA",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },

      {
        headerName: "conveyence",
        field: "conveyence",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },


      {
        headerName: "ESI ",
        field: "esishare",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },

      {
        headerName: "EPF ",
        field: "epfshare",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },


      {
        headerName: "Over Time",
        field: "overtime",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },

      {
        headerName: "Detection",
        field: "detection",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },



    ],
    rowData: [],
    defaultColDef: {
      resizable: true,
      width: 200,
      filter: "agTextColumnFilter"
      // filter: true ,
    },
    getRowHeight: function (params) {
      return 35;
    }


  };
  salaryObj = [];
  rowDataT = [];


  onmonthchange(e) {
    this.setState({ month: e.target.value });
  }

  onyearchange(e) {
    this.setState({ year: e.target.value });
  }


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



  loadSalaryData = () => {
    let body = {
      month: this.state.month,
      year: this.state.year
    };
    axios
      .put("/employee_monthly_salary_month_year", body)
      .then(response => {
        this.salaryObj = response.data;
        console.log("response", response.data);
        this.setState({ salaryData: response.data });
        this.setState({ loading: false });
        this.rowDataT = [];

        this.salaryObj.map(data => {
          let temp = {
            data,
            finalsalary: data['final_salary'],
            EmployeeName: data["employee_name"],
            month: data["month"],
            squarefeet: data['sq.ft'],
            netsalary: data['net_salary'],
            BasicSalary: data["basic_salary"],
            WL: data['wl_allowence'],
            HRA: data['hra'],
            conveyence: data['conveyence'],
            esishare: data['esi_employee_share'],
            epfshare: data['epf_employee_share'],
            overtime: data['overtime'],
            detection: data['detection'],
            BankName: data["bank_name"],
            AccountNo: data["account_no"],
            AccountHolderName: data["account_holder"],
            IFSCcode: data["ifsc_code"],
            //TaxDeduction:data["salary"][0]["TaxDeduction"],

          };

          this.rowDataT.push(temp);
        });
        this.setState({ rowData: this.rowDataT });



      })
      .catch(error => {
        console.log(error);
      });
  };

  onSalaryDelete = e => {
    console.log(e);
    let body = {
      employee_name: e
    };
    if (window.confirm("Are you sure to delete this record? ") == true) {
      axios
        .put("/employee_salary_delete", body)
        .then(res => {
          this.componentDidMount();
        })
        .catch(err => {
          console.log(err);
        });
    }
  };

  handlechange(e) {
    console.log(e.target.value);
    this.setState({ currentdate: e.target.value });
    this.loadSalaryData();

  }

  componentDidMount() {
   this.loadMonth();
   this.loadYear();
  }

  renderButton(params) {
    console.log(params);
    return <FontAwesomeIcon
      icon={faTrash}
      onClick={() => this.onSalaryDelete(params.data.data["employee_name"])}
    />;
  }



  editform(params) {
    this.props.onEditSalary(params.data.data)
  }

  renderEditButton(params) {
    console.log("params", params.data.data);
    return <FontAwesomeIcon
      icon={faEdit}
      // axios.get("/get_esi_epf_share").then();
      onClick={() => this.props.onEditSalary(params.data.data)}

    />;
  }

  render() {
    return (
      <div id="table-outer-div-scroll">

        <div >
          <h2 id="role-title">Salary Details {this.state.month + " : "} {this.state.year} </h2>

          <Container>
            <Row>

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
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10, offset: 2 }}>
                    <Button type="submit" onClick={this.loadSalaryData} >
                      <FontAwesomeIcon icon={faDownload} id="plus-icon" />
                      GET</Button>
                  </Col>
                </Form.Group>
              </Col>

              <Col>
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10, offset: 2 }}>
                    <Button
                      variant="info"

                      color="ff7043"
                      onClick={() =>{
                        axios({
                          url: '/monthly_epf_download', 
                         data: { date: this.state.currentdate ,month: this.state.month,
                          year: this.state.year},//your url
                          method: 'PUT',
                          responseType: 'blob', // important
                        }).then((response) => {
                           const url = window.URL.createObjectURL(new Blob([response.data]));
                           const link = document.createElement('a');
                           link.href = url;
                           link.setAttribute('download', 'MARP EPF REPORT.pdf'); //or any other extension
                           document.body.appendChild(link);
                           link.click();
                        });
                       
                      }
                    }
                    >

                      <FontAwesomeIcon icon={faDownload} id="plus-icon" />
                      EPF
                    </Button>
                  </Col>
                </Form.Group>
              </Col>

              <Col>
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10 }} className="form-input" >

                    <Button
                      variant="info"

                      color="ff7043"
                      onClick={() =>{
                        axios({
                          url: '/monthly_esi_download', 
                         data: { date: this.state.currentdate ,month: this.state.month,
                          year: this.state.year},//your url
                          method: 'PUT',
                          responseType: 'blob', // important
                        }).then((response) => {
                           const url = window.URL.createObjectURL(new Blob([response.data]));
                           const link = document.createElement('a');
                           link.href = url;
                           link.setAttribute('download', 'MARP ESI REPORT.pdf'); //or any other extension
                           document.body.appendChild(link);
                           link.click();
                        });
                       
                      }
                    }
                    >
                      <FontAwesomeIcon icon={faDownload} id="plus-icon" />
                      ESI
                    </Button>
                  </Col>
                </Form.Group>
              </Col>


              <Col>
                <Form.Group as={Row} id="form-submit-button">
                  <Col sm={{ span: 10, offset: 2 }}>
                    <Button
                      variant="info"

                      color="ff7043"
                      onClick={() =>{
                        axios({
                          url: '/monthly_salary_download', 
                         data: { date: this.state.currentdate ,month: this.state.month,
                          year: this.state.year},//your url
                          method: 'PUT',
                          responseType: 'blob', // important
                        }).then((response) => {
                           const url = window.URL.createObjectURL(new Blob([response.data]));
                           const link = document.createElement('a');
                           link.href = url;
                           link.setAttribute('download', 'MARP SALARY REPORT.pdf'); //or any other extension
                           document.body.appendChild(link);
                           link.click();
                        });
                       
                      }
                    }
                    >
                      <FontAwesomeIcon icon={faDownload} id="plus-icon" />
                      All
                    </Button>
                  </Col>
                </Form.Group>
              </Col>



              <Col>
              </Col>

            </Row>
          </Container>






        </div>

        <div id="clear-both" />

        {!this.state.loading ? (
          <div
            id="table-div"
            className="ag-theme-balham"
            style={
              {
                height: "900px"


              }
            }
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              defaultColDef={this.state.defaultColDef}
              columnTypes={this.state.columnTypes}
              rowData={this.state.rowData}
              // floatingFilter={true}
              // onGridReady={this.onGridReady}
              pagination={false}
              //domLayout='autoHeight'
              paginationPageSize={10}
              getRowHeight={this.state.getRowHeight}
            />
          </div>
        ) : (
          <div id="loading-bar">
            <RingLoader
              css={override}
              sizeUnit={"px"}
              size={50}
              color={"#0000ff"}
              loading={true}
            />
          </div>
        )}

      </div>
    );
  }
}

export default AdminSalaryTable;
