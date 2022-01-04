import React, { Component } from "react";
// import "./SalaryFormEdit.css";
import axios from "axios";
import { Form,Button,Col,Row } from "react-bootstrap";



class ContEdit extends Component {
    state = {
        salaryData : [],
     
        // status: '',
        // portalsInfo:[],
        // SalaryTitleData:this.props.editData["SalaryTitle"],
        // SalaryURLData:this.props.editData["SalaryURL"],
        // SalaryDescriptionData:this.props.editData["SalaryDesc"],      
        // EstimatedTimeData:this.props.editData["EstimatedTime"],   
        // RemarkData:this.props.editData["Remark"],
           BedPolish:this.props.sqteditData["bed_polish"],
            HandPolish:  this.props.sqteditData["hand_polish"],
            DryCutting:this.props.sqteditData["dry_cutting"],
    
            
         //   TaxDeductionData: this.props.editData["salary"][0]["TaxDeduction"],
      

        // value={this.state.SalaryTitleData}
        // onChange={value => this.onSalaryTitleDataChange(value)}

      };

     onBedPolishChange(e){

      this.setState({ BedPolish: e.target.value });
     }

      onHandPolishChange(e) {
        this.setState({ HandPolish: e.target.value });
      }
      onDryCuttingChange(e) {
        this.setState({ DryCutting : e.target.value });
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
        <h2 id="role-form-title">Square Feet Cost 
        {/* {JSON.stringify(this.props.editData ) } */}
        </h2>       
 <div id="role-form-outer-div"><Form id="form" onSubmit={e=>this.props.sqtonSalaryEditUpdate(this.props.sqteditData,e)}>
  



            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Bed Polish
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Bed Polish"
                  required
                  value={this.state.BedPolish}
        onChange={value => this.onBedPolishChange(value)}
                />
              </Col>
            </Form.Group>
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Hand Polish
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Hand Polish"
                  required
                  value={this.state.HandPolish}
        onChange={value => this.onHandPolishChange(value)}
                />
              </Col>
            </Form.Group>
     
     
     
            <Form.Group as={Row}>
              <Form.Label column sm={2}>
              Dry Cutting
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  type="text"
                  placeholder="Dry Cutting"
                  required
                  value={this.state.DryCutting}
        onChange={value => this.onDryCuttingChange(value)}
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
      <Button type="reset" onClick={this.props.sqtonFormEditClose}>cancel</Button>
    </Col>
  </Form.Group>
</Form>
<footer>
  <p>Note: use comma , for multiple values</p>

</footer>

</div>
          {/* </div>
        </div> */}
      </React.Fragment>
    );
  }
}

export default ContEdit;
