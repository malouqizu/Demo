<%
function mailcheck(mail)
  dim flag
  flag=true
  if (mail="") then flag=false 
  if (len(mail)<5) then flag=false
  if (instr(1,mail,"@")<2) or (instr(1,mail,"@")<>instrrev(mail,"@")) or (instr(1,mail,"@")>(len(mail)-3)) then flag=false
  if (instr(1,mail,".")<4) or (instr(1,mail,"@")>instr(1,mail,".")) then flag=false
  if ((instr(instr(1,mail,".")+1,mail,"."))<>(instrrev(mail,"@"))) and (instr(1,mail,".")<>instrrev(mail,".")) then flag=false
  for checkletter=1 to len(mail)
    letter=mid(mail,checkletter,1)
    if (letter<>chr(46)) and (letter<>"_") then
       if (letter<chr(48)) or ((letter>chr(57)) and (letter<chr(64))) or ((letter>chr(90) and (letter<chr(97))) or (letter>chr(122))) then flag=false
    end if 
   next
  mailcheck=flag
end function
%>