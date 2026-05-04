const socket = new WebSocket("ws://localhost:8000/ws/chat/app/")

socket.onopen = function() {
    console.log("Conectando al chat");
}

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const chatDiv = document.getElementById('chat');
    
    // Crear elemento de mensaje
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message';
    
    // Verificar si es mi mensaje o de otro usuario
    if (data.username === window.currentUsername) {
        messageDiv.classList.add('sent');  // Azul (mi mensaje)
    } else {
        messageDiv.classList.add('received');  // Gris (otros)
    }
    
    messageDiv.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
    chatDiv.appendChild(messageDiv);
    
    // Auto-scroll al último mensaje
    chatDiv.scrollTop = chatDiv.scrollHeight;
}

socket.onclose = function() {
    console.log("Desconectando");
}

function enviarMensaje(mensaje) {
    if (mensaje.trim() === '') return;
    
    socket.send(JSON.stringify({
        'message': mensaje,
        'username': window.currentUsername
    }));
    
    // Limpiar el input después de enviar
    document.getElementById('mensajeInput').value = '';
    document.getElementById('mensajeInput').focus();
}