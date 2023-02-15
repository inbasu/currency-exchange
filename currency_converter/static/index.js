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
    swap()
}

function swap() {
    let from = document.querySelector('#fromCur').value;
    let to = document.querySelector('#toCur').value;
    document.querySelector('#fromCur').value = to;
    document.querySelector('#toCur').value = from;
}

