import React, { Component } from "react";
import "./EmployeeTable.css";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faPlus,
  faTrash,
  faEdit,
  faInfoCircle
} from "@fortawesome/free-solid-svg-icons";
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


class AdminEmployeeTable extends Component {
  state = {
    employeeData: [],
    loading: false,

    columnDefs: [
      {
        headerName: "Employee Code",
        field: "EmployeeCode",
        sortable: true,
        width: 140,
        // filter: true ,
      },
    
    
      {
        headerName: "Position Name",
        field: "PositionName",
        sortable: true,
        width: 120,

        // filter: true ,
      },
      {
        headerName: "Department Name",
        field: "DepartmentName",
        sortable: true
        ,
        width: 120,
        // filter: true ,
      },
      
      
            {
        headerName: "Role",
        field: "RoleName",
        sortable: true,

        width: 120,
        // filter: true ,
      },
  
  
       {
        headerName: "ContactNo",
        field: "ContactNo",
        sortable: true,
        width: 117,
        // filter: true ,
      },
      
      
      
      {
        headerName: "Date Of Joining",
        field: "DateOfJoining",
        sortable: true
        ,
        width: 120,
        // filter: true ,

      },
      


      {
        headerName: "First Name",
        field: "FirstName",
        sortable: true,
        width: 110,

        // filter: true ,
      },
 
 //     {
   //     headerName: "Middle Name",
     //   field: "MiddleName",
       // sortable: true,
       // width: 130,

        // filter: true ,
     // },
      {
        headerName: "Last Name",
        field: "LastName",
        sortable: true,
        width: 110,

        // filter: true ,
      },
      {
        headerName: "DOB",
        field: "DOB",
        sortable: true,
        filter: true,
        type: ["dateColumn"],
        filter: "agDateColumnFilter"
      },
      
        {
        headerName: "Blood Group",
        field: "BloodGroup",
        sortable: true,
        filter: true,

      },
      
 
  

      
      {
        headerName: "Emergency Contact",
        field: "EmergencyContact",
        sortable: true
        ,
        width: 120,
        // filter: true ,

      },
      
      // {
      //   headerName: "Info",
      //   field: "info",
      //   filter: false,
        
    
      //   // cellRenderer:this.ageCellRendererFunc,
      //   // cellRendererFramework: function(params) {
      //   //   return <button OnClick={console.log("pa",params)}>Test</button>;
      //   // },
      //   cellRendererFramework: this.renderInfoButton.bind(this),


      // },
      {
        headerName: "Edit",
        field: "edit",
        filter: false,
    
        // cellRenderer:this.ageCellRendererFunc,
        // cellRendererFramework: function(params) {
        //   return <button OnClick={console.log("pa",params)}>Test</button>;
        // },
        cellRendererFramework: this.renderEditButton.bind(this),


      },
      {
        headerName: "Delete",
        field: "delete",
        filter: false,
       
        // cellRenderer:this.ageCellRendererFunc,
        // cellRendererFramework: function(params) {
        //   return <button OnClick={console.log("pa",params)}>Test</button>;
        // },
        cellRendererFramework: this.renderButton.bind(this),


      },

    ],
    rowData: [],
    defaultColDef: {
      resizable: true,
      width: 100,
      filter: "agTextColumnFilter"
      // filter: true ,
    },
    getRowHeight: function (params) {
      return 45;
    }
  };
  employeeObj = [];
  rowDataT = [];

  loadEmployeeData = () => {
    axios
      .get("/employee-details")
      .then(response => {
        this.employeeObj = response.data;
        console.log("response", response.data);
        this.setState({ employeeData: response.data });
        this.setState({ loading: false });
        this.rowDataT = [];
      
        response.data.map(data => {
          let temp = {
            data,
            Email: data["Email"],
            Password: data["Password"],
            Account: data["Account"] == 1 ? "Admin" : (data["Account"] == 2 ? "HR" : (data["Account"] == 3 ? "Employee" : "")),
            RoleName: data["role"],
            FirstName: data["FirstName"],
            MiddleName: data["MiddleName"],
            LastName: data["LastName"],
            DOB: data["DOB"],
            ContactNo: data["ContactNo"],
            EmployeeCode: data["EmployeeCode"],
            DepartmentName: data["department"],
            PositionName: data["position"],
            DateOfJoining: data["DateOfJoining"],
            EmergencyContact:data["EmergencyContact"],
            BloodGroup:data["Bloodgroup"]
            
            
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
  };

  onEmployeeDelete = e => {
    console.log(e);
    let del={
    employee_id:e,
    };
    if (window.confirm("Are you sure to delete this record? ") == true) {
      axios
        .post("/employee_delete",del)
        .then(res => {
          this.componentDidMount();
        })
        .catch(err => {
          console.log(err);
        });
    }
  };
  componentDidMount() {
    this.loadEmployeeData();
  }
  handleClick = (e) => {
    console.log(e);
  }
  renderInfoButton(params) {
    console.log(params);
    return <div>
      <FontAwesomeIcon
        icon={faInfoCircle}
        onClick={() => this.props.onEmpInfo(params.data.data)}
      /></div>;
  }
  
  renderButton(params) {
    console.log(params);
    return <FontAwesomeIcon
      icon={faTrash}
      onClick={() => this.onEmployeeDelete(params.data.data["FirstName"]+"_"+params.data.data["EmployeeCode"])}
    />;
  }
  renderEditButton(params) {
    console.log(params);
    return <FontAwesomeIcon
      icon={faEdit}
      onClick={() => this.props.onEditEmployee(params.data.data)}
    />;
  }

  searchChange = e => {
    console.log(e.target.value);
    this.setState({ searchData: e.target.value });
  };
   getFilteredEmp() {
     return this.employeeObj.filter(emp => {
       return (
         emp["Email"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["role"][0]["RoleName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["FirstName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["MiddleName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["LastName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["DOB"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["ContactNo"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["EmployeeCode"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["department"][0]["DepartmentName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["position"][0]["PositionName"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase()) ||
         emp["DateOfJoining"]
           .toLowerCase()
           .includes(this.state.searchData.toLocaleLowerCase())
       );
     });
   }

  render() {
    // let filteredEmp = this.getFilteredEmp();
    return (
      <div id="table-outer-div-scroll">
        <h2 id="role-title">Employee Details</h2>

        <Button
          variant="info"
          id="add-button"
          color="ff7043"
          onClick={this.props.onAddEmployee}
        >
          <FontAwesomeIcon icon={faPlus} id="plus-icon" />
          Add
        </Button>

        <div id="clear-both" />
        {!this.state.loading ? (
          <div
            id="table-div"
            className="ag-theme-balham"
             style={
               {
               height: "900px",
           
             }
          }
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              defaultColDef={this.state.defaultColDef}
              columnTypes={this.state.columnTypes}
              rowData={this.state.rowData}
              // floatingFilter={true}
             //  domLayout='autoHeight'
              onGridReady={this.onGridReady}
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

export default AdminEmployeeTable;
