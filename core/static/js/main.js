
/*
window.onload = function() {
    if (window.jQuery) {  
        // jQuery is loaded  
        alert("Yeah!");
    } else {
        // jQuery is not loaded
        alert("Doesn't Work");
    }
} 
*/

$(function(){
    $("audio").on("play", function() {
        $("audio").not(this).each(function(index, audio) {
            
            
            


            audio.pause();
            audio.currentTime = 0;
           
            
        });
    });
});