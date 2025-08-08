p1 = document.querySelector('.p1');
p2 = document.querySelector('.p2');
p3 = document.querySelector('.p3');
p4 = document.querySelector('.p4');
p5 = document.querySelector('.p5');
p6 = document.querySelector('.p6');
p7 = document.querySelector('.p7');
p8 = document.querySelector('.p8');
p9 = document.querySelector('.p9');
h1 = document.querySelector('h1');
const spisok = [-1, -1, -1, -1, -1, -1, -1, -1, -1]


function prov(){
    if (spisok[0] == spisok[1] == spisok[2]){
        if (spisok[0] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[0] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[0] == spisok[3] == spisok[6]){
        if (spisok[0] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[0] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[0] == spisok[4] == spisok[8]){
        if (spisok[0] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[0] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[3] == spisok[4] == spisok[5]){
        if (spisok[3] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[3] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[6] == spisok[7] == spisok[8]){
        if (spisok[6] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[6] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[1] == spisok[4] == spisok[7]){
        if (spisok[1] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[1] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[2] == spisok[5] == spisok[8]){
        if (spisok[2] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[2] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok[6] == spisok[4] == spisok[2]){
        if (spisok[6] == 1){
            h1.innerHTML = 'Победили Крестики!'
        }
        else if (spisok[6] == 0){
            h1.innerHTML = 'Победили Нолики!'
        }
    }
    else if (spisok.indexOf(-1) == -1){
        h1.innerHTML = 'Ничья'
    }


    
}

function stepAi(){
    let randomNum;
    while (true){
    randomNum = Math.floor(Math.random() * 10);
    if (spisok[randomNum] == -1){
        break;
    }
    }
    
    if (randomNum == 0){
        p1.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 1){
        p2.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 2){
        p3.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 3){
        p4.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 4){
        p5.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 5){
        p6.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 6){
        p7.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 7){
        p8.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }
    else if (randomNum == 8){
        p9.innerHTML = '<img src="krug.png" alt="1">'
        spisok[randomNum] = 0;
    }



}

p1.onclick = () => {
    spisok[0]=1
    p1.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p2.onclick = () => {
    spisok[1]=1
    p2.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p3.onclick = () => {
    spisok[2]=1
    p3.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p4.onclick = () => {
    spisok[3]=1
    p4.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p5.onclick = () => {
    spisok[4]=1
    p5.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p6.onclick = () => {
    spisok[5]=1
    p6.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p7.onclick = () => {
    spisok[6]=1
    p7.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p8.onclick = () => {
    spisok[7]=1
    p8.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}
p9.onclick = () => {
    spisok[8]=1
    p9.innerHTML = '<img src="krest.png" alt="1">';
    stepAi()
    prov()
}


