<html>
<head>
<title>SpicyMango v0.1</title>
<script type="text/JavaScript">
function autoRefresh() {
	setTimeout("location.reload(true);",5000);
}
</script>
</head>
<body onload="JavaScript:autoRefresh();">
<table border="1">
%for line in lines:
  <tr>
  	<td>{{line}}</td>
  </tr>
%end
</table>
</body>
</html>
