
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ marker }) => <div>{marker}</div>;

class SimpleMap extends Component {
    static defaultProps = {
        center: {
            lat: 34.42,
            lng: 119.69
        },
        zoom: 8

    };

    render() {
        return (
            // Important! Always set the container height explicitly
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
                </GoogleMapReact>
            </div>
        );
    }
}
export default SimpleMap;