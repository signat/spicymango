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
			<div class="portlet-header"><h4>Events</h4></div>
			
			<div class="portlet-content">
				
				<table cellpadding="0" cellspacing="0" border="0" class="display" rel="datatable" id="events_table">
					<thead>
						<tr>
							<th>Module</th>
							<th>Date</th>
							<th>Username</th>
							<th>Message</th>
						</tr>
					</thead>
					<tbody>
						{{!event_rows}}
					</tbody>
				</table>
				
			</div>
		</div>
		

		
	</div> <!-- #content -->

%include footer	
