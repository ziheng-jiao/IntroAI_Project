import axios from "axios"

const api = axios.create({
baseURL: 'http://localhost:5000/api'
})

export function generatePainting(text) {
return api.post('/generate', { text })
}