import React from 'react';
import Spinner from 'react-bootstrap/Spinner'

const LoadingSpinner = () => (
    <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
        <h3> uploading please wait ... </h3>
  <Spinner animation="border" role="status">
  <span className="visually-hidden">..</span>
</Spinner>
</div>
);

export default LoadingSpinner;