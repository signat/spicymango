var q;
var reload;
var count;

function showData()
{
var rand;
if (q == undefined){
	q = '';
}
if (count == undefined){
	count = '50';
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
xmlhttp.open("GET","get_data_table?"+q+"rand="+rand+"&count="+count, true);
xmlhttp.send();
}

function autoReload()
{
	showData();
	reload = setTimeout("autoReload()", 5000);
}

function set_Filter()
{
	var field;
	var term;
	var count;
	var query;

	field = document.getElementById('field').value;
	term = document.getElementById('term').value;
	query = "field=" + field + "&term=" + term + "&"
	
	q = query;
	clearTimeout(reload);
	autoReload(); 
}

function set_Count()
{
	count = document.getElementById('count').value;
	clearTimeout(reload);
        autoReload();
}
