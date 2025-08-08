// Task 1.
// Выведите в консоль ваше имя.
// Выведите в консоль номер месяца в котором вы родились. Изучите чем отличается вывод числа и строки.
console.log('Ilya')
console.log(9)

//  Task 2
// По нажатию кнопки b-2 запускайте функцию f2, которая присваивает блоку out-2 класс .bg-2.

function f2() {
    document.querySelector('.out-2').classList.add('bg-2')
}

document.querySelector('.b-2').onclick = f2;


//  Task 3
// По нажатию кнопки b-3 запускайте функцию f3, которая удаляет у блока out-3 класс .bg-3.

function f3() {
    document.querySelector('.out-3').classList.remove('bg-3') 
}

document.querySelector('.b-3').onclick = f3;

//  Task 4
// По нажатию кнопки b-4 запускайте функцию f4, которая делает toggle класса bg-4 для блока out-4.


function f4() {
    document.querySelector('.out-4').classList.toggle('bg-4') 
}

document.querySelector('.b-4').onclick = f4;


//  Task 5
// По нажатию b-5 запускайте функцию f5, которая проверяет наличие класса bg-4 у блока out-4 (да, именно bg-4 у out-4 ). Результат - true или false, выводите в out-5.

function f5() {
    let a = document.querySelector('.out-4')
    document.querySelector('.out-5').innerHTML = a.classList.contains('bg-4')
}

document.querySelector('.b-5').onclick = f5;

//  Task 6
// Добавьте кнопку .b-6, которая запускает функцию f6. Функция создает через createElement div c текстом 25 и добавляет его через append в out-6.


function f6() {
    document.querySelector('.out-6').innerHTML='';
    let div = document.createElement('div');
    div.innerHTML = '25';
    document.querySelector('.out-6').append(div);
}

document.querySelector('.b-6').onclick = f6;

//  Task 7
// Добавьте кнопку .b-7, которая запускает функцию f7. Функция создает через createElement div c текстом 12 и добавляет ему класс bg-7. Созданный div добавляется в out-7.


function f7() {
    document.querySelector('.out-7').innerHTML='';
    let div = document.createElement('div');
    div.classList.add('bg-7')
    div.innerHTML = '12';
    document.querySelector('.out-7').append(div);
}

document.querySelector('.b-7').onclick = f7;

// Task 8 ============================================
/*  Добавьте на блок .div-8 событие клик. При клике - увеличивайте ширину блока на 5px. Каждый клик - увеличение ширины на 5px. 10 кликов - на 50px. Ширину выводите в out-8. */

let w8 = 75;

function t8() {
    let div = document.querySelector('.div-8');
    w8+=5;
    div.style.width = w8+'px';
    document.querySelector('.out-8').innerHTML = w8;
}

// ваше событие здесь!!!
document.querySelector('.div-8').onclick = t8;

