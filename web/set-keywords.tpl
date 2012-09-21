<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<title>SpicyMango</title>	
<!--	
    <style type="text/css" title="currentStyle">
            @import "./css/jquery-ui.css";
            @import "./css/jquery-ui-1.7.2.custom.css";
    </style>
-->
    <link rel="stylesheet" href="./css/screen.css" type="text/css" media="screen" title="no title" charset="utf-8" />	
	<link rel="stylesheet" href="./css/plugin.css" type="text/css" media="screen" title="no title" charset="utf-8" />	
	<link rel="stylesheet" href="./css/custom.css" type="text/css" media="screen" title="no title" charset="utf-8" />
</head>

<body>
	
%include header_nav
	
	<div id="content" class="xfluid">
		
		<div class="portlet x6">
			<div class="portlet-header"><h4>Keywords</h4></div>
			
			<div class="portlet-content">
                <!-- Place holder where add and delete buttons will be generated -->
                <!--<div class="add_delete_toolbar" /></div>-->
                <div>
                <button id="btnAddNewRow" class="btn btn-small">Add</button>
                <button id="btnDeleteRow" class="delete_row btn btn-small">Delete</button>
				</div>
                <br />
                <table cellpadding="0" cellspacing="0" border="0" class="display" id="keyword_table">
					<thead>
						<tr>
							<th>id</th>
							<th>keyword</th>
							<th>weight</th>
						</tr>
					</thead>
					<tbody>
					</tbody>
				</table>
                
                <!-- Custom form for adding new records -->
                <form id="formAddNewRow" action="#" title="Add new keyword">
                    <label for="keyword">Keyword</label><br />
                    <input type="text" name="keyword" id="keyword" class="required" rel="1" />
                    <br />
                    <label for="weight">Weight</label><br />
                    <input type="text" name="weight" id="weight" class="required" rel="2" />
                    <input type="hidden" name="id" id="id" rel="0" />
                    <br />
                </form>

			</div>
		</div>
		
	</div> <!-- #content -->

%include footer

<script  type="text/javascript" src="js/jquery/jquery.1.4.2.min.js"></script>
<script  type="text/javascript" src="js/slate/slate.js"></script>
<script  type="text/javascript" src="js/slate/slate.portlet.js"></script>
<script  type="text/javascript" src="js/jquery.dataTables.js"></script>
<script  type="text/javascript" src="js/jquery.dataTables.editable.js"></script>
<script  type="text/javascript" src="js/jquery.jeditable.js"></script>
<script  type="text/javascript" src="js/jquery-ui.js"></script>
<script  type="text/javascript" src="js/jquery.validate.js"></script>

<script type="text/javascript" charset="utf-8">
$(function () 
{
	//slate.init ();
	//slate.portlet.init ();
	$('#keyword_table').dataTable({
		"bProcessing": true,
        	"sAjaxSource": "keywords.txt",
        	"bDeferRender": true,
		"aaSorting": [[ 1, "desc" ]],
        "oLanguage": {
                        "oPaginate": {
                                        "sNext": "",
                                        "sPrevious": ""
                                     }
                     },
        "aoColumns": [
                        /* id */ { "bSearchable": false,
                                   "bVisible": false },
                        /* keyword */ null,
                        /* weight */ null
                     ]
    	}).makeEditable({
                     sUpdateURL: "keyupdate",
                     sAddURL: "keyadd"
            });
});
</script>

</body>
</html>
