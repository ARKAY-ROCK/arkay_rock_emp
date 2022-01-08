
# ARKAY ROCK EMPLOYEE MANAGEMENT

Employee and Attendence Mangement System for MARP 


## Tech Stack

**Client:** React, Axios, TailwindCSS

**Server:** Node, Flask

**DATABASE:** MongoDB


## Tools Used

 - [ReactJS](https://reactjs.org/)
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 - [MongoDB](https://www.mongodb.com/)


## Start Development

Install Python Packages



```bash
  pip install -r requirements.txt
```


Clone the Repository


```bash
  git clone url
```


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## API Reference

#### Create New User

```http
  PUT /create_user_account
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user_name,password` | `string` | **Create User**|

#### Login 

```http
  POST /users/login
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_name,password`      | `string` | **user login** |