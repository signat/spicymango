function showData()
{
var xmlhttp;
xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("data-table").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","get_data_table", true);
xmlhttp.send();
}

function autoReload()
{
	showData();
	setTimeout("autoReload()", 5000);
}
