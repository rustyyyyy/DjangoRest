// import logo from './logo.svg';
import './App.css';
import React  from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import ListProductComponent from './components/ListProductComponent';
import HeaderComponent from './components/HeaderComponent';
import FooterComponent from './components/FooterComponent';
import AddProductComponent from './components/AddProductComponent';
import updateProductComponent from './components/updateProductComponent';


function App() {
  return (
    <Router>
        <HeaderComponent />
              <div className="container"> 
                {/* <ListProductComponent /> */}
                
                  <Switch>
                    <Route exact path="/" component={ListProductComponent}></Route>
                    <Route exact path="/product" component={ListProductComponent}></Route>
                    
                    <Route  path="/addProduct/:id" component={AddProductComponent}></Route>

                    <Route  path="/updateProduct/:id" component={updateProductComponent}></Route>
                      
                  </Switch>
                 
              </div>
          <FooterComponent />
    </Router> 
  );
}

export default App;
