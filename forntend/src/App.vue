<template>
  
  <!-- <RouterView /> -->
  <div id="app" class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Mini E-Commerce Inventory</h1>
    
    <ProductForm 
      @product-added="addProduct" 
      class="mb-4"
    />

    <div class="flex items-center mb-4">
      <label class="mr-2">Filter:</label>
      <select 
        v-model="stockFilter" 
        @change="filterProducts" 
        class="border p-2 rounded"
      >
        <option value="">All Products</option>
        <option value="true">In Stock</option>
        <option value="false">Out of Stock</option>
      </select>
    </div>

    <ProductList 
      :products="products"
      @update-product="updateProduct"
      @delete-product="deleteProduct"
    />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
// import { RouterView } from 'vue-router';
import ProductList from './components/ProductList.vue';
import ProductForm from './components/ProductForm.vue';
import api from './services/api';

export default {
  name: 'App',
  components: {
    
    ProductList,
    ProductForm
  },
  data() {
    return {
      products: [],
      stockFilter: ''
    }
  },
  methods: {
    async fetchProducts(inStock = null) {
      let data = []
      try {
        data = await api.getProducts(inStock);
        this.products = data.results
        console.log(this.products)
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    async addProduct(product) {
      try {
        const newProduct = await api.createProduct(product);
        this.products.push(newProduct);
        this.stockFilter = ''; // Reset filter
      } catch (error) {
        console.error('Error adding product:', error);
      }
    },
    async updateProduct(product) {
      try {
        const updatedProduct = await api.updateProduct(product.id, product);
        const index = this.products.findIndex(p => p.id === product.id);
        this.products.splice(index, 1, updatedProduct);
      } catch (error) {
        console.error('Error updating product:', error);
      }
    },
    async deleteProduct(productId) {
      try {
        await api.deleteProduct(productId);
        this.products = this.products.filter(p => p.id !== productId);
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    },
    async filterProducts() {
      const inStock = this.stockFilter === '' 
        ? null 
        : this.stockFilter === 'true';
      await this.fetchProducts(inStock);
    }
  },
  mounted() {
    this.fetchProducts();
  }
}
</script>




