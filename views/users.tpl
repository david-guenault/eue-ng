%rebase layout globals(), title="Users", css=["bootstrap/css/bootstrap.min.css", "bootstrap/css/bootstrap-responsive.min.css", "assets/styles.css", "assets/DT_bootstrap.css"], js=["vendors/modernizr-2.6.2-respond-1.1.0.min.js"], jslate=["vendors/jquery-1.9.1.js", "bootstrap/js/bootstrap.min.js", "vendors/datatables/js/jquery.dataTables.min.js", "assets/scripts.js", "assets/DT_bootstrap.js", "js/users.js"]

<div class="span9" id="content">

     <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Bootstrap dataTables</div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                        <table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="example">
                        <thead>
                            <tr>
                                <th>Email</th>
                                <th>First name</th>
                                <th>Last name(s)</th>
                                <th>is Admin ?</th>
                            </tr>
                        </thead>
                        <tbody>
                            %for u in data["users"]:
                            %   if not "firstname" in u:
                            %       u["firstname"] = ""
                            %   end
                            %   if not "lastname" in u:
                            %       u["lastname"] = ""
                            %   end
                            %   if not "acl" in u:
                            %       u["acl"]={"isAdmin": False}
                            %   else:
                            %       if not "isAdmin" in u["acl"]:
                            %           u["acl"]["isAdmin"] = False
                            %       end
                            %   end
                            %   if u["acl"]["isAdmin"]:
                            %       isAdmin = "checked"
                            %   else:
                            %       isAdmin = ""
                            %   end
                            <tr class="odd gradeX">
                                <td><a id="edit-{{u["email"]}}" href="#modalUser" data-toggle="modal">{{u["email"]}}</a></td>
                                <td>{{u["firstname"]}}</td>
                                <td>{{u["lastname"]}}</td>
                                <td class="center">
                                    <input type="checkbox" id="chk-{{u["email"]}}" {{isAdmin}} disabled>
                                </td>
                            </tr>
                            %end
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
        <form class="form-horizontal">
            <fieldset>
                <div class="control-group">
                    <label class="control-label" for="email">Email</label>
                    <div class="controls">
                        <input class="input-xlarge" id="email" type="text" value="">
                    </div>
                    <label class="control-label" for="firstname">First name</label>
                    <div class="controls">
                        <input class="input-xlarge" id="firstname" type="text" value="">
                    </div>
                    <label class="control-label" for="lastname">Last name</label>
                    <div class="controls">
                        <input class="input-xlarge" id="lastname" type="text" value="">
                    </div>
                </div>
                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">Save changes</button>
                    <button type="reset" class="btn">Cancel</button>
                </div>
            </fieldset>
        </form>
    </div>
</div>