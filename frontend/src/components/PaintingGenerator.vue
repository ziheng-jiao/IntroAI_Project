<template>
    <div class="container">
        <h2>山水画生成模型</h2>
        <textarea v-model="inputText" placeholder="请输入描述..." />
        <button @click="generate">生成</button>


        <div v-if="loading">生成中...</div>


        <div v-if="image">
            <h3>生成结果</h3>
            <img :src="image" alt="Generated Painting" />
        </div>
    </div>
</template>


<script>
import { generatePainting } from '../services/api'


export default {
    data() {
        return {
            inputText: '',
            image: null,
            loading: false
        }   
    },
    methods: {
        async generate() {
            this.loading = true
            this.image = null
            try {
                const res = await generatePainting(this.inputText)
                this.image = `data:image/png;base64,${res.data.image}`
            } catch (err) {
                console.error(err)
            }
            this.loading = false
        }
    }
}
</script>


<style>
.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
}

textarea {
    width: 100%;
    height: 120px;
    margin-bottom: 10px;
}

button {
    padding: 8px 16px;
}

img {
    margin-top: 20px;
    width: 100%;
    border: 1px solid #ccc;
}
</style>