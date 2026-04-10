const in1 = document.querySelector('#in1');
const in2 = document.querySelector('#in2');
const form = document.querySelector('#form1');

// Login check

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const completeData = Object.fromEntries(formData.entries());
    const API_URL = window.location.hostname == 'localhost'
    ? 'http://127.0.0.1:8000/'
    : '';

    fetch(`API_URL`/config/views.py, {
        method: 'POST',
        body: JSON.stringify(completeData),
        headers: {
            'Content-Type': 'application/json'
            }
    })
    .then(response => response.json())
    .then(data => {
        if(data.status === "success") {
            box2.classList.remove('hide');
        } else {
            
        }
    })
    .catch(error => console.error("Error:", error));
});