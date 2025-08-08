// const toggle = document.querySelector('.toggle');
// toggle.onclick = function() {
//     this.classList.toggle('three');
// }
// let a = document.createElement('div');
// a.innerHTML = 'Heelo1'
// a.classList.add('one')
// document.querySelector('.test').appendChild(a);

const header = document.querySelector('#header');
const btn = document.querySelector('#submit');
btn.addEventListener('click', function() {
    document.body.style.backgroundColor = 'red';
    header.classList.add('one')});

document.querySelector('.t').onclick = () => {
    document.querySelector('.ones').style.display = 'flex'
    document.querySelector('body').classList.add('ooo');

}