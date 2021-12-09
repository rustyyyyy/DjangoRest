import React, { Component } from 'react';

class HeaderComponent extends Component {
    
    render() {
        return (
            <div>
                <header>
                    <nav className="nav bg-dark navbar-dark navbar-expand-md"> 
                        <div className="ml-3"> 
                            <p  className="navbar-brand text-center mb-1"> Product  </p>
                        </div>
                    </nav>
                </header>
            </div>
        );
    }
}

export default HeaderComponent;