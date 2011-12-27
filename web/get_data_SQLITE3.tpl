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
%for line in lines:
	%line = line[0] + ": " + line[1]
	%evenodd += 1
	%r1 = r"(http://\S*(?=(]|\)|\b)))"
	%line = re.sub(r1,r'<a rel="nofollow" target="_blank" href="\1">\1</a>',line)
  <tr>
  	<td class="{{even(evenodd)}}">{{!line}}</td>
  </tr>
%end
</table>
