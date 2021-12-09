import axios from "axios";

const PRODUCT_API_BASE_URL = "http://127.0.0.1:8000/api/products/";

class ProductService{
    getProducts(){
        return axios.get(PRODUCT_API_BASE_URL);
    }
    addProduct(product){
        return axios.post("http://127.0.0.1:8000/api/products-create/",product);
    }
    getProductByID(productID){
        return axios.get(PRODUCT_API_BASE_URL +  productID );
    }
    updateProduct(productID, products){
        return axios.post("http://127.0.0.1:8000/api/products-update/" +  productID, products);
      
    }
    deleteProduct(productID){
        return axios.delete("http://127.0.0.1:8000/api/products-delete/" +  productID);
    }
}
export default new ProductService()