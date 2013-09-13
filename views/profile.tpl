%rebase layout globals(), title="accueil", css=["layout","icons"]
<div class="container-fluid" style="margin-top:70px;">
    <div class="row">
      <div class="col-md-12">
        <div class="panel panel-default">
          <div class="panel-heading">
             <h3 class="panel-title">Profile</h3>
        </div>
      </div>
      <div class="panel-body">      
        <form name="formprofile" id="formprofile" class="form-horizontal" role="form" method="post" action="/profil_update">
          <div class="form-group">
            <label for="inputEmail1" class="col-lg-2 control-label">Email</label>
            <div class="col-lg-10">
              <input type="email" class="form-control" id="inputEmail1" placeholder="Email">
            </div>
          </div>
          <div class="form-group">
            <label for="inputEmail2" class="col-lg-2 control-label">Repeat Email</label>
            <div class="col-lg-10">
              <input type="email" class="form-control" id="inputEmail2" placeholder="Email">
            </div>
          </div>
          <div class="form-group">
            <label for="inputPassword1" class="col-lg-2 control-label">Password</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="inputPassword1" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <label for="inputPassword2" class="col-lg-2 control-label">Repeat Password</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="inputPassword2" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <label for="inputFirstname" class="col-lg-2 control-label">Firstname</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="inputFirstname" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <label for="inputLastname" class="col-lg-2 control-label">Lastname</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="inputLastname" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <div class="col-lg-offset-2 col-lg-10">
              <button type="submit" class="btn btn-default">Validate</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>