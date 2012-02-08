var doReload;
var doFilter;
var q;

function showData()
{
var rand;
if (q == undefined){
	q = '';
}
rand  = new Date().getTime();
var xmlhttp;
xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("data").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","get_data_table?"+q+"rand="+rand, true);
xmlhttp.send();
}

function autoReload()
{
	showData();
	doReload = setTimeout("autoReload()", 5000);
}

function set_Filter()
{
	var field;
	var term;
	var query;

	field = document.getElementById('field').value;
	term = document.getElementById('term').value;
	query = "field=" + field + "&term=" + term + "&"
	
	q = query; 
}
