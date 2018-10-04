<!--#include file="datastore.asp"-->
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta name="GENERATOR" content="Microsoft FrontPage 4.0">
<meta name="ProgId" content="FrontPage.Editor.Document">
<title>欢迎使用高级搜索</title>
</head>

<body>

<p align="center"><img border="0" src="banner.gif" width="700" height="60" align="center"></p>

<form method="POST" action="search.asp">
  <p align="center">搜索方式:
  <select size="1" name="D1">
  <option>作者名字</option>
  <option>邮箱地址</option>
  <option>留言内容</option>
  </select>关键词:
  <input type="text" name="text" size="10"><input type="submit" value="搜索"></p>
</form>
<%
 if Request.Form("d1")<>"" then
  dim strmethod
  strmethod=Request.Form("d1")
  dim objconnect
  set objconnect=server.CreateObject ("adodb.connection")
  objconnect.Open strconnect
  dim objrs
  set objrs=server.CreateObject("adodb.recordset")
  dim strkey
  select case strmethod
    case "作者名字"
       strkey="select * from content where name like '" & trim(Request.Form("text")) & "'order by date desc"
       objrs.Open strkey,objconnect,1,2
    case "邮箱地址"
       strkey="select * from content where mail like '" & trim(Request.Form("text")) & "'order by date desc"
       objrs.Open strkey,objconnect,1,2
    case "留言内容"
       strkey="select * from content where text like '%" & trim(Request.Form("text")) & "%'order by date desc"
       objrs.Open strkey,objconnect,1,2
  end select
  strkey=trim(Request.Form("text"))
 end if
 if Request.QueryString<>"" then
   
   strmethod=left(Request.QueryString,4)
  
  set objconnect=server.CreateObject ("adodb.connection")
  objconnect.Open strconnect
  
  set objrs=server.CreateObject("adodb.recordset")
  
   strkey=mid(Request.QueryString,5,len(Request.QueryString)-5)
   select case strmethod
    case "作者名字"
       strkey="select * from content where name like '" & strkey & "'order by date desc"
       objrs.Open strkey,objconnect,1,2
    case "邮箱地址"
       strkey="select * from content where mail like '" & strkey & "'order by date desc"
       objrs.Open strkey,objconnect,1,2
    case "留言内容"
       strkey="select * from content where mail like '%" & strkey & "%'order by date desc"
       objrs.Open strkey,objconnect,1,2
   end select
   strkey=mid(Request.QueryString,5,len(Request.QueryString)-5)
 end if
 dim intpageno
 if len(Request.QueryString)<>0 then
   intpageno=cint(right(Request.QueryString,1))
   
 else 
   intpageno=1
 end if  
 if len(Request.QueryString)<>0 or Request.Form("d1")<>"" then
 dim intrscount
 intrscount=objrs.recordcount
 if intrscount<>0 then
   objrs.Move (intpageno-1)*6
   dim intrsno
   intrsno=0
   while (not objrs.EOF ) and intrsno<6
      Response.Write "<div align=""center""><center><table border=""1"" width=""700""><tr><td width=""125"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">名字："
      Response.Write (objrs("name"))
      Response.Write "</td><td width=""195"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">邮箱："
      Response.Write (objrs("mail"))
      Response.Write "</td><td width=""358"" bgcolor=""F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">发表日期："
      Response.Write (objrs("date"))
      Response.Write "</td></tr><tr><td width=""678"" bgcolor=""#E3F1D1"" colspan=""3"">"
      Response.Write (objrs("text"))
      Response.Write "</td></tr></table></center></div>"
      intrsno=intrsno+1
      objrs.Movenext
   wend
 else
  Response.Write "没有符合条件的留言。"
 end if
 
 objrs.Close
 set objrs=nothing
 objconnect.Close 
 set objconnect=nothing
end if
%>
<font size="2" ><P align="right">
<%
dim intpagecount
intpagecount=intrscount\6
if (intpagecount*6)<intrscount then intpagecount=intpagecount+1
Response.Write "共" & intpagecount & "页"
if intpageno=1 or intpagecount=0 then 
   Response.Write "   第<font face=webdings>9</font><font face=webdings>7</font>&nbsp;"
else
   Response.Write "   第<font face=webdings><a href=search.asp?" & strmethod & strkey & "1" &">9</a></font> <font face=webdings><a href=search.asp?" & strmethod & strkey & (intpageno-1) & ">7</a></font>&nbsp;"
end if
dim intnopage
for intnopage=1to intpagecount
  if intnopage=intpageno then
     Response.Write intnopage & "&nbsp;"
  else
     Response.Write "<a href=search.asp?" & strmethod & strkey & intnopage & ">" & intnopage & "</a>&nbsp;"
  end if
 
next

if intpageno = intpagecount  then
   Response.Write "<font face=webdings>8</font><font face=webdings>:</font>页"
else
   Response.Write "<font face=webdings><a href=search.asp?" & strmethod & strkey & (intpageno+1) & ">8</a> </font><font face=webdings><a href=search.asp?" & strmethod & strkey & intpagecount & ">:</a></font>页"
end if

%>
</P>
</body>

</html>
