const inputField = document.querySelector('.inputField');
const btn = document.querySelector('.btn');
const toDoContainer = document.querySelector('.ToDoContainer')
btn.addEventListener('click', function () {
    const item = document.createElement('li');
    item.innerHTML = inputField.value;
    toDoContainer.appendChild(item);
    item.classList.add('toDoAdded');
    inputField.value = '';

    item.addEventListener('click', () => {
        item.classList.add('toDoCompleted');
    })

    item.addEventListener('dblclick', ()=>{
        toDoContainer.removeChild(item);
    })
})