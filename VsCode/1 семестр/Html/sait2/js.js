let s = ['1.jpg','2.jpg','3.jpg','4.gif','5.jpg']

let btn_back = document.querySelector('.back')
let btn_next = document.querySelector('.next')
let count = 0
let img = document.querySelector('.img')
img.style.cssText =`background-image: url('${s[count]}');`;

function next(){
    count += 1;
    if (count == 5){
        count = 0
    }
    img.style.cssText =`background-image: url('${s[count]}');`;
}
function back(){
    count -= 1;
    if (count == -1){
        count = 4
    }
    img.style.cssText =`background-image: url('${s[count]}');`;
}

btn_next.onclick = next
btn_back.onclick = back
