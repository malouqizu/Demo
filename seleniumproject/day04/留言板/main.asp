<!--#include file="datastore.asp"-->
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta name="GENERATOR" content="Microsoft FrontPage 4.0">
<meta name="ProgId" content="FrontPage.Editor.Document">
<title>��ӭ�����ҵ����԰�</title>
</head>
<body>


<p align="center"><img border="0" src="banner.gif" width="700" height="60" align="center"></p>
<%
  if len(Request.QueryString)=0 then
     dim strquery
     strquery=Request.form("d1")
     dim intdays
     select case strquery
         case "���һ�췢�������"
           intdays=0
         case "������췢�������"
           intdays=3
         case "���һ�ܷ��������"
           intdays=7
         case "���һ�·��������"
           intdays=8
         case "��������"
           intdays=9
      end select
   else
    intdays=cint(left(Request.QueryString,1))
  end if
%>
<form action="main.asp" method=post>
 <p align="center">
 <select size="1" name="D1">
   <%
    select case intdays
      case 0
        Response.Write "<option>���һ�췢�������</option><option>������췢�������</option><option>���һ�ܷ��������</option><option>���һ�·��������</option><option>��������</option>"
      case 9
        Response.Write "<option>��������</option><option>���һ�췢�������</option><option>������췢�������</option><option>���һ�ܷ��������</option><option>���һ�·��������</option>"
      case 8
        Response.Write "<option>���һ�·��������</option><option>���һ�췢�������</option><option>������췢�������</option><option>���һ�ܷ��������</option><option>��������</option>"
      case 7
        Response.Write "<option>���һ�ܷ��������</option><option>���һ�췢�������</option><option>������췢�������</option><option>���һ�·��������</option><option>��������</option>"
      case 3
        Response.Write "<option>������췢�������</option><option>���һ�췢�������</option><option>���һ�ܷ��������</option><option>���һ�·��������</option><option>��������</option>"
    end select
   %>
 </select>
 <input type="submit" value="����" name="B1">&nbsp;&nbsp;<a href="search.asp"><font size="2">�߼�����</font></a> 
 </form>
 <%
 dim inteachpage
 inteachpage=6
 dim objconnect
 set objconnect=server.CreateObject("adodb.connection")
 objconnect.open strconnect
 dim objrs
 set objrs=server.CreateObject ("adodb.recordset")

 select case intdays
   case 9
      objrs.Open "select * from content order by date desc",objconnect,1,2
   case 0
      objrs.Open "select * from content where now()-date<1 order by date desc",objconnect,1,2
   case 3
      objrs.Open "select * from content where now()-date<3 order by date desc",objconnect,1,2  
   case 7
      objrs.Open "select * from content where now()-date<7 order by date desc",objconnect,1,2
   case 8
      objrs.Open "select * from content where now()-date<30 order by date desc",objconnect,1,2
 end select
 dim intpageno
 if mid(Request.QueryString,2)<>"" then
   intpageno=cint(mid(Request.QueryString,2))
 else 
   intpageno=1
 end if  
 
 dim intrscount
 intrscount=objrs.recordcount
 if intrscount<>0 then
   objrs.Move (intpageno-1)*6
   dim intrsno
   intrsno=0
   while (not objrs.EOF ) and intrsno<6
      Response.Write "<div align=""center""><center><table border=""1"" width=""700""><tr><td width=""125"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">���֣�"
      Response.Write (objrs("name"))
      Response.Write "</td><td width=""195"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">���䣺"
      Response.Write (objrs("mail"))
      Response.Write "</td><td width=""358"" bgcolor=""F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">�������ڣ�"
      Response.Write (objrs("date"))
      Response.Write "</td></tr><tr><td width=""678"" bgcolor=""#E3F1D1"" colspan=""3"">"
      Response.Write (objrs("text"))
      Response.Write "</td></tr></table></center></div>"
      intrsno=intrsno+1
      objrs.Movenext
   wend
 else
  Response.Write "û�з������������ԡ�"
 end if
 
 objrs.Close
 set objrs=nothing
 objconnect.Close
 set objconnect=nothing
 %>


<font size="2" ><P align="right">
<%
dim intpagecount
intpagecount=intrscount\6
if (intpagecount*6)<intrscount then intpagecount=intpagecount+1
Response.Write "��" & intpagecount & "ҳ"
if intpageno=1 then
   Response.Write "   ��<font face=webdings>9</font><font face=webdings>7</font>&nbsp;"
else
   Response.Write "   ��<font face=webdings><a href=main.asp?" & intdays & "1" &">9</a></font> <font face=webdings><a href=main.asp?" & intdays & (intpageno-1) & ">7</a></font>&nbsp;"
end if
dim intnopage
for intnopage=1to intpagecount
  if intnopage=intpageno then
     Response.Write intnopage & "&nbsp;"
  else
     Response.Write "<a href=main.asp?" & intdays & intnopage & ">" & intnopage & "</a>&nbsp;"
  end if
next
if intpageno=intpagecount or intpagecount=0 then
   Response.Write "<font face=webdings>8</font><font face=webdings>:</font>ҳ"
else
   Response.Write "<font face=webdings><a href=main.asp?" & intdyas & (intpageno) & ">8</a> </font><font face=webdings><a href=main.asp?" & intdays & intpagenumber & ">:</a></font>ҳ"
end if
%>
</P>
<div align="center">
  <center>
  <table border="1" width="700" bgcolor=#A9D46D>
  <form action="write.asp" method="post" id=form1 name=form1>
    <tr>
      <td bgcolor=#A9D46D width="130" >����<input type="text" name="name" size="10" value="�ο�" id=name class=name></td> 
      <td bgcolor=#A9D46D width="200" >����<input type="text" name="mail" id=mail class=mail></td>
      <td bgcolor=#A9D46D width="370" align="center"><%=date%>  &nbsp; <%=time%> &nbsp; &nbsp; (�������255���ַ�)</td>                   
    </tr>
    <tr>
      <td  width="700" colspan="3">
      <textarea name="text" rows="5" cols="95" id=comments class=comments>
     
      </textarea></td>
    </tr>
    <tr>
      <td width="700" colspan="3" align="center"><input type="submit" value="�� ��" id=submit1 name=submit1 class=submit1></td>
    </tr>
    </form>
  </table>
  </center>
</div>
</body>
</html>
