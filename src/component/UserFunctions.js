import { faCommentsDollar } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';

export const register = newUser => {
    return axios
    .post("http://localhost:5000/users/login",{
        user_name:newUser.user_name,
        device_name:newUser.device_name,
        no_of_device:newUser.no_of_device,
        password:newUser.password
    })
    .then(response => {
        console.log("Registered")
    }

    )
}

export const login =user =>{
    return axios
      .post("http://localhost:5000/users/login",{
          user_name:user.user_name,
          password:user.password
      })
      
      .then(response =>{
          console.log(response.data);
          localStorage.setItem('usertoken',response.data.token)
          return response.data.token
      })
      .catch(err => {
          console.log(err)
      })
}   





