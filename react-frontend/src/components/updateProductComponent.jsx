import React, { Component } from 'react';
import ProductService from '../services/ProductService';

class AddProductComponent extends Component {
    constructor(props) {
        super(props)
        this.state = {
            id:this.props.match.params.id,
           name:'',
           description:'',
           price:''
        }
        //binding
        this.changeNameHandler = this.changeNameHandler.bind(this);
        this.changedescriptionHandler = this.changedescriptionHandler.bind(this);
        this.changePriceHandler = this.changePriceHandler.bind(this);
        this.updateProduct = this.updateProduct.bind(this);
        this.cancel = this.cancel.bind(this);
    }
    componentDidMount(){
        ProductService.getProductByID(this.state.id).then((response ) =>{
            let product = response.data;
            this.setState({
                name : product.name,
                description : product.description,
                price : product.price
            })
        });
    }
    updateProduct = (event) => {
        event.preventDefault();
        let product ={name:this.state.name, description:this.state.description, price:this.state.price };
        console.log('product update -> ' + JSON.stringify(product));   
        ProductService.updateProduct(this.state.id,product).then((res) =>{
            this.props.history.push('/product');
        });
    }
    cancel(){
        this.props.history.push('/product')
    }
    
    changeNameHandler= (event) =>{
        this.setState({name:event.target.value});
    }
    changedescriptionHandler =(event) =>{
        this.setState({description:event.target.value});
    }
    changePriceHandler = (event) => {
        this.setState({price:event.target.value});
    }
   

    render() {
        return (
            <div className="my-3">
               <div className="row"> 
                    <div className="card col-md-6 offset-md-3"> 
                        <div className="text-center mt-3"> <h4>Update Product </h4> </div>
                        <div className="card-body"> 
                            <form method="post">
                                <div className="form-group">
                                    <label>Name</label>
                                    <input placeholder="Name"  name = "name" className="form-control" 
                                        value={this.state.name} onChange={this.changeNameHandler}  />
                                </div>
                                <div className="form-group">
                                    <label>description</label>
                                    <input placeholder="description"  name = "description" className="form-control" 
                                        value={this.state.description} onChange={this.changedescriptionHandler}  />
                                </div>
                                <div className="form-group">
                                    <label>Price</label>
                                    <input placeholder="Price"  name = "price" className="form-control" 
                                        value={this.state.price} onChange={this.changePriceHandler}  />
                                </div>
                                <button className="btn btn-success mr-3" onClick={this.updateProduct}>Save</button>
                                <button className="btn btn-danger" onClick={this.cancel}>Cancel</button>

                            </form>                                            
                        </div>
                    </div>
               </div>
            </div>
        );
    }
}

export default AddProductComponent;