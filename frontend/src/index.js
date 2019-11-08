import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
<<<<<<< HEAD
// class Square extends React.Component {
//     render() {
// 	return (
//       <button className="square">
// 	  {/* TODO */}
//       </button>
// 		);
//     }
// }

// class Board extends React.Component {
//     renderSquare(i) {
// 	return <Square />;
//     }

//     render() {
// 	const status = 'Next player: X';

// 	return (
//       <div>
//       <div className="status">{status}</div>
//         <div className="board-row">
//           {this.renderSquare(0)}
//           {this.renderSquare(1)}
//           {this.renderSquare(2)}
//         </div>
//         <div className="board-row">
// 	    {this.renderSquare(3)}
// 	    {this.renderSquare(4)}
// 	    {this.renderSquare(5)}
//         </div>
//         <div className="board-row">
// 	    {this.renderSquare(6)}
// 	    {this.renderSquare(7)}
// 	    {this.renderSquare(8)}
//         </div>
//       </div>
// 		);
//     }
// }

// class Game extends React.Component {
//     render() {
// 	return (
//       <div className="game">
//         <div className="game-board">
//           <Board />
//         </div>
//         <div className="game-info">
//       <div>{/* status */}</div>
//       <ol>{/* TODO */}</ol>
//         </div>
//       </div>
// 		);
//     }
// }

 // This component is only a placeholder for now
 // It should be replaced with Google map area later
  // class MapArea extends Component {
  //   render() {
  //     return (
  //       <div className="card">
  //         <h5 className="card-header">placeholder</h5>
  //         <div className="card-body">
  //           <p className="card-text">This is only a placeholder for Google map</p>
  //         </div>
  //       </div>
  //     );
  //   }
  // }

  // Text box for Analysis text
  class Analysis extends Component {
    render() {
      const analysisText = 'analysis text goes here';
      return (
        <div className="card">
          <h5 className="card-header">Water Efficiency</h5>
          <div className="card-body">
            <p className="card-text">analysis text goes here!</p>
            <PDFDownloadLink 
              document={<MyDocument data={analysisText}/>}
              fileName="efficiencyAnalysis.pdf"
              className="btn btn-primary"
            >
              Download PDF
            </PDFDownloadLink>
          </div>
        </div>
      );
    }
  }

  class MainBody extends Component {
    render() {
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
  }

=======
import App from './App';
>>>>>>> 12230e2036471dc8a8bcdb239bd4ef1099fa90cf


ReactDOM.render(<App />, document.getElementById('root'));