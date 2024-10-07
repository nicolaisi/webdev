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

setInterval(function() {
    $.ajax({
        url: '/data/',
        type: 'GET',
        success: function (response) {
            console.log(response);
            $("#mydata").text(response["data"]);
        },
        error: function () {
            console.log("error");
        }
    });
}, 1000); // every one second
