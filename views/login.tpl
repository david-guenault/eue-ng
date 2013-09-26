%rebase layoutlogin globals(), title="login", css=["bootstrap/css/bootstrap.min.css", "bootstrap/css/bootstrap-responsive.min.css", "assets/styles.css", "css/login.css"], js=["vendors/modernizr-2.6.2-respond-1.1.0.min.js", "vendors/jquery-1.9.1.js", "bootstrap/js/bootstrap.min.js", "assets/scripts.js"]

<div class="container">
<form name="loginform" id="loginform" class="form-signin" method="post" action="/do_login">
<h2 class="form-signin-heading">Eue-ng</h2>
<input name="user" id="user" type="text" class="form-control" placeholder="Email address" autofocus>
<input name="password" id="password" type="password" class="form-control" placeholder="Password">
<button class="btn btn-lg btn-primary" type="submit">Sign in</button>
</form>
%if "message" in data:
<div class="alert alert-{{data["message"]["type"]}}">
{{data["message"]["content"]}}
</div>
%end
</div>
