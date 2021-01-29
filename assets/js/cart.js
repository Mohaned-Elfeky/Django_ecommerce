let update_btns=document.getElementsByClassName('update_cart')



for (i=0 ;i<update_btns.length; i++){
    
  

    update_btns[i].addEventListener("click",function(){
        
       
       
       if(user=="Guest"){
           alert("login first")
           window.location.replace("login")
       }
       
       else{
           
        let productId = this.dataset.product
        let action = this.dataset.action
        updateOrder(productId,action)
        
       }
    })
}

document.getElementById("logout_btn").addEventListener("click",function(){
    fetch("/logout",{

        method:"post",
        headers:{

            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,

        },
        body: JSON.stringify({"logout":true})
    })
    // .then( (response) =>{
    //     return response.json()
    // })
    // .then( (data) => {
        
    //     console.log("loggedout")
        
    //  })
})


let clear_btn=document.getElementById("clear_btn");

if(clear_btn){
    clear_btn.addEventListener("click",function(){
        clearCart()
    })
}


function clearCart(){

    fetch("/clear_cart/",{

        method:"post",
        headers:{

            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,

        },
        body: JSON.stringify({"empty":"none"})
    })
    .then( (response) =>{
        return response.json()
    })
    .then( (data) => {

        location.reload()
     })
  
        
}



function updateOrder(productId,action){

    fetch("/update_cart/",{

        method:"post",
        headers:{

            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,

        },
        body: JSON.stringify({"product_id":productId,"action":action})
    })
    .then( (response) =>{
        return response.json()
    })
    .then( (data) => {

        location.reload()
     })
  
        
}


function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken')

