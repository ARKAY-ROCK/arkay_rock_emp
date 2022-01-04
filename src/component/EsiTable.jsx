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
    sqfeetDate: [],
    loading: true,


    columnDefs: [
      {
        headerName: "Basic Pay",
        field: "BasicPay",
        sortable: true
        // filter: true ,
      },
      {
        headerName: "WL Allowence",
        field: "WLAllowence",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },
      {
        headerName: "HRA",
        field: "HRA",
        sortable: true
        // filter: true ,
      },
      {
        headerName: "Conveyence",
        field: "Conveyence",
        sortable: true
        // filter: true ,
      },

      {
        headerName: "ESI Employeer",
        field: "ESIEmployeer",
        sortable: true,
        // width: 117,
        // filter: true ,
      },
      {
        headerName: "ESI Employee",
        field: "ESIEmployee",
        sortable: true,
        // width: 117,
        // filter: true ,
      },

  {
        headerName: "EPF Employee Pension",
        field: "ESFEmployeePension",
        sortable: true,
        // width: 117,
        // filter: true ,
      },
        {
        headerName: "EPF Employee",
        field: "EPFEmployee",
        sortable: true,
        // width: 117,
        // filter: true ,
      },
      
      
        {
        headerName: "EPF Employeer",
        field: "EPFEmployeer",
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
    
    
        sqtcolumn: [
      {
        headerName: "Bed Polish",
        field: "bedpolish",
        sortable: true
        // filter: true ,
      },
      {
        headerName: "Hand Polish",
        field: "handpolish",
        sortable: true,
        type: "numberColumn",
        filter: 'agNumberColumnFilter'
        // filter: true ,
      },
      {
        headerName: "Dry Cutting",
        field: "drycutting",
        sortable: true
        // filter: true ,
      },
      
          {
        headerName: "",
        field: "edit",
        filter: false ,
        width: 30,
        cellRendererFramework: this.sqtrenderEditButton.bind(this),
      
    
      },
      
      
      ],
    
    sqtData:[],
      defaultColDefsqt: {
      resizable: true,
      width: 200,
      filter: "agTextColumnFilter"
      // filter: true ,
    },
    getRowHeight: function(params) {
      return 35;
    },
    
    
    
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
  sqtObj = [];
  
  
  
  salaryObj = [];
  rowDataT = [];
  sqtDataT=[];
  
  loadSalaryData = () => {
    axios
      .get("/get_esi_epf_share")
      .then(response => {
        this.salaryObj = response.data;
        console.log("esi_epf_data", response.data);
        this.setState({ salaryData: response.data });
        this.setState({ loading: false });
        this.rowDataT = [];

         this.salaryObj.map(data => {
          let temp = {
            data,
            
            BasicPay: data["basic_pay"],
            WLAllowence: data["wl_allowence"],
            HRA: data["hra"],
            Conveyence:data["conveyence"],
            ESIEmployeer: data["esi_employeer_share"],
            ESIEmployee: data["esi_employee_share"],
            ESFEmployeePension: data["epf_employeer_pension"],
            EPFEmployee: data["epf_employee_share"],
            EPFEmployeer: data["epf_employeer_epf"],
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
  
  
  
    loadSqtData = () => {
    axios
      .get("/get_contractors")
      .then(response => {
        this.sqtObj = response.data;
        console.log("esi_epf_data", response.data);
        this.setState({ sqfeetDate: response.data });
        this.setState({ loading: false });
        this.sqtDataT = [];

         this.sqtObj.map(data => {
          let temp = {
            data,
            bedpolish: data["bed_polish"],
            handpolish: data["hand_polish"],
            drycutting: data["dry_cutting"],
          
            //TaxDeduction:data["salary"][0]["TaxDeduction"],
            
          };
          
          this.sqtDataT.push(temp);
        });
        this.setState({ sqtData: this.sqtDataT });



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
    this.loadSqtData();
  }

  renderButton(params){
    console.log(params);
    return <FontAwesomeIcon
    icon={faTrash}
    onClick={() => this.onSalaryDelete(params.data.data["employee_name"])}
  />;
  }


  renderEditButton(params){
    console.log("esi_edit",params.data.data);
    return <FontAwesomeIcon
    icon={faEdit}
    onClick={() => this.props.onEditSalary(params.data.data)}
  />;
  }
  
  
  
   sqtrenderEditButton(params){
    console.log("esi_edit",params.data.data);
    return <FontAwesomeIcon
    icon={faEdit}
    onClick={() => this.props.onsqtEditSalary(params.data.data)}
  />;
  }

  render() {
    return (
      <div id="table-outer-div-scroll">
        <h2 id="role-title"> Percentage Setter  </h2>

       
        <div id="clear-both" />

        {!this.state.loading ? (
          <div
            id="table-div"
            className="ag-theme-balham"
               style={
                 {
                 height: "100px",
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
              paginationPageSize={10}
              getRowHeight={this.state.getRowHeight}
            />
            
               <AgGridReact
              columnDefs={this.state.sqtcolumn}
              defaultColDef={this.state.defaultColDefsqt}
              columnTypes={this.state.columnTypes}
              rowData={this.state.sqtData}
              // floatingFilter={true}
              // onGridReady={this.onGridReady}
              pagination={false}
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
