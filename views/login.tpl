%rebase layout globals(), title="login", css=["login"]
<div class="container">
<form name="loginform" id="loginform" class="form-signin" method="post" action="/do_login">
<h2 class="form-signin-heading">Eue-ng</h2>
<input name="user" id="user" type="text" class="form-control" placeholder="Email address" autofocus>
<input name="password" id="password" type="password" class="form-control" placeholder="Password">
<button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
</form>
</div>