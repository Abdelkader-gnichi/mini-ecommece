<template>
    <div 
      class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex justify-between items-center"
      :class="{'opacity-50': product.stock === 0}"
    >
      <div>
        <h2 class="text-xl font-bold">
          {{ product.name }}
          <span 
            v-if="product.stock === 0" 
            class="text-red-500 text-sm ml-2"
          >
            Out of Stock
          </span>
        </h2>
        <p class="text-gray-600">{{ product.description }}</p>
        <p>Price: €{{ product.price }}</p>
        <p 
          class="font-bold" 
          :class="product.stock === 0 ? 'text-red-500' : 'text-green-500'"
        >
          Stock: {{ product.stock }}
        </p>
      </div>
      <div class="flex flex-col space-y-2">
        <div class="flex items-center">
          <input 
            v-model.number="stockUpdate" 
            type="number" 
            min="0" 
            class="border rounded w-20 p-1 mr-2"
            placeholder="Update Stock"
          />
          <button 
            @click="updateStock" 
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
          >
            Update
          </button>
        </div>
        <button 
          @click="deleteProduct" 
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded"
        >
          Delete
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProductItem',
    props: {
      product: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        stockUpdate: null
      }
    },
    methods: {
      updateStock() {
        if (this.stockUpdate !== null && this.stockUpdate >= 0) {
          const updatedProduct = {
            ...this.product,
            stock: this.stockUpdate
          };
          this.$emit('update-product', updatedProduct);
          this.stockUpdate = null;
        }
      },
      deleteProduct() {
        if (confirm(`Are you sure you want to delete ${this.product.name}?`)) {
          this.$emit('delete-product', this.product.id);
        }
      }
    }
  }
  </script>