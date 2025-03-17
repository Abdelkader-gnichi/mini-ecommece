<template>
  <form @submit.prevent="submitProduct" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
        Name *
      </label>
      <input 
        v-model="product.name" 
        type="text" 
        required 
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
      />
    </div>
    
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="description">
        Description
      </label>
      <textarea 
        v-model="product.description" 
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
      ></textarea>
    </div>
    
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="price">
        Price *
      </label>
      <input 
        v-model.number="product.price" 
        type="number" 
        step="0.01" 
        min="0" 
        required 
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
      />
    </div>
    
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="stock">
        Stock *
      </label>
      <input 
        v-model.number="product.stock" 
        type="number" 
        min="0" 
        required 
        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
      />
    </div>
    
    <button 
      type="submit" 
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Add Product
    </button>
  </form>
</template>

<script>
import api from '@/services/api.js'; // Ensure the path to api.js is correct

export default {
  name: 'ProductForm',
  data() {
    return {
      product: {
        name: '',
        description: '',
        price: null,
        stock: null
      }
    };
  },
  methods: {
    async submitProduct() {
      try {
        const response = await api.createProduct(this.product);
        alert('Product added successfully!');
        // Optionally reset the form after successful submission
        this.product = {
          name: '',
          description: '',
          price: null,
          stock: null
        };
        console.log(response);
      } catch (error) {
        console.error('Error creating product:', error);
        alert('Failed to add product.');
      }
    }
  }
};
</script>
