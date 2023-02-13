const curForms = document.getElementById('forms')
const result = document.getElementById('result')

curForms.addEventListener("submit", handleFormSubmit)

function handleFormSubmit(event) {
    event.preventDefault()
    const formData = new FormData(event.target)
    const xhr = new XMLHttpRequest()
    const method = 'POST'
    const URL = '/'
    xhr.responseType = 'json'
    xhr.open(method, URL)
    xhr.onload = function() { 
        result.innerText = xhr.response['result']
    }
    xhr.send(formData)
}