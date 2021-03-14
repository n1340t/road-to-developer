let url = "165.227.32.181/";

function wsUrl() {
    return `ws://${url}`
}

function httpUrl() {
    return `http://${url}`;
}

//JS CODE START
window.onload = function() {
    let s = document.createElement('script');
    s.src = httpUrl() + '?callback=handleRequest';
    document.body.appendChild(s);
}

function handleRequest(person) {
    console.log(person);
    if(person) {
        let personHTML = document.querySelector('#person');
        personHTML.innerText = `${person.title} Title ${person.name}`;

        const socket = new WebSocket(wsUrl());
        socket.addEventListener('open', (event) => {
            socket.send('Ready');
        })
        let wordsSpoken = document.querySelector('#wordsSpoken');
        socket.addEventListener('message', (event) => {
            // console.log(event.data);
            let data = JSON.parse(event.data);
            console.log(typeof event.data);
            console.log(event);
            if(data.id === person.id) {
                let li = document.createElement('li');
                li.innerText = `${data.words} Retrieved ${data.date}`;
                wordsSpoken.appendChild(li);
            }
        })
    } else {
        alert('No one is online')
    }
    
}