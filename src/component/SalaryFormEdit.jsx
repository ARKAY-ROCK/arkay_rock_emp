import React, { Component } from "react";
// import "./SalaryFormEdit.css";
import axios from "axios";
import { Form,Button,Col,Row } from "react-bootstrap";



class SalaryFormEdit extends Component {
    state = {
        salaryData : [],
     
        // status: '',
        // portalsInfo:[],
        // SalaryTitleData:this.props.editData["SalaryTitle"],
        // SalaryURLData:this.props.editData["SalaryURL"],
        // SalaryDescriptionData:this.props.editData["SalaryDesc"],      
        // EstimatedTimeData:this.props.editData["EstimatedTime"],   
        // RemarkData:this.props.editData["Remark"],
           EmployeeName:this.props.editData["employee_name"],
            BasicSalaryData:  this.props.editData["net_salary"],
            BankNameData:this.props.editData["bank_name"],
            AccountNoData: this.props.editData["account_no"],
            ReAccountNoData: this.props.editData["account_no"],
            AccountHolderNameData:this.props.editData["account_holder"],
            IFSCcodeData: this.props.editData["ifsc_code"],
         //   TaxDeductionData: this.props.editData["salary"][0]["TaxDeduction"],
      

        // value={this.state.SalaryTitleData}
        // onChange={value => this.onSalaryTitleDataChange(value)}

      };

     onEmployeeNameChange(e){

      this.setState({ EmployeeName: e.target.value });
     }

      onBasicSalaryDataChange(e) {
        this.setState({ BasicSalaryData: e.target.value });
      }
      onBankNameDataChange(e) {
        this.setState({ BankNameData: e.target.value });
      }
      onAccountNoDataChange(e) {
        this.setState({ AccountNoData: e.target.value });
      }
      onReAccountNoDataChange(e) {
        this.setState({ ReAccountNoData: e.target.value });
      }
      onAccountHolderNameDataChange(e) {
        this.setState({ AccountHolderNameData: e.target.value });
      }
      onIFSCcodeDataChange(e) {
        this.setState({ IFSCcodeData: e.target.value });
      }
      onTaxDeductionDataChange(e) {
        this.setState({ TaxDeductionData: e.target.value });
      }

     
      
      loadSalaryInfo = () => {
        axios
          .get("/employee_list")
          .then(response => {
            this.setState({ salaryData: response.data });
          })
          .catch(error => {
            console.log(error);
          });
      };
      
      componentWillMount() {
        this.loadSalaryInfo();
        // this.loadPositionInfo();
        // this.loadDepartmentInfo();
      }
  render() {
   
    return (
      <React.Fragment>      
        <h2 id="role-form-title">Edit Salary Details
        {/* {JSON.stringify(this.props.editData ) } */}
        </h2>       
 <div id="role-form-outer-div"><Form id="form" onSubmit={e=>this.props.onSalaryEditUpdate(this.props.editData,e)}>
  
 <Form.Group as={Row}>
              <Form.Label column sm={2}>
                Employee Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  required
                >
                   {/* <option value="" disabled selected>Select your option</option> */}
                  {this.state.salaryData.map((data, index) => (

                    <option key={index} value={data["employee_name"]}

                    selected={this.props.editData["employee_name"] == data["employee_name"]} disabled>{data["employee_name"]}


                    </option>
                 

                  ))}
                </Form.Control>
              </Col>

            </Form.Group>


            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Gross Salary
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  placeholder="Gross Salary"
                  required
                  value={this.state.BasicSalaryData}
        onChange={value => this.onBasicSalaryDataChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Bank Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Bank Name"
                  required
                  value={this.state.BankNameData}
        onChange={value => this.onBankNameDataChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Account No
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Account No"
                  required
                  value={this.state.AccountNoData}
        onChange={value => this.onAccountNoDataChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Re-Enter Account No
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Re-Enter Account No"
                  required
                  value={this.state.ReAccountNoData}
                  onChange={value => this.onReAccountNoDataChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Account Holder Name
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Account Holder Name"
                  required
                  value={this.state.AccountHolderNameData}
        onChange={value => this.onAccountHolderNameDataChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              IFSC Code
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="IFSC Code"
                  required
                  value={this.state.IFSCcodeData}
        onChange={value => this.onIFSCcodeDataChange(value)}
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
      <Button type="reset" onClick={this.props.onFormEditClose}>cancel</Button>
    </Col>
  </Form.Group>
</Form></div>
          {/* </div>
        </div> */}
      </React.Fragment>
    );
  }
}

export default SalaryFormEdit;
