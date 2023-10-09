var btns = document.getElementsByClassName('action-button')

for(var i=0;i<btns.length;i++){
    btns[i].addEventListener('click', function (){
        var action = this.dataset.action
        update(action)
    })
}

function update(action){
    url = '/update-count/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(
            {'action':action}
        ),
    })

    .then((response) => {
        return response.json()
    })
    
    .then((data) => {
        console.log(data)
        location.reload()
    })
}