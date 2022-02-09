/* Buttons */
let poke_btn = document.getElementById('poke_btn')
let version_btn = document.getElementById('version_btn')
let peek_btn = document.getElementById('peek_btn')
let program_btn = document.getElementById('program_btn')

/* UI Text */
let version_text = document.getElementById('version_text')
let peek_data = document.getElementById('peek_data')

/* UI input fields */
let poke_address = document.getElementById('poke_address')
let poke_data = document.getElementById('poke_data')
let peek_address = document.getElementById('peek_address')
let program_file = document.getElementById('file_upload')

/* Sends Address and Data to Python for Poking */
function fetch_poke(event) {

    let data = {
        address: poke_address.value,
        data: poke_data.value
    }

    fetch('/poke', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'content-type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.success)
    })
}

/* Requests version number from python script */
function fetch_version(event) {
    fetch('/version', {
        method: 'GET',
        headers: { 'content-type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        update_version(Number.parseInt(data.version))
    });
}

/* Requests data at an address from python */
function fetch_peek(event) {

    let data = {
        address: peek_address.value
    }

    fetch('/peek', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'content-type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.data)
        update_peek_data(data.data)
    })
}

/* Uploads a .bin file to python */
function upload(file) {

    fetch('/program', {
        method: 'POST',
        body: file
    })
    .then(response => response.json())
    .then(success => console.log(success))
    .catch(error => console.log(error))
}

/* Updates the UI Version number */
function update_version(version) {
    version_text.value = version
}

/* Updates peek data in UI */
function update_peek_data(data) {
    peek_data.value = data
}

/* Add button event listeners */
poke_btn.addEventListener('click', fetch_poke)
version_btn.addEventListener('click', fetch_version)
peek_btn.addEventListener('click', fetch_peek)