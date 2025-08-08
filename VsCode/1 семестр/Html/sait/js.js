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

const but = document.querySelector("button");
but.onclick = () => {
    let s = document.querySelectorAll('input')
    for(let i = 0; i < 2; i++){
        s[i].value="";
    }
}