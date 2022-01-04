import React, { Component } from "react";
// import "./AdminSalaryTable.css";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faTrash, faEdit , faDownload } from "@fortawesome/free-solid-svg-icons";
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
        headerName: "Salary",
        field: "BasicSalary",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },
      {
        headerName: "Bank Name",
        field: "BankName",
        sortable: true
        // filter: true ,
      },
      {
        headerName: "Account No",
        field: "AccountNo",
        sortable: true
        // filter: true ,
      },

      {
        headerName: "Account Holder Name",
        field: "AccountHolderName",
        sortable: true,
        // width: 117,
        // filter: true ,
      },
      {
        headerName: "IFSC code",
        field: "IFSCcode",
        sortable: true,
        // width: 117,
        // filter: true ,
      },

      {
        headerName: "Edit",
        field: "edit",
        filter: false ,

        cellRendererFramework: this.renderEditButton.bind(this),
      
    
      },

      {
        headerName: "Delete",
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
      .get("/employee_salary_list")
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
            BasicSalary: data["net_salary"],
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


  renderEditButton(params){
    console.log(params);
    return <FontAwesomeIcon
    icon={faEdit}
    onClick={() => this.props.onEditSalary(params.data.data)}
  />;
  }

  onSalaryDownload() {
    console.log("download function called ");
    axios
      .put('/salary_list_download')
      .then(response => {
        //this.setState({ employeeYear: response.data });
       console.log(response.data);
      // window.alert(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <div id="table-outer-div-scroll">
        <h2 id="role-title">Salary Details</h2>

        <Button
          variant="primary"
          id="add-button"
          onClick={this.props.onAddSalary}
        >
          <FontAwesomeIcon icon={faPlus} id="plus-icon" />
          Add
        </Button>

        <Button
          variant="primary"
          id="add-button"
          onClick={value => this.onSalaryDownload(value)}
                  
        >
          <FontAwesomeIcon icon={faDownload} id="plus-icon" />
          Download 
        </Button>


        <div id="clear-both" />

        {!this.state.loading ? (
          <div
            id="table-div"
            className="ag-theme-balham"
               style={
                 {
                 height: "900px"
               //  width: "100%"
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
            //  domLayout='autoHeight'
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
