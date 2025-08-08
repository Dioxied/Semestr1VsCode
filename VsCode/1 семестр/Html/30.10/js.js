document.querySelector('button').onclick = () => {
    console.log(document.querySelector("#one"));
    const myCheckBox = document.getElementById("one").value;
    console.log(myCheckBox.checked)
    if (myCheckBox.checked){
        console.log('ON')
    }
    else{
        console.log('OFF')
    }
}