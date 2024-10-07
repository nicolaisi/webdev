function changeColor() {
    console.log("Clicked changeColor() function");
    //let mycolor = document.getElementById("myname").style.color;
    let mycolor = $("#myname").css("color");
    console.log(mycolor);
    
    if (mycolor == "rgb(255, 0, 0)") {
        $("#myname").css("color", "blue");
    } else {
        $("#myname").css("color", "red");
    }
}