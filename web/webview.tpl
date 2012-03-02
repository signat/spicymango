<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>SpicyMango v1.0 Beta</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <link rel="stylesheet" type="text/css" href="css/ui-darkness/jquery-ui-1.8.17.custom.css" />
    <link rel="stylesheet" type="text/css" href="css/ui.jqgrid.css" />
    <link rel="stylesheet" type="text/css" href="css/spicy.css" />
    <script type="text/javascript" src="js/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-1.8.17.custom.min.js"></script>
    <script type="text/javascript" src="js/i18n/grid.locale-en.js"></script>
    <script type="text/javascript" src="js/jquery.jqGrid.min.js"></script>
    <style type="text/css">
	.ui-jqgrid tr.jqgrow td {
   		white-space: normal !important;
    		height:auto;
    		vertical-align:text-top;
    		padding-top: 5px;
		padding-bottom: 5px;
	}
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	    var refresher;
	    $("#tabs").tabs({selected: 2});
            $("#list").jqGrid({
                url: 'get_json', //url: 'execute.jsp?command=command',
                //mtype:'POST',
                datatype:'json',
		colNames : ['TimeStamp', 'Module', 'Username', 'Hostname', 'IRC Channel', 'Message'],
                colModel : [
		     {name:'timeStamp', index:'timeStamp'},
                     {name:'modname', index:'modname'},
                     {name:'username', index:'username'},
                     {name:'hostname', index: 'hostname'},
                     {name:'ircchan', index:'irchan'},
		     {name:'msg', index:'msg', width: 600}
                ],
                //width: '1000',
		shrinkToFit: false,
                //height: '550',
                pager: '#pager',
		sortname: 'timeStamp',
                sortorder: 'desc',
		rowNum: 25,
		rowList:[25,50,75,100],
                viewrecords: true,
		gridview: true,
		hidegrid: false,
		loadui: 'disable',
                caption: ''
            });
	    jQuery("#list").jqGrid('navGrid','#pager',{search:true,edit:false,add:false,del:false},
	    {},
	    {},
	    {},
	    {sopt : ['eq', 'cn'], overlay : 0},
	    {}
	    );
	    jQuery("#list").jqGrid('navButtonAdd', '#pager',{caption: "Columns", buttonicon: "ui-icon-newwin", title: "Choose Columns", onClickButton: function() {
                jQuery("#list").jqGrid('columnChooser');
            }});
	   jQuery("#liveview").button({ icons: {primary: 'ui-icon-play'}});
	   jQuery("#liveview").toggle(function () {
		 $(this).button("option", "icons", {primary: 'ui-icon-pause'});
		 $("#list").setGridParam({loadonce:true, rowNum:90000}).trigger('reloadGrid');
		 clearInterval(refresher);
		 },
		 function() {
		 $(this).button("option", "icons", {primary: 'ui-icon-play'});
		 $("#list").setGridParam({loadonce:false, datatype: 'json', rowNum:25}).trigger('reloadGrid');
		 refresher = setInterval(function(){jQuery("#list").trigger("reloadGrid");}, 5000);
		 }
	   ); 
	   $(window).bind('resize', function() {
		jQuery('#list').setGridWidth($('#tabs-1').width(), true);
		jQuery('#list').setGridHeight($(window).height()-260, true);
	   }).trigger('resize');
	   refresher = setInterval(function(){jQuery("#list").trigger("reloadGrid");}, 10000);
     });
    </script>
</head>
<body style="font-size:62.5%; background: #000;">
    <button id="liveview" style="display: inline; float: right;">LiveView</button>
    <img src="images/smlogo.png"><span id="version">v1.0 Beta</span><br>
    <span id="slogan">The Open Source Analysis Engine</span>
    <br><br>
    <div id="tabs">
	    <ul>
		<li><a href="#tabs-1">Events</a></li>
		<li><a href="#tabs-2">Analysis</a></li>
	    </ul>
	    <div id="tabs-1">
		<table id="list"><tr><td/></tr></table>
		<div id="pager"></div>
	    </div>
	    <div id="tabs-2">
		<p>Still in development</p>
	    </div>
    </div>
</body>
</html>
