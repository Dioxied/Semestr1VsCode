const button = document.querySelector(".button");
const input = document.querySelector(".input-1");

button.onclick = () => { //Функцию можно записать в таком виде
    let num = input.value;

    if (num < 16){
        document.querySelector(".out").innerHTML = "Школоло";
    }

    else if (num > 16 && num <30){
        document.querySelector(".out").innerHTML = "Эщкерембус";
    }
    
    else{
        document.querySelector(".out").innerHTML = "Чивапчес";
    }
}