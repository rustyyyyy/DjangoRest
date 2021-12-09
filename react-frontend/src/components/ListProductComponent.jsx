import React, { Component } from 'react';
import ProductService from '../services/ProductService';

class ListProductComponent extends Component {
    constructor(props) {
        super(props)
        this.state = {
            product: [] //creating list of product
        }
        this.addProduct = this.addProduct.bind(this);
        this.editProduct = this.editProduct.bind(this);
        this.deleteProduct = this.deleteProduct.bind(this);
    }
    editProduct(id){
        this.props.history.push(`/updateProduct/${id}`);
    }
    deleteProduct(id){
        //api call
        ProductService.deleteProduct(id).then((res) => {
            // this.props.history.push('/products');
            this.setState({product:this.state.product.filter(product => product.id !== id)});
        })
    }
    componentDidMount(){
        ProductService.getProducts().then((response) =>{
            this.setState({ product :response.data }) ;
        });
    } //filling data into list 
    addProduct(){
        this.props.history.push('/addProduct/-1')
    }//react router maintains history objects of mapping and passes as props
    //using history to manually controll 

   
    render() {
        return (
            <div className="my-3">
                <h4 >Product List</h4>
                <div className="my-3">
                    <button className="btn btn-primary" onClick={this.addProduct}>Add </button>
                </div>
                <div className="col">
                    <div className="row">
                        <table className="table table-striped table-bodered">
                            <thead>
                                <tr>
                                    <th>Product Name</th>
                                    <th>Product Specification</th>
                                    <th>Product Price</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    this.state.product.map(
                                        product =>
                                            <tr key={product.id}>
                                                <td>{product.name}</td>
                                                <td>{product.description}</td>
                                                <td>{product.price}</td>
                                                <td>
                                                    <button className="btn btn-info mr-3" onClick={ ()=> this.editProduct(product.id) }> Update </button> 
                                                    
                                                    <button className="btn btn-danger" onClick={ ()=> this.deleteProduct(product.id) }> Delete </button>
                                                </td>
                                        </tr>
                                    )
                                }
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        );
    }
}

export default ListProductComponent;