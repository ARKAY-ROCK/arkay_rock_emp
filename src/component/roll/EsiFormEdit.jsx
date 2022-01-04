import React, { Component } from "react";
// import "./SalaryFormEdit.css";
import axios from "axios";
import { Form,Button,Col,Row } from "react-bootstrap";



class EsiFormEdit extends Component {
    state = {
        salaryData : [],
     
        // status: '',
        // portalsInfo:[],
        // SalaryTitleData:this.props.editData["SalaryTitle"],
        // SalaryURLData:this.props.editData["SalaryURL"],
        // SalaryDescriptionData:this.props.editData["SalaryDesc"],      
        // EstimatedTimeData:this.props.editData["EstimatedTime"],   
        // RemarkData:this.props.editData["Remark"],
           EmployeeName:this.props.editData["basic_pay"],
            BasicSalaryData:  this.props.editData["conveyence"],
            BankNameData:this.props.editData["bank_name"],
            AccountNoData: this.props.editData["account_no"],
            ReAccountNoData: this.props.editData["account_no"],
            AccountHolderNameData:this.props.editData["account_holder"],
            IFSCcodeData: this.props.editData["ifsc_code"],
            
            BasicPay:this.props.editData["basic_pay"],
            Conveyence:this.props.editData["conveyence"],
            EpfEmployeeShare:this.props.editData["epf_employee_share"],
            EpfEmployeerShare:this.props.editData["epf_employeer_epf"],
            EpfEmployeerPension:this.props.editData["epf_employeer_pension"],
            EsiEmployeeShare:this.props.editData["esi_employee_share"],
            EsiEmployerShare:this.props.editData["esi_employeer_share"],
            HRA:this.props.editData["hra"],
            WlAllowence:this.props.editData["wl_allowence"],
           
            
         //   TaxDeductionData: this.props.editData["salary"][0]["TaxDeduction"],
      

        // value={this.state.SalaryTitleData}
        // onChange={value => this.onSalaryTitleDataChange(value)}

      };

     onBasicPayChange(e){

      this.setState({ BasicPay: e.target.value });
     }

      onConveyenceChange(e) {
        this.setState({ Conveyence: e.target.value });
      }
      onEpfEmployeeShareChange(e) {
        this.setState({ EpfEmployeeShare: e.target.value });
      }
      onEpfEmployeerShareChange(e) {
        this.setState({ EpfEmployeerShare: e.target.value });
      }
      onEpfEmployeerPensionChange(e) {
        this.setState({ EpfEmployeerPension: e.target.value });
      }
      onEsiEmployeeShareChange(e) {
        this.setState({ EsiEmployeeShare: e.target.value });
      }
      onEsiEmployerShareChange(e) {
        this.setState({ EsiEmployerShare: e.target.value });
      }
      onHRAChange(e) {
        this.setState({ HRA: e.target.value });
      }
      
           onWlAllowenceChange(e) {
        this.setState({ WlAllowence: e.target.value });
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
        <h2 id="role-form-title">Edit ESI EPF SHARES
        {/* {JSON.stringify(this.props.editData ) } */}
        </h2>       
 <div id="role-form-outer-div"><Form id="form" onSubmit={e=>this.props.onSalaryEditUpdate(this.props.editData,e)}>
  



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Basic Pay
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="number"
                  placeholder="Basic Pay"
                  required
                  value={this.state.BasicPay}
        onChange={value => this.onBasicPayChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Conveyence
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Conveyence"
                  required
                  value={this.state.Conveyence}
        onChange={value => this.onConveyenceChange(value)}
                />
              </Col>
            </Form.Group>
     
     
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Epf Employee Share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Epf Employee Share"
                  required
                  value={this.state.EpfEmployeeShare}
        onChange={value => this.onEpfEmployeeShareChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
             Epf Employeer Share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Epf Employeer Share"
                  required
                  value={this.state.EpfEmployeerShare}
                  onChange={value => this.onEpfEmployeerShareChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
             Epf Employeer Pension
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Epf Employeer Pension"
                  required
                  value={this.state.EpfEmployeerPension}
        onChange={value => this.onEpfEmployeerPensionChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Esi Employee Share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Esi Employee Share"
                  required
                  value={this.state.EsiEmployeeShare}
        onChange={value => this.onEsiEmployeeShareChange(value)}
                />
              </Col>
            </Form.Group>
            
            
       <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Esi Employeer Share
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Esi Employeer Share"
                  required
                  value={this.state.EsiEmployerShare}
        onChange={value => this.onEsiEmployerShareChange(value)}
                />
              </Col>
            </Form.Group>

       <Form.Group as={Row}>
              <Form.Label column sm={2}>
              HRA
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="HRA"
                  required
                  value={this.state.HRA}
        onChange={value => this.onHRAChange(value)}
                />
              </Col>
            </Form.Group>

       <Form.Group as={Row}>
              <Form.Label column sm={2}>
              WlAllowence
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="WlAllowence"
                  required
                  value={this.state.WlAllowence}
        onChange={value => this.onWlAllowenceChange(value)}
                />
              </Col>
            </Form.Group>


  <Form.Group as={Row} id="form-submit-button">
    <Col sm={{ span: 10, offset: 2 }}>
      <Button type="submit">Update</Button>
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

export default EsiFormEdit;
