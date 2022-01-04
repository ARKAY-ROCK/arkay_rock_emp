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

   

      {
        headerName: "",
        field: "edit",
        filter: false ,
     
        cellRendererFramework: this.renderEditButton.bind(this),
      
    
      },

      {
        headerName: "",
        field: "delete",
        filter: false ,
  
        cellRendererFramework: this.renderButton.bind(this),
      
    
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
      return 35;
    }


  };
  salaryObj = [];
  rowDataT = [];

  loadSalaryData = () => {
    axios
      .get("/employee_monthly_salary/roll")
      .then(response => {
        this.salaryObj = response.data;
        console.log("response", response.data);
        this.setState({ salaryData: response.data });
        this.setState({ loading: false });
        this.rowDataT = [];

        this.salaryObj.map(data => {
          let temp = {
            data,
            finalsalary:data['final_salary'],
            EmployeeName: data["employee_name"],
            month:data["month"],
            squarefeet:data['sq.ft'],
            netsalary:data['net_salary'],
            BasicSalary: data["basic_salary"],
            WL:data['wl_allowence'],
            HRA:data['hra'],
            conveyence:data['conveyence'],
            esishare:data['esi_employee_share'],
            epfshare:data['epf_employee_share'],
            overtime:data['overtime'],
            detection:data['detection'],
            BankName: data["bank_name"],
            AccountNo:data["account_no"],
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

editform(params){
  this.props.onEditSalary(params.data.data)
}

  renderEditButton (params){
    console.log("params",params.data.data);
    return <FontAwesomeIcon
    icon={faEdit}
   // axios.get("/get_esi_epf_share").then();
    onClick={() => this.props.onEditSalary(params.data.data)}

  />;
  }

  render() {
    return (
      <div id="table-outer-div-scroll">
        <h2 id="role-title">Salary Details</h2>

      

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
