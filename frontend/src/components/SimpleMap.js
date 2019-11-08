
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Polygon from 'google-map-react';
import coordinates from './Coordinates1'
import Marker from './Marker'
const AnyReactComponent = ({ marker }) => <div>{marker}</div>;

class SimpleMap extends Component {
    static defaultProps = {
        center: {
            lat: 34.42,
            lng: -119.70
        },
        zoom: 8

    };

    render() {

        return (
            // Important! Always set the container height explicitly
<<<<<<< HEAD
            // only one root is allowed so the wrapper div is required even if it's not doing anything
            <div>
                <div style={{ height: '500px', width: '100%' }}>
                    <GoogleMapReact
                        bootstrapURLKeys={{ key: 'AIzaSyCgi0P05okXVDaayvOKj80KJC2JU_p3A2k' }}
                        defaultCenter={this.props.center}
                        defaultZoom={this.props.zoom}
                    >
                        <AnyReactComponent
                            lat={34.4208}
                            lng={119.6982}
                            marker="My Marker"
                        />
=======
             // only one root is allowed so the wrapper div is required even if it's not doing anything
            <div>
                <div style={{ height: '500px', width: '100%' }}>
                    <GoogleMapReact
                        bootstrapURLKeys={{ key: '000' }}
                        defaultCenter={this.props.center}
                        defaultZoom={this.props.zoom}
                    >
                        <Marker
						 	lat={34.4208}
                            lng={-119.6982}
                            marker="My Marker"
							color = "blue"
						/>
						{/*}	<Polygon
								path={coordinates}
								key={1}
								options={{
									fillColor: "#000",
									fillOpacity: 0.4,
									strokeColor: "#000",
									strokeOpacity: 1,
									strokeWeight: 1
								}}

						/>*/}
		
>>>>>>> 12230e2036471dc8a8bcdb239bd4ef1099fa90cf
                    </GoogleMapReact>
                </div>
                <div className="btn-group dropright mt-2 mr-2">
                    <button className="btn btn-secondary dropdown-toggle" type="button" data-toggle="dropdown">
                    Filter by Crop
                    </button>
                    <div className="dropdown-menu">
                        <button className="dropdown-item" type="button">Almond</button>
                        <button className="dropdown-item" type="button">Pistachio</button>
                        <button className="dropdown-item" type="button">Something</button>
                    </div>
                </div>
                <div className="btn-group dropright mt-2">
                    <button className="btn btn-secondary dropdown-toggle" type="button" data-toggle="dropdown">
                    Filter by Year
                    </button>
                    <div className="dropdown-menu">
                        <button className="dropdown-item" type="button">year1</button>
                        <button className="dropdown-item" type="button">year2</button>
                        <button className="dropdown-item" type="button">year3</button>
                    </div>
                </div>
            </div>
			
			
        );
    }
}
export default SimpleMap;