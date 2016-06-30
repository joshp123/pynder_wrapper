<%inherit file="pynder_web:templates/base.mako" />
<style>
    body {
      padding-top: 40px;
      padding-bottom: 40px;
      background-color: #eee;
    }

    .form-signin {
      max-width: 330px;
      padding: 15px;
      margin: 0 auto;
    }
    .form-signin .form-signin-heading,
    .form-signin .checkbox {
      margin-bottom: 10px;
    }
    .form-signin .checkbox {
      font-weight: normal;
    }
    .form-signin .form-control {
      position: relative;
      height: auto;
      -webkit-box-sizing: border-box;
              box-sizing: border-box;
      padding: 10px;
      font-size: 16px;
    }
    .form-signin .form-control:focus {
      z-index: 2;
    }
    .form-signin input[type="email"] {
      margin-bottom: -1px;
      border-bottom-right-radius: 0;
      border-bottom-left-radius: 0;
    }
    .form-signin input[type="password"] {
      margin-bottom: 10px;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }
</style>
<div class="page-header">
    <h1>Login</h1>
</div>


<div class="container">

  <form class="form-signin" action="/login/" method="post">
    <h2 class="form-signin-heading">Please sign in</h2>
    <label for="inputUsername" class="sr-only">Username</label>
    <input type="username" id="inputUsername" name="username" class="form-control" placeholder="username" required autofocus>
    <label for="inputPassword" class="sr-only">Password</label>
    <input type="password" id="inputPassword" class="form-control" name="password" placeholder="Password" required>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
  </form>

</div
