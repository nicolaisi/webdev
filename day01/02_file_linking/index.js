function changeColor() {
    console.log("Clicked changeColor() function");
    let mycolor = document.getElementById("myname").style.color; 

    if (mycolor == "red") {
        document.getElementById("myname").style.color="blue";
    } else {
        document.getElementById("myname").style.color="red";
    }
}