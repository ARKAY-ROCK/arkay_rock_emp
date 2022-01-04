import React, { Component } from "react";
// import "./AdminSalaryTable.css";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faTrash, faEdit } from "@fortawesome/free-solid-svg-icons";
import { RingLoader } from "react-spinners";
import { css } from "@emotion/core";
import { Button } from "react-bootstrap";


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
    gridOptions:{
      rowModelType: 'infinite',
    },
    salaryData: [],
    loading: true,


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
        filterParams:{
          comparator:
          function(filterLocalDateAtMidnight,cellValue){
            var dateAsString=cellValue;
            if( dateAsString==null
              ){
                return 0;
            }
            var dateParts=dateAsString.split('/');
            var day=Number(dateParts[2]);
            var month=Number(dateParts[1]) - 1;
            var year= Number(dateParts[0]);
            var cellDate=new Date(day,month,year);
            if(cellDate<filterLocalDateAtMidnight){
              return -1;
            }
            else if(cellDate>filterLocalDateAtMidnight){
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

      {
        headerName: "",
        field: "edit",
        filter: false ,
        width: 30,
        cellRendererFramework: this.renderEditButton.bind(this),
      
    
      },

  
      
    ],
    rowData: [],
    defaultColDef: {
      resizable: true,
      width: 200,

      filter: "agTextColumnFilter"
      // filter: true ,
    },
    getRowHeight: function(params) {
      //return 35;
      return 50;
    },

    rowtype:function(params){
      return 'infinite';
    }


  };
  salaryObj = [];
  rowDataT = [];

  loadSalaryData = () => {
    axios
      .get("/attendence_list/roll")
      .then(response => {
        this.salaryObj = response.data;
        console.log("response", response.data);
        this.setState({ salaryData: response.data });
        this.setState({ loading: false });
        this.rowDataT = [];

        this.salaryObj.map(data => {
          let temp = {
            data,
            EmployeeName: data["employee_name"],
            intime: data["in_time"],
            Date: data["date"],
            outtime:data["out_time"],
            delay: data["delay"],
            overtime: data["overtime"],
            totalhours: data["totalhours"],
            status: data["status"],
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
      employee_name:e
    };
    if (window.confirm("Are you sure to delete this record? ") == true) {
      axios
        .put("/employee_salary_delete",body)
        .then(res => {
          this.componentDidMount();
        })
        .catch(err => {
          console.log(err);
        });
    }
  };


  componentDidMount() {
    this.loadSalaryData();
  }

  renderButton(params){
    console.log(params);
    return <FontAwesomeIcon
    icon={faTrash}
    onClick={() => this.onSalaryDelete(params.data.data["employee_name"])}
  />;
  }


  renderEditButton(params){
    console.log(params);
    return <FontAwesomeIcon
    icon={faEdit}
    onClick={() => this.props.onEditSalary(params.data.data)}
  />;
  }

  render() {
    return (
      <div id="table-outer-div-scroll">
        <h2 id="role-title">Attendence</h2>

      

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
