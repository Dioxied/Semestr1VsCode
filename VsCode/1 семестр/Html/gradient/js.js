let input1 = document.querySelector('.input1')
let input2 = document.querySelector('.input2')
let input1txt = document.querySelector('.int1')
let input2txt = document.querySelector('.int2')
let button = document.querySelector('.b1')
let body = document.querySelector('body')
let p1 = document.querySelector('.p1')
let p2 = document.querySelector('.p2')


function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }


button.onclick = function() {
    body.style.background = 'linear-gradient(to right, '+input1.value+', '+input2.value;
}
p1.onclick = function() {
    let color = getRandomColor()
    input1.value = color;
    input1.style.background = input1.value;
    input1txt.value = color;
}
p2.onclick = function() {
    let color = getRandomColor()
    input2.value = color;
    input2.style.background = input2.value;
    input2txt.value = color;
}

input1.onchange = function() {
    input1txt.value = input1.value;
    input1.style.background = input1.value;
}
input2.onchange = function() {
    input2txt.value = input2.value;
    input2.style.background = input2.value;
}

input1txt.onchange = function() {
    input1.value = input1txt.value;
    input1.style.background = input1.value;
}
input2txt.onchange = function() {
    input2.value = input2txt.value;
    input2.style.background = input2.value;
}


