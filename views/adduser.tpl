<div class="modal fade" id="adduser" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title">Add user</h4>
      </div>
      <div class="modal-body">
        <form name="formprofile" id="formprofile" name="formprofile" class="form-horizontal" role="form" method="post" action="/profile_add">
          <div class="form-group">
            <label for="email" class="col-lg-3 control-label">Email</label>
            <div class="col-lg-9">
              <input type="text" class="form-control" id="email" name="email" placeholder="Email">
            </div>
          </div>
          <div class="form-group">
            <label for="email" class="col-lg-3 control-label"></label>
            <div class="col-lg-9">
              <input type="text" class="form-control" id="email2" name="email2" placeholder="Repeat email">
            </div>
          </div>
          <div class="form-group">
            <label for="password" class="col-lg-3 control-label">Password</label>
            <div class="col-lg-9">
              <input type="password" class="form-control" id="password" name="password" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <label for="email" class="col-lg-3 control-label"></label>            
            <div class="col-lg-9">
              <input type="password" class="form-control" id="password2" name="password2" placeholder="Repeat Password">
            </div>
          </div>
          <div class="form-group">
            <label for="firstname" class="col-lg-3 control-label">Firstname</label>
            <div class="col-lg-9">
              <input type="text" class="form-control" id="firstname" name="firstname" placeholder="First name">
            </div>
          </div>
          <div class="form-group">
            <label for="lastname" class="col-lg-3 control-label">Lastname</label>
            <div class="col-lg-9">
              <input type="text" class="form-control" id="lastname" name="lastname" placeholder="Last name">
            </div>
          </div>
          <div class="checkbox">
            <label class="col-lg-3">
              <input type="checkbox"> Is admin ?
            </label>
          </div>       
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        <button id="sumitUser" type="button" class="btn btn-primary">Add</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->