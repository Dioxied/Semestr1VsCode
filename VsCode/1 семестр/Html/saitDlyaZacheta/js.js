//--------------------------Верхнее меню------------------------
let btn_boss = document.querySelector('.btn-1')
let btn_minecraft = document.querySelector('.btn-2')
let btn_mobs = document.querySelector('.btn-3')

let logo1 = document.querySelector('.boss')
let logo2 = document.querySelector('.minecraft')
let logo3 = document.querySelector('.mobs')
let s_header = [logo1, logo2, logo3]

btn_boss.onclick = () =>{
    s_header[1].style.cssText = "display: none";
    s_header[2].style.cssText = "display: none";
    s_header[0].style.cssText = "display: flex";
}
btn_minecraft.onclick = () =>{
    s_header[0].style.cssText = "display: none";
    s_header[2].style.cssText = "display: none";
    s_header[1].style.cssText = "display: flex";
}
btn_mobs.onclick = () =>{
    s_header[1].style.cssText = "display: none";
    s_header[0].style.cssText = "display: none";
    s_header[2].style.cssText = "display: flex";
}

//--------------------------Верхнее меню------------------------
//--------------------------Меню Боссы--------------------------

const items = document.querySelectorAll('.item');
items.forEach (item => {
    item.addEventListener('mouseover', () => {
        removeFocus();
        item.classList.add('selected');
        })
    removeFocus = () => {
        items.forEach(item => {
            item.classList.remove('selected');
        })
    }
})
//-------------------------Меню Мобы-----------------------------

let sM1 = ['1z.jpg','2z.jpg','3z.jpg','4z.jpg','5z.jpg']

let btn_backM1 = document.querySelector('.mobs-container-1-back')
let btn_nextM1 = document.querySelector('.mobs-container-1-next')
let countM1 = 0
let imgM1 = document.querySelector('.mobs-container-1-img')
imgM1.style.cssText =`background-image: url('${sM1[countM1]}');`;

function nextM1(){
    countM1 += 1;
    if (countM1 == 5){
        countM1 = 0
    }
    imgM1.style.cssText =`background-image: url('${sM1[countM1]}');`;
}
function backM1(){
    countM1 -= 1;
    if (countM1 == -1){
        countM1 = 4
    }
    imgM1.style.cssText =`background-image: url('${sM1[countM1]}');`;
}

btn_nextM1.onclick = nextM1
btn_backM1.onclick = backM1
2
let sM2 = ['1d.jpg','2d.jpg','3d.jpg','4d.jpg','5d.jpg']

let btn_backM2 = document.querySelector('.mobs-container-2-back')
let btn_nextM2 = document.querySelector('.mobs-container-2-next')
let countM2 = 0
let imgM2 = document.querySelector('.mobs-container-2-img')
imgM2.style.cssText =`background-image: url('${sM2[countM2]}');`;

function nextM2(){
    countM2 += 1;
    if (countM2 == 5){
        countM2 = 0
    }
    imgM2.style.cssText =`background-image: url('${sM2[countM2]}');`;
}
function backM2(){
    countM2 -= 1;
    if (countM2 == -1){
        countM2 = 4
    }
    imgM2.style.cssText =`background-image: url('${sM2[countM2]}');`;
}

btn_nextM2.onclick = nextM2
btn_backM2.onclick = backM2
//-----------------------------Меню мобы-----------------------------------



