document.addEventListener('DOMContentLoaded',()=>{
    var socket = io.connect('http://'+document.domain + ':' +location.port);

    // socket.on('connect', () => {
    //     socket.send("Iam  connected");
    // });

    socket.on('message', data => {
        const p = document.createElement('p');
        const span_username = document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');
        span_username.innerHTML = data.username;
        span_timestamp.innerHTML = data.time_stamp;
        p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
        document.querySelector('#display-message-section').append(p);
        // console.log('message received: ${data}');
    });

    socket.on('some-event', data => {
        console.log(data);
    });

    // Send message 
    document.querySelector('#send_message').onclick = () => {
        socket.send({'msg': document.querySelector('#user_message').value,'username': username });
    }


}) 