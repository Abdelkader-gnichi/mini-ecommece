<template>
    <div class="product-list">
      <ProductItem 
        v-for="product in products" 
        :key="product.id"
        :product="product"
        @update-product="$emit('update-product', $event)"
        @delete-product="$emit('delete-product', $event)"
      />
      <p v-if="products.length === 0" class="text-gray-500">
        No products available.
      </p>
    </div>
  </template>
  
  <script>
  import ProductItem from './ProductItem.vue';
  
  export default {
    name: 'ProductList',
    components: {
      ProductItem
    },
    props: {
      products: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  