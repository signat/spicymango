<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<title>SpicyMango</title>	
	
	<link rel="stylesheet" href="./css/screen.css" type="text/css" media="screen" title="no title" charset="utf-8" />	
	<link rel="stylesheet" href="./css/plugin.css" type="text/css" media="screen" title="no title" charset="utf-8" />	
	<link rel="stylesheet" href="./css/custom.css" type="text/css" media="screen" title="no title" charset="utf-8" />	
		
</head>

<body>
	
%include header_nav
	
	<div id="content" class="xfluid">

		<div class="portlet x12">
				
			<div class="portlet-content">
				<div id="big_stats" class="clearfix">
					<div class="stat">
						<h4>Total High Alerts</h4>
						<span class="value">{{total_alert_highs}}</span>
					</div>
					<div class="stat">
						<h4>Total Medium Alerts</h4>
						<span class="value">{{total_alert_mediums}}</span>
					</div>
					<div class="stat">
						<h4>Total Low Alerts</h4>
						<span class="value">{{total_alert_lows}}</span>
					</div>
				</div>
			</div> <!-- .portlet-content -->
		</div> <!-- .portlet -->
		
		<div class="portlet x12">
			<div class="portlet-header"><h4>Alerts</h4></div>
			
			<div class="portlet-content">
				
				<table cellpadding="0" cellspacing="0" border="0" class="display" id="alerts_table">
					<thead>
						<tr>
							<th style='width: 60px;'>Level</th>
							<th style='width: 60px;'>Weight</th>
							<th>Module</th>
							<th>Date</th>
							<th>Username</th>
							<th style='width: 48%;'>Message</th>
						</tr>
					</thead>
					<tbody>
					</tbody>
					<tfoot>
						<tr>
							<th><input type="text" name="search_engine" value="Search Level" class="search_init" /></th>
							<th><input type="text" name="search_browser" value="Search Weight" class="search_init" /></th>
							<th><input type="text" name="search_platform" value="Search Module" class="search_init" /></th>
							<th><input type="text" name="search_version" value="Search Date" class="search_init" /></th>
							<th><input type="text" name="search_grade" value="Search Username" class="search_init" /></th>
							<th><input type="text" name="search_grade" value="Search Message" class="search_init" /></th>
						</tr>
					</tfoot>
				</table>
				
			</div>
		</div>
		

		
	</div> <!-- #content -->

%include footer	

<script  type="text/javascript" src="js/jquery/jquery.1.4.2.min.js"></script>
<script  type="text/javascript" src="js/slate/slate.js"></script>
<script  type="text/javascript" src="js/slate/slate.portlet.js"></script>
<script  type="text/javascript" src="js/jquery.dataTables.js"></script>
<!-- <script  type="text/javascript" src="js/plugin.js"></script> -->

<script type="text/javascript" charset="utf-8">

var asInitVals = new Array();

$(document).ready(function () 
{
        //slate.init ();
        //slate.portlet.init ();
	var oTable = $('#alerts_table').dataTable({
		"bProcessing": true,
		"sAjaxSource": "alerts.txt",
		"bDeferRender": true,
		"aaSorting": [[ 3, "desc" ]],
		"oLanguage": {
			"oPaginate": {
				"sNext": "",
				"sPrevious": ""
			}
		},
		"aoColumnDefs": [
		      { "bSortable": false, "aTargets": [ 0 ] }
		    ]
	});

	$("tfoot input").keyup( function () {
		/* Filter on the column (the index) of this element */
		oTable.fnFilter( this.value, $("tfoot input").index(this) );
	} );

	$("tfoot input").each( function (i) {
			asInitVals[i] = this.value;
		} );
		
	$("tfoot input").focus( function () {
		if ( this.className == "search_init" )
		{
			this.className = "";
			this.value = "";
		}
	} );
	
	$("tfoot input").blur( function (i) {
		if ( this.value == "" )
		{
			this.className = "search_init";
			this.value = asInitVals[$("tfoot input").index(this)];
		}
	} );

});
</script>

</body>
</html>
