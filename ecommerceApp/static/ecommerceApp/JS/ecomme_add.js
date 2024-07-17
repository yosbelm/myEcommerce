console.log('hi')

var updButtons = document.getElementsByClassName('update-cart')

for(var i=0; i<updButtons.length; i++){
    updButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, '----------------', action)

        console.log(usuario)
        if(usuario == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    var url = 'updateitem'
    console.log('Url****************', url)
    fetch(url, {
        method: "POST", 
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}