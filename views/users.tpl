%rebase layout globals(), title="users", css=["layout","icons","glyphicon","buttonbar"]
<script type="text/javascript">
    $(document).ready(function(){
        $('#lnkadduser').click(function(){
            $('#adduser').modal();
        });

        $('#sumitUser').click(function(){
            $('#formprofile').submit();
        });
        
    })
</script>
<div class="container-fluid" style="margin-top:70px;">
    <div class="row">
        <div class="col-md-12 well">
            &nbsp;<span class="glyphicon glyphicon-chevron-right"> Users management</span>
        </div>
        <div class="col-md-12">
            <div class="btn-group col-md-offset-10">
                <button type="button" class="btn-bar-left btn btn-default"><span class="glyphicon glyphicon-user glyphicon-white"></span></button>
                <a id="lnkadduser" href="#" type="button" class="btn btn-default st" data-toggle="tooltip" title data-original-title="Create new user"><span class="glyphicon glyphicon-plus-sign"></span></a>
                <button type="button" class="btn btn-default st" data-toggle="tooltip" title data-original-title="Remove selected users"><span class="glyphicon glyphicon-minus-sign"></span></button>
            </div>
        </div>
        <div></div>
        <div class="col-md-10 col-md-offset-1">
            <table class="table table-hover table-striped">
                <thead> 
                    <tr>
                        <th><input type="checkbox"></th>
                        <th>First name</th>
                        <th>Last name</th>
                        <th>Email</th>
                        <th>Is admin ?</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>First name</td>
                        <td>Last name</td>
                        <td>Email</td>
                        <td>Is admin ?</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
%include adduser.tpl