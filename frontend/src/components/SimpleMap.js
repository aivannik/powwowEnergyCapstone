import React, { Component } from 'react';
import coordinates from './CoordinatesSB'
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker,Polygon } from "react-google-maps"


const SimpleMap = compose(
    withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?key=AIzaSyD2zir3KVWBzE4GjkMN_x9RDrp_uEKCboU",
        loadingElement: <div style={{ height: `200%` }} />,
        containerElement: <div style={{ height: `500px` }} />,
        mapElement: <div style={{ height: `100%` }} />,
    }),
    withScriptjs,
    withGoogleMap

)((props) =>
	<div>
		<GoogleMap defaultZoom={7} defaultCenter={{ lat: 34.4208, lng: -119.6982 }}>
			{/*} {props.isMarkerShown && <Marker position={{ lat: 41.015137, lng: 28.979530 }} />}*/}
			<Polygon
				path={coordinates}
				options={{
					fillColor: "#FF0000",
					fillOpacity: 0.4,
					strokeColor: "FF0000",
					strokeOpacity: 1,
					strokeWeight: 1
				}} />
		</GoogleMap>
		
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
)

export default SimpleMap;