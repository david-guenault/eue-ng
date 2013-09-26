$(function() {
    $("#users").on("click", "tbody tr", function(event){
        // get user email
        user = $(this).children()[0].textContent
        // clean up form 
        $("#email").val("");
        $("#firstname").val("");
        $("#lastname").val("");
        $("#isadmin").val("");                
        $('#isadmin').prop('checked', false);                                
        // get user data with ajax call
        $.getJSON('user/'+user)
            .done(function(json){
                //now fill in modal box and display 
                $("#email").val(json.email);
                $("#firstname").val(json.firstname);
                $("#lastname").val(json.lastname);
                $("#isadmin").val(json.isAdmin);                
                $('#isadmin').prop('checked', json.isAdmin);                                
            })
            .fail(function(jqxhr, textStatus, error){
                var err = textStatus + ", " + error;
                console.log( "Request Failed: " + err );                
            });

        $("#usermessage").hide();

    });

    $("#usersave").click(function(){
        data = {
            email:$("#email").val(),
            firstname:$("#firstname").val(),
            lastname:$("#lastname").val(),
            isadmin:$("#isadmin").is(':checked')
        };

        $.post( "updateuser", data, function(data){
            $("#usermessage").show();
            $("#usermessage").removeClass("alert-success");                
            $("#usermessage").removeClass("alert-error");                                
            if (data.result){
                // display success message and close modal box
                $("#usermessage").addClass("alert-success");
                $("#usermessage").html("<h4>Success</h4>");
                // wait 1,5 second before closing and reloading data table
                window.setTimeout(ajaxusersreload, 1500);
            }else{
                // display error message
                $("#usermessage").addClass("alert-error");
                $("#usermessage").html("<h4>Error</h4>");
            }
        },"json");
    });

    function ajaxusersreload(){
        // discard error message
        $("#usermessage").hide();
        // close modal form
        $("#modalUser").modal('hide');
        // reload dataTable
        $.getJSON('users/jsondt')
        .done(function(json){
            dt = $("#users").dataTable();
            dt.fnClearTable();
            dt.fnAddData(json.aaData);
            dt.fnDraw();        
        })
    }

    // init data table and load data

    optTable = {
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "sPaginationType": "bootstrap",
        "oLanguage": {"sLengthMenu": "_MENU_ records per page"},
        "bProcessing": true,
        "sAjaxSource": 'users/jsondt',
        "aoColumns": [
            { "mData": "email" , "mRender": function (data, type, full ) {
                return '<a href="#modalUser" data-toggle="modal" class="email">'+data+'</a>'
            }},
            { "mData": "firstname" },
            { "mData": "lastname" },
            { "mData": "isAdmin", "mRender": function (data, type, full ) {
                if (data == true){
                    return '<input type="checkbox" checked disabled />';
                }else{
                    return '<input type="checkbox" disabled />';
                }}}            
        ]
    }

    $('#users').dataTable(optTable);

});