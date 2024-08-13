import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    proxy: {
      '/api/submit': {
        target: 'localhost:5328/api/submit',
        changeOrigin: true,
      }
    }
  },
  plugins: [vue()],
})
