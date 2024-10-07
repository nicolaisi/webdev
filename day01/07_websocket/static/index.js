$('#myname').click(function(){
    console.log("Clicked jQuery click function");
    //let mycolor = document.getElementById("myname").style.color;
    let mycolor = $("#myname").css("color");
    console.log(mycolor);
    
    if (mycolor == "rgb(255, 0, 0)") {
        $("#myname").css("color", "blue");
    } else {
        $("#myname").css("color", "red");
    }
});


$(document).ready(function() {
    var ws = new WebSocket("ws://0.0.0.0:8888/websocket");
      ws.onopen = function() {
         ws.send("0");
      };
      ws.onmessage = function (evt) {
         $("#mydata").text(evt.data)
      };
});



