import React, { Component } from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faUpload, faEdit , faDownload } from "@fortawesome/free-solid-svg-icons";
import { Form, Button, Col, Row } from "react-bootstrap";
import LoadingSpinner from "./LoadingSpinner";

class UploadAttendence extends Component {
  state = {
    employeeData : [],
    departmentData:[],
    employeeMonth :[],
    employeeYear : [],
    file_name: '',
    department:'',
    month:'',
    year:'',
    isUploading:false
   
    
  }
 
  
  loadDepartment = () => {
    axios
      .get('/department_post')
      .then(response => {
        this.setState({ departmentData: response.data });
      })
      .catch(error => {
        console.log(error);
      });
  };

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


  onmonthchange(e){
    this.setState({month: e.target.value});
    }


    onyearchange(e){
        this.setState({year: e.target.value});
        }


  componentWillMount() {
    this.loadDepartment();
    this.loadMonth();
    this.loadYear();
    
    // this.loadPositionInfo();
    // this.loadDepartmentInfo();
  }


  async  postemployeename(e)  {
      console.log(e.target.value);
        this.setState({ employee_name : e.target.value });
    await  axios
      .put('/get_selected_employee_details',{'employee_name':e.target.value,'month':this.state.month,'year':this.state.year})
      .then(response => {
        //this.setState({ employeeYear: response.data });
        console.log(response.data['department']);
        console.log(response.data[0]['department']);
        this.setState({ name: response.data[0]['employee_name'] });
        this.setState({ department: response.data[0]['department'] });

      })
      .catch(error => {
        console.log(error);
      });
 
  }

  
  ondepartmentChange(e) {
    this.setState({department : e.target.value});
    console.log(e.target.value);
  }


           async selectedfile(e) {
              var files = e.target.files;
              var filesArray = [].slice.call(files);
             await filesArray.forEach(e => {
                console.log(e.name);
                this.setState({file_name: e.name});
              });
            }

  updatesqtft() {
      console.log("submit pressed");
      axios
      .put('/update_ot_zero',{'department':this.state.department,'month':this.state.month,'year':this.state.year})
      .then(response => {
        //this.setState({ employeeYear: response.data });
       console.log(response.data);
       window.alert(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }

  
async  testupdate() {
    console.log("submit pressed");
    this.setState({isUploading:true});
 await   axios
    .put('/test_att',{filename:this.state.file_name})
    .then(response => {
      //this.setState({ employeeYear: response.data });
     console.log(response.data);
     window.alert(response.data);
     this.setState({isUploading:false});
    })
    .catch(error => {
      console.log(error);
      window.alert("error not uploaded");
      this.setState({isUploading:false});
    });
}


  render() {
    //const { data, isUploading } = this.state;
    return (

      
      this.state.isUploading ? <LoadingSpinner /> :  


      <div>
        <h2 id="role-form-title">Upload Attendance </h2>
     
        
        <div id="role-form-outer-div">
          <Form id="form" onSubmit={this.props.onSalarySubmit}>



          <Form as={Row}>
              <Form.Label column sm={2}>
              Select File
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                
                  type="file"
                  placeholder="Select File"
                  required
                  onChange={value => this.selectedfile(value)}
                />
                
              </Col>
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit"  onClick= { () => this.testupdate() } >
                <FontAwesomeIcon icon={faUpload} id="plus-icon" />
                  Upload  </Button>
              </Col>
            

            </Form>


&nbsp;
            <Form.Group as={Row}>
            <Form.Label column sm={2}>
                Select Month
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  
                  onChange={value => this.onmonthchange(value)}
                >
                   <option value="" disabled selected>Select Month</option>
                  {this.state.employeeMonth.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["month"]}</option>
                  ))}
                </Form.Control>
              </Col>
            </Form.Group>



            <Form.Group as={Row}>
            <Form.Label column sm={2}>
                Select Year
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  
                  onChange={value => this.onyearchange(value)}
                  
                >
                   <option value="" disabled selected>Select Year</option>
                  {this.state.employeeYear.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["year"]}</option>
                  ))}
                </Form.Control>
              </Col>
            </Form.Group>


            <Form.Group as={Row}>
            <Form.Label column sm={2}>
               Mark OT as Zero
              </Form.Label>
              <Col sm={10} className="form-input">
                <Form.Control
                  as="select"
                  
                  onChange={value => this.ondepartmentChange(value)}
                >
                   <option value="" disabled selected>Select Department</option>
                  {this.state.departmentData.map((data, index) => (

                    <option key={index} value={data["_id"]}>{data["department"]}</option>
                  ))}
                </Form.Control>
              </Col>
            </Form.Group>

        
   
            <Form.Group as={Row} id="form-submit-button">
              <Col sm={{ span: 10, offset: 2 }}>
                <Button type="submit"  onClick= { () => this.updatesqtft() } >update</Button>
              </Col>
            </Form.Group>

            <Form.Group as={Row} id="form-cancel-button">
              <Col sm={{ span: 10, offset: 2 }} id="form-cancel-button-inner">
                <Button type="reset" onClick={this.props.onFormClose}>
                  cancel
                </Button>
              </Col>
            </Form.Group>
          </Form>

          
        </div>

        {/* </div>
        </div> */}
      </div>
      
    );
  }
}

export default UploadAttendence;
