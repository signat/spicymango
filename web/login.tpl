<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>SpicyMango v1.0 Beta</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <link rel="stylesheet" type="text/css" href="css/ui-darkness/jquery-ui-1.8.17.custom.css" />
    <link rel="stylesheet" type="text/css" href="css/login.css" />
    <script type="text/javascript" src="js/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-1.8.17.custom.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
		$("#login_submit").button();
		$("#login-box").hide();
		$("#login-box").fadeIn(3000);
            });
    </script>
</head>
	<body style="font-size:62.5%; background: #000;">
		<div id="login-box">
			<img src="images/smlogo.png">
			<form action='/login-check' method='POST'>
				<label>username</label><input type="text" name="user" style="width: 120px;"><br>
				<label>password</label><input type="password" name="pass" style="width: 120px;">
				<button type=submit id="login_submit">Login</button>
			</form>
		</div>
	</body>
</html>
