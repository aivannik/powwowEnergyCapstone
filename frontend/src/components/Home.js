import React from 'react';
import Analysis from './Analysis'
import SimpleMap from './SimpleMap'

const home = () => {
    return (
        <div className="container mt-5">
          <div className="row">
            <div className="col-md-12">
              <SimpleMap />
            </div>
            <div className="col-md-12 mt-5">
              <Analysis />
            </div>
          </div>
        </div>
      );
    
  }

export default home;