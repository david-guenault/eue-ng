$(function() {
    $("a[id*='edit-']").click(function(){
        user = $(this).html();
        // get user data with ajax call
        $.getJSON('user/'+user)
            .done(function(json){
                //now fill in modal box and display 
                
            })
            .fail(function(jqxhr, textStatus, error){
                var err = textStatus + ", " + error;
                console.log( "Request Failed: " + err );                
            });

    });
});