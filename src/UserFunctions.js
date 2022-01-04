import axios from 'axios';

export const register = newUser => {
    return axios
    .post("/users/register",{
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
      .post("users/login",{
          user_name:user.user_name,
          password:user.password
      })
      
      .then(response =>{
          localStorage.setItem('usertoken',response.data.token)
          return response.data.token
      })
      .catch(err => {
          console.log(err)
      })
}   





