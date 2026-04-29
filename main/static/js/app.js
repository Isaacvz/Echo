const form = document.querySelector('.form1');

// Login check

// Función para obtener el CSRF Token (indispensable en Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }   
    }
    return cookieValue;
}

async function autenticarUsuario(username, password) {
    const csrftoken = getCookie('csrftoken');

    // Creamos la variable para verificar la dirrecion de mandar los datos

    try {
        const response = await fetch('/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            console.log(data.message);
            alert("Login Succesfull."); // Redirigir al éxito
        } else {
            alert("Error: " + data.message);
        }
    } catch (error) {
        console.error("Error en la conexión:", error);
    }
}

// Esperamos que la el usuario suba la autentificacion
form.addEventListener( 'submit', async (event) => {
    // Evitamos que la pagina recargue
    event.preventDefault();
    console.log("subiendo formulario");
    // Capturamos los datos
    const user = document.querySelector('#in1').value;
    const password = document.querySelector('#in2').value;

    if (user == '' || password == '') {
        alert("Fill all the inputs");
        return;
    }

    // Llamamos la funcion async 
    console.log("Intentando autenticar el usuario a:", user);
    await autenticarUsuario(user, password);
})