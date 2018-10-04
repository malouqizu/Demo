<!--#include file="datastore.asp"-->
<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>留言管理</title>
</HEAD>
<BODY >
<%
if Request.Cookies("login")="off" then
   Response.Redirect "login.asp"
end if
%>
<p align="center"><img border="0" src="banner1.gif" width="700" height="60" align="center"></p>
<div align="center">
  <center>
  <table border="1" width=700>
    <tr>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage1.asp">添加管理员帐户</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage2.asp">删除管理员帐户</td>
      <td bgcolor=#F4FBF9 width=175 align="center">管理留言板</td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">修改密码</a></td>
    </tr>
  </table>
  </center>
  <hr>
  <div align="center">
  <center>
  <table border="1" width="536">
    <tr>
      <td bgcolor=#F4FBF9 width="48">查询：</td>
      <td bgcolor=#E1ECE9 width="32">姓名</td>
      <td bgcolor=#F4FBF9 width="64">
        <form method="POST" action="manage3.asp">
          <input type="text" name="name" size="8" value="所有"></td>
      <td bgcolor=#E1ECE9 width="32">邮箱</td>
      <td bgcolor=#F4FBF9 width="80"><input type="text" name="mail" size="10" value="所有"></td>
      <td bgcolor=#E1ECE9 width="32">时间</td>
      <td bgcolor=#F4FBF9 width="58">
      <select size="1" name="D1">
      <option>所有留言</option>
      <option>最近一天发表的留言</option>
      <option>最近三天发表的留言</option>
      <option>最近一周发表的留言</option>
      <option>最近一月发表的留言</option>
      </select>
      </td>
      <td bgcolor=#E1ECE9 width="22"><input type="submit" value="提交" name="B1"></td>
      </form>
    </tr>
  </table>
  </center>
</div>
</div>

<%
if Request.Form("d1")<>"" then
   dim objconnect
   set objconnect=server.CreateObject ("adodb.connection")
   objconnect.Open strconnect
   dim objrs
   set objrs=server.CreateObject ("adodb.recordset")
   dim strkey
   if Request.Form ("name")="所有"  then
      strkey="select * from content"
      if Request.Form("mail")="所有" then
         strkey=strkey
         select case Request.Form("d1")
            case "最近一天发表的留言" 
               strkey=strkey & " where (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " where (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " where (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " where (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      else
         strkey=strkey & " where mail='" & Request.Form("mail") & "'"
         select case Request.Form("d1")
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      end if
    else
        strkey="select * from content where name='" & Request.Form("name") & "' "
        if Request.Form("mail")="所有" then
         strkey=strkey
         select case Request.Form("d1")
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      else
         strkey=strkey & " and mail='" & Request.Form("mail") & "'"
         select case Request.Form("d1")
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      end if
 end if
 
   strkey=strkey & " order by date asc "
 objrs.Open strkey,objconnect,1,2
 if objrs.RecordCount=0 then 
   Response.Write "没有符合条件的留言"
 else
   dim intno
   intno=1
   Response.Write "<form method=post action=""delete.asp?n=" & Request.Form("name") & "m=" & Request.Form("mail") & "t=" & Request.Form("d1") & """ name=form3>"
   while not objrs.EOF 
      Response.Write "<div align=""center""><center><table border=""1"" width=""700""><tr><td width=""125"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">名字："
      Response.Write (objrs("name"))
      Response.Write "</td><td width=""195"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">邮箱："
      Response.Write (objrs("mail"))
      Response.Write "</td><td width=""250"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">发表日期："
      Response.Write (objrs("date"))
      Response.Write "</td><td width=""108"" bgcolor=""#F4FAED"" bordercolor=""#669999"" bordercolorlight=""#669999"" bordercolordark=""#669999"">&nbsp;&nbsp;删除："
      Response.Write "<input type=""checkbox"" name=" & intno & ">"
      Response.Write "</td></tr><tr><td width=""678"" bgcolor=""#E3F1D1"" colspan=""4"">"
      Response.Write (objrs("text"))
      Response.Write "</td></tr></table></center></div>"
      objrs.Movenext
      intno=intno+1
   wend
 end if
 end if
 Response.Write "<p align=""right""><input type=""submit"" value=""删 除"">&nbsp;&nbsp;&nbsp;&nbsp;</p></form>"      
%>
<hr>
<form method="POST" action="exit.asp" id=form1 name=form1>
    <p align="center"><input type="submit" value="离 开" name="B1"></p>
</form>
</BODY>
</HTML>
