%evenodd = 0
%def even(number):
	%if number%2==0:
		%return "evenrow"
	%else:
        	%return "oddrow"
	%end
%end	
%for line in lines:
	%evenodd += 1
  <tr>
  	<td class="{{even(evenodd)}}">{{line}}</td>
  </tr>
%end
