import axios from 'axios';
import config from '@/config';


export default {
  async getProducts(inStock = null) {
    const url = inStock !== null 
      ? `${config.backendUrl}api/products/?in_stock=${inStock}` 
      : `${config.backendUrl}api/products/`;
    
    const response = await axios.get(url);
    return response.data;
  },

  async createProduct(product) {
    const response = await axios.post(`${config.backendUrl}api/products/`, product);
    return response.data;
  },

  async updateProduct(id, product) {
    const response = await axios.put(`${config.backendUrl}api/products/${id}/`, product);
    return response.data;
  },

  async deleteProduct(id) {
    const response = await axios.delete(`${config.backendUrl}api/products/${id}/`);
    return response.data;
  }
}
