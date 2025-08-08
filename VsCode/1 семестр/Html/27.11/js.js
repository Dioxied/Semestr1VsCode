// let d = ['Ivan', 37, 'ribi'];

// for (let i = 0; i < d.length; i++) {
//     document.querySelector('.out-1').innerHTML += d[i] + " ";
// }
// const div = document.querySelector('.out-1');
// let a = [34, 33, 75, 29, 5, 16, 12, 10];
// let max = 0;
// let sum = 0;
// for (let i = 0; i < a.length; i++) {
//     if (a[i] > max) {
//         max = a[i];
//     }
//     sum += a[i];
// }
// div.innerHTML = max;
// alert(sum)
const div = document.querySelector('.out-1');
let d = ['Ivan', 37, 'ribi'];

for (let i = 0; i < d.length; i++) {
    document.querySelector('.out-1').innerHTML += d[i] + " ";
}

let a = [10, 20, 30, 40, 50, 60, 70, 80];
let sum = 0;
for (let i = 0; i < a.length; i++) {
    sum += a[i];
}
console.log(a);
div.innerHTML = sum;

a.push (100); // добавляет число к массиву
a.pop(); // удаляет последнее число массива
a.splice(4, 2, 'hi'); // удаляет с (1) числа (2) элемента добавить (3) элемент(-ы)
shift() / unshift()
