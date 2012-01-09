%import re
%evenodd = 0
%def even(number):
	%if number%2==0:
		%return "evenrow"
	%else:
        	%return "oddrow"
	%end
%end
<table id="data-table">
<tr class="titles"><td>TimeStamp</td><td>Module</td><td>Username</td><td>Hostname</td><td>IRC Channel</td><td>Message</td></tr>	
%for line in lines:
	<tr class="{{even(evenodd)}}">
	<td>{{line[5]}}</td>
	<td>{{line[0]}}</td>
	<td>{{line[1]}}</td>
	<td>{{line[2]}}</td>
	<td>{{line[3]}}</td>
	%linemsg = line[4]
	%r1 = r"(http://\S*(?=(]|\)|\b)))"
	%linemsg = re.sub(r1,r'<a rel="nofollow" target="_blank" href="\1">\1</a>',linemsg)
	<td>{{!linemsg}}</td>
	</tr>

	%evenodd += 1
%end
</table>
