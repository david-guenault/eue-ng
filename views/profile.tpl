%rebase layout globals(), title="accueil", css=["layout","icons"]
% if "profile" in data:
  % email=data["profile"]["email"]
  % firstname=data["profile"]["firstname"]
  % lastname=data["profile"]["lastname"]
% else:
  % email=""
  % firstname=""
  % lastname=""
% end
<div class="container-fluid" style="margin-top:70px;">
    <div class="row">
      <div class="col-md-12">
        <div class="panel panel-default">
          <div class="panel-heading">
             <h3 class="panel-title">Profile : {{email}}</h3>
        </div>
      </div>
      <div class="panel-body">      
        <form name="formprofile" id="formprofile" class="form-horizontal" role="form" method="post" action="/profil_update">
          <div class="form-group">
            <label for="password" class="col-lg-2 control-label">Password</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="password" placeholder="Password">
            </div>
          </div>
          <div class="form-group">
            <label for="firstname" class="col-lg-2 control-label">Firstname</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="firstname" placeholder="Password" value="{{firstname}}">
            </div>
          </div>
          <div class="form-group">
            <label for="lastname" class="col-lg-2 control-label">Lastname</label>
            <div class="col-lg-10">
              <input type="password" class="form-control" id="lastname" placeholder="Password" value="{{lastname}}">
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