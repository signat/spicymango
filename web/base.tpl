<html>
<head>
<title>SpicyMango v0.1 Alpha</title>
<script type="text/javascript" src="js/spicy.js"></script>
<link type="text/css" rel="stylesheet" href="css/spicymain.css" />
</head>
<body onload="javascript:autoReload();">
<img src="images/spicy_logo.png" align="middle"><span id="version">v0.1 Alpha</span>
<br><br>
<div align=right>
        <form id="filter">
	<select id="field">
		<option value="modname">Module</option>
		<option value="username">Username</option>
		<option value="hostname">Hostname</option>
		<option value=ircchan>IRC Channel</option>
		<option value="msg">Message</option>
	</select>
	<input type=text id="term">
                <a href="javascript: set_Filter()">Filter</a>
        </form>
</div>
<div id="data">
</div>
</body>
</html>
