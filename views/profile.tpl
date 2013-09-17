%rebase layout globals(), title="accueil", css=["layout"]
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
    <div class="col-md-12 well">
      &nbsp;<span class="glyphicon glyphicon-chevron-right"> Profile : {{email}}</span>
    </div>
    <div class="col-md-8 col-md-offset-1">      
      <form name="formprofile" id="formprofile" name="formprofile" class="form-horizontal" role="form" method="post" action="/profile_update">
        <div class="form-group">
          <label for="password" class="col-lg-2 control-label">Password</label>
          <div class="col-lg-10">
            <input type="password" class="form-control" id="password" name="password" placeholder="Password">
          </div>
        </div>
        <div class="form-group">
          <label for="firstname" class="col-lg-2 control-label">Firstname</label>
          <div class="col-lg-10">
            <input type="text" class="form-control" id="firstname" name="firstname" placeholder="First name" value="{{firstname}}">
          </div>
        </div>
        <div class="form-group">
          <label for="lastname" class="col-lg-2 control-label">Lastname</label>
          <div class="col-lg-10">
            <input type="text" class="form-control" id="lastname" name="lastname" placeholder="Last name" value="{{lastname}}">
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