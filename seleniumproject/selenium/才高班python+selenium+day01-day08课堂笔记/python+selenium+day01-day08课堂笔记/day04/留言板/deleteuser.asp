<!--#include file="datastore.asp"-->
<%
dim objconnect
set objconnect=server.CreateObject ("adodb.connection")
objconnect.Open strconnect
dim objrs
set objrs=server.CreateObject ("adodb.recordset")
dim stradminname
stradminname=Request.Form("admin")
dim stradminpassword
stradminpassword=Request.Form("adminpassword")
dim strdeleteuser
strdeleteuser="select * from admin where name like '" & Request.Form ("d1") & "'"
objrs.Open "admin",objconnect,1,2
if stradminname=objrs("name") and stradminpassword=objrs("password") then
   objrs.Close
   objrs.Open strdeleteuser,objconnect,1,3
   objrs.Delete
   objrs.Update 
else 
   Response.Write "请您输入正确的最高管理员用户名和密码"
end if
objrs.Close
set objrs=nothing
objconnect.Close 
set objconnect=nothing
Response.Redirect "manage2.asp"   
%>
