let inputIn = document.querySelector(".input_in");
let button = document.querySelector("button");
let outq = document.querySelector(".out");
button.onclick = function(){
    outq.innerHTML = inputIn.value;
    inputIn.value='';
    
}

