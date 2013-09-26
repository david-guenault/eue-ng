%rebase layout globals(), title="Users", css=["bootstrap/css/bootstrap.min.css", "bootstrap/css/bootstrap-responsive.min.css", "assets/styles.css", "assets/DT_bootstrap.css"], js=["vendors/modernizr-2.6.2-respond-1.1.0.min.js"], jslate=["vendors/jquery-1.9.1.js", "bootstrap/js/bootstrap.min.js", "vendors/datatables/js/jquery.dataTables.min.js", "assets/scripts.js", "assets/DT_bootstrap.js", "js/users.js"]

%include sidebarusers
<div class="span9" id="content">
     <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Users</div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                        <table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="users">
                        <thead>
                            <tr>
                                <th>Email</th>
                                <th>First name</th>
                                <th>Last name(s)</th>
                                <th>is Admin ?</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>


</div>

<div id="modalUser" class="modal hide" aria-hidden="true" style="display: none;">
    <div class="modal-header">
        <button data-dismiss="modal" class="close" type="button">×</button>
        <h3>User profile</h3>
    </div>
    <div class="modal-body">
        
        <div id="usermessage" class="alert alert-block hide">
            <a class="close" data-dismiss="alert" href="#">×</a>
<!--             <h4 class="alert-heading">Error</h4>
            Best check yo self, you're not looking too good. Nulla vitae elit libero, a pharetra augue. Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
 -->        </div>        
        <form id="frmuser" method="post" action="updateuser" class="form-horizontal">
            <fieldset>
                <div class="control-group">
                    <label class="control-label" for="email">Email</label>
                    <div class="controls">
                        <input class="input-xlarge" disabled id="email" type="text" value="">
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="firstname">First name</label>
                    <div class="controls">
                        <input class="input-xlarge" id="firstname" type="text" value="">
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="lastname">Last name</label>
                    <div class="controls">
                        <input class="input-xlarge" id="lastname" type="text" value="">
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="isadmin">Admin ?</label>
                    <div class="controls">
                        <input class="input-xlarge" id="isadmin" type="checkbox" value="">
                    </div>
                </div>
            </fieldset>
            <div class="form-actions">
                <button id="usersave" type="button" class="btn btn-primary">Save changes</button>
                <button type="button" data-dismiss="modal" class="btn">Close</button>
            </div>            
        </form>
    </div>
</div>

