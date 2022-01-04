import React, { Component } from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faTrash, faEdit } from "@fortawesome/free-solid-svg-icons";
import { RingLoader } from "react-spinners";
import { css } from "@emotion/core";

import { Container, Form, Button, Col, Row } from "react-bootstrap";

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
    employeeData: [],
    gridOptions: {
      rowModelType: 'infinite',
    },
    month: [],
    year: [],
    months: "",
    years: "",
    dates:"",
  
    loading: false,


    columnDefs: [
      {
        headerName: "Employee Name",
        field: "EmployeeName",
        sortable: true
        // filter: true ,
      },

      {
        headerName: "Date",
        field: "Date",
        sortable: true,
        type: ["dateColumn"],
        filter: "agDateColumnFilter",
        filterParams: {
          comparator:
            function (filterLocalDateAtMidnight, cellValue) {
              var dateAsString = cellValue;
              if (dateAsString == null
              ) {
                return 0;
              }
              var dateParts = dateAsString.split('/');
              var day = Number(dateParts[2]);
              var month = Number(dateParts[1]) - 1;
              var year = Number(dateParts[0]);
              var cellDate = new Date(day, month, year);
              if (cellDate < filterLocalDateAtMidnight) {
                return -1;
              }
              else if (cellDate > filterLocalDateAtMidnight) {
                return 1;
              }
              else {
                return 0;
              }
            }
        }
        // filter: true 
      },

      {
        headerName: "Status",
        field: "status",
        sortable: true

        // filter: true 
      },

      {
        headerName: "In Time",
        field: "intime",
        sortable: true
        // filter: true ,
      },

      {
        headerName: "Out Time",
        field: "outtime",
        sortable: true,
        // width: 117,
        // filter: true ,
      },
      {
        headerName: "Delay",
        field: "delay",
        sortable: true,
        // width: 117,
        // filter: true ,
      },

      {
        headerName: "Overtime",
        field: "overtime",
        sortable: true,
        // width: 117,
        // filter: true ,
      },



      {
        headerName: "Total (hrs)",
        field: "totalhours",
        sortable: true,
        // width: 117,
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
      //return 35;
      return 50;
    },

    rowtype: function (params) {
      return 'infinite';
    }


  };
  employeeObj = [];
  rowDataT = [];

  onmonthchange(e) {
    this.setState({ months: e.target.value });

  }


  onyearchange(e) {
    this.setState({ years: e.target.value });
  }


onDateChenge = (e) => {
  console.log(e.target.value);
  axios
  .put('/attendence_list',{key:"date",date:e.target.value})
  .then(response => {
    this.employeeObj = response.data;
    console.log("response", response.data);
    this.setState({ employeeData: response.data });
    this.setState({ loading: false });
    this.rowDataT = [];
  
    response.data.map(data => {
      let temp = {
        data,
        EmployeeName: data["employee_name"],
        Date: data["_id"],
        status: data["status"],
        intime: data["in_time"],
        outtime: data["out_time"],
        delay: data["delay"],
        overtime: data["overtime"],
        totalhours: data["total_hours"],
        
      };
      console.log(this.temp);
      this.rowDataT.push(temp);
      console.log(this.rowDataT);
      console.log("rowdata");
    });

    console.log("not inside");
    this.setState({ rowData: this.rowDataT });
      
    
  })
  .catch(error => {
    console.log("error",error);
  });
}

getattendence = () => {
  axios
  .put('/attendence_list',{key:"month_year",month_year:this.state.months+"_"+this.state.years})
  .then(response => {
    this.employeeObj = response.data;
    console.log("response", response.data);
    this.setState({ employeeData: response.data });
    this.setState({ loading: false });
    this.rowDataT = [];
  
    response.data.map(data => {
      let temp = {
        data,
        EmployeeName: data["employee_name"],
        Date: data["_id"],
        status: data["status"],
        intime: data["in_time"],
        outtime: data["out_time"],
        delay: data["delay"],
        overtime: data["overtime"],
        totalhours: data["total_hours"],
        
      };
      console.log(this.temp);
      this.rowDataT.push(temp);
      console.log(this.rowDataT);
      console.log("rowdata");
    });

    console.log("not inside");
    this.setState({ rowData: this.rowDataT });
      
    
  })
  .catch(error => {
    console.log("error",error);
  });
}



  loadMonth = () => {
    axios
      .get('/salary_month')
      .then(response => {
        this.setState({ month: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };


  loadYear = () => {
    axios
      .get('/salary_year')
      .then(response => {
        this.setState({ year: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };



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


  renderEditButton(params) {
    console.log(params);
    return <FontAwesomeIcon
      icon={faEdit}
      onClick={() => this.props.onEditSalary(params.data.data)}
    />;
  }

  render() {
    return (
      <div id="table-outer-div-scroll">
        <br />
        <Container>
          <Row>
            <Col>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                  Date
                </Form.Label>
                <Col sm={10} className="form-input">
                  <Form.Control
                    type="date"
                    placeholder="Date Of Joining"
                    required
                    onChange={this.onDateChenge}
                  />
                </Col>
              </Form.Group>
            </Col>
            <Col>
              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                   Month
                </Form.Label>
                <Col sm={10} className="form-input">
                  <Form.Control
                    as="select"
                    required
                    onChange={value => this.onmonthchange(value)}
                  >
                    <option value="" disabled selected>Select Month</option>
                    {this.state.month.map((data, index) => (

                      <option key={index} value={data["_id"]}>{data["month"]}</option>
                    ))}
                  </Form.Control>
                </Col>
              </Form.Group>
            </Col>
            <Col>

              <Form.Group as={Row}>
                <Form.Label column sm={2}>
                   Year
                </Form.Label>
                <Col sm={10} className="form-input">
                  <Form.Control
                    as="select"
                    required
                    onChange={value => this.onyearchange(value)}

                  >
                    <option value="" disabled selected>Select Year</option>
                    {this.state.year.map((data, index) => (

                      <option key={index} value={data["_id"]}>{data["year"]}</option>
                    ))}
                  </Form.Control>
                </Col>
              </Form.Group>

            </Col>
           
            <Col sm={{ span: 1, offset: 2 }}>
                <Button type="submit" onClick={this.getattendence} > GET</Button>
              </Col>

          </Row>

         
        </Container>

        <div id="clear-both" />

        {!this.state.loading ? (
          <div
            id="table-div"
            className="ag-theme-balham"
          //   style={
          //     {
          //     height: "500px",
          //     width: "100%"
          //   }
          // }
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              //rowModelType={this.state.rowModelType}
              defaultColDef={this.state.defaultColDef}
              columnTypes={this.state.columnTypes}
              rowData={this.state.rowData}
              floatingFilter={true}
              domLayout='autoHeight'
              // onGridReady={this.onGridReady}
              pagination={false}
              //pagination={true}
              paginationPageSize={10}
              //singleClickEdit={true}
              //paginationPageSize={10}
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
