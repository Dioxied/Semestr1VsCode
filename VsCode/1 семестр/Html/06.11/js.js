document.querySelector('.button').onclick = () =>{
    let r = document.querySelectorAll('input[type="radio"]')
    for(let i = 0; i < r.length; i++){
        if (r[i].checked) console.log(r[i].value);
}
}

let out = "";
for (let i = 0; i < 10; i++){
    if (i == 6) continue;
    out += i + ' ';
}
document.querySelector('#out').innerHTML = out;