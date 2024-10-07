$('#mybtn').click(function(){
    for (var i = 0; i < 5; i++) {
        $('body').append('<div>' + '*'.repeat(i+1) + '</div>');
    }
});