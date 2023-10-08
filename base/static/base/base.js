var btns = document.getElementsByClassName('action-button')

for(var i=0;i<btns.length;i++){
    btns[i].addEventListener('click', function (){
        console.log('Hi')
    })
}