/*global google*/ 
import React from "react";
import invariant from "invariant"
import coordinates from './CoordinatesSB'
const FaAnchor = require("react-icons");
const { compose, withProps, withStateHandlers, lifecycle } = require("recompose");
const {
  withScriptjs, withGoogleMap, GoogleMap, Polygon //, InfoWindow
} = require("react-google-maps");
const { InfoBox } = require("react-google-maps/lib/components/addons/InfoBox");
const { StandaloneSearchBox } = require("react-google-maps/lib/components/places/StandaloneSearchBox");

const SimpleMap = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?key=KEYHERE&v=3.exp&libraries=geometry,drawing,places",
        loadingElement: <div style={{ height: `200%` }} />,
        containerElement: <div style={{ height: `500px` }} />,
        mapElement: <div style={{ height: `100%` }} />,
  }),

	withStateHandlers(() => ({
		isOpen: false,
	  }), {
		onToggleOpen: ({ isOpen }) => () => ({
		  isOpen: !isOpen,
		})
  }),
  lifecycle({
    componentWillMount() {
      const refs = {}
	  

      this.setState({
        places: [],
        onSearchBoxMounted: ref => {
          refs.searchBox = ref;
        },
        onPlacesChanged: () => {
          const places = refs.searchBox.getPlaces();

          this.setState({
            places,
          });
        },
      })
    },
  }),
  
  
  withScriptjs  ,
  withGoogleMap
)(props =>

<div>
	<GoogleMap defaultZoom={7} clickableIcons={true} defaultCenter={{ lat: 34.4208, lng: -119.6982 }}>
	
		<Polygon
			path={coordinates}
			
			onClick={props.onToggleOpen}
			options={{
				clickable: true,
				fillColor: "#FF0000",
				fillOpacity: 0.4,
				strokeColor: "FF0000",
				strokeOpacity: 1,
				strokeWeight: 1
			}} >
			{props.isOpen && 
				<InfoBox
					 onCloseClick={props.onToggleOpen}
					 defaultPosition={{ lat: 34.4208, lng: -119.6982 }}
					 options={{ closeBoxURL: ``, enableEventPropagation: true }}
				>
				<div style={{ backgroundColor: `yellow`, opacity: 0.75, padding: `12px` }}>
				  <div style={{ fontSize: `16px`, fontColor: `#08233B` }}>
					Hello!
				  </div>
				</div>
			   </InfoBox>}
			   
	   </Polygon>
	</GoogleMap>

  <div data-standalone-searchbox="">
    <StandaloneSearchBox
      ref={props.onSearchBoxMounted}
      bounds={props.bounds}
      onPlacesChanged={props.onPlacesChanged}
    >
      <input
        type="text"
        placeholder="Enter Your City"
        style={{
          boxSizing: `border-box`,
          border: `1px solid transparent`,
          width: `240px`,
          height: `32px`,
          padding: `0 12px`,
          borderRadius: `3px`,
          boxShadow: `0 2px 6px rgba(0, 0, 0, 0.3)`,
          fontSize: `14px`,
          outline: `none`,
          textOverflow: `ellipses`,
        }}
      />
    </StandaloneSearchBox>
	
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


    <ol>
      {props.places.map(({ place_id, formatted_address, geometry: { location } }) =>
        <li key={place_id}>
          {formatted_address}
          {" at "}
          ({location.lat()}, {location.lng()})
        </li>
      )}
    </ol>

  </div>
</div>
);

{/* ////
//map autocompete tutorialhttps://medium.com/@imranhsayed/google-maps-in-react-autocomplete-location-search-draggable-marker-marker-infobox-565ab8e8cf22
//standalone search box https://tomchentw.github.io/react-google-maps/#introduction
import React from "react";
import Map from './Map'

class SimpleMap extends React.Component {
  render() {
    return(
        <Map
     google={this.props.google}
     center={{lat: 34.4208, lng: -119.6982}}
     height='500px'
     zoom={8}
    />
      )
  }
}
*/}
export default SimpleMap;