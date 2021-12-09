import React, { Component } from 'react';

class FooterComponent extends Component {
    render() {
        return (
            <div >
                <footer className="footer fixed-bottom" >
                    <div className="text-center">
                        <span className="text-muted"> footer  </span>
                    </div>
                </footer>
            </div>
        );
    }
}

export default FooterComponent;