<!--#include file="datastore.asp"-->
<%
if Request.Cookies("login")="off" then
   Response.Redirect "login.asp"
end if

dim objconnect
set objconnect=server.CreateObject ("adodb.connection")
objconnect.Open strconnect
dim strname
strname=Request.Form("name")
dim stroldpassword
stroldpassword=Request.Form ("oldpassword")
dim strnewpassword
strnewpassword=Request.Form ("newpassword")
dim strconfirmpassword
strconfirmpassword=Request.Form ("confirmpassword")
strname="select * from admin where name like '" & strname & "'"
dim objrs
set objrs=server.CreateObject ("adodb.recordset")
objrs.Open strname,objconnect,1,3
if objrs.RecordCount =0 then 
   Response.Write "请您输入正确的用户名"
else
   if objrs("password")<>stroldpassword then
      Response.Write "请您输入正确的密码"
   else
      if strnewpassword<>strconfirmpassword then
         Response.Write "两次输入的新密码不同"
      else
         objrs("password")=strnewpassword
         objrs("lastdate")=now()
         objrs("lastip")=Request.ServerVariables("remote_addr")
         objrs("usenumber")=objrs("usenumber")+1
         objrs.Update
         objrs.Close
         set objrs=nothing
         objconnect.Close
         set objconnect=nothing
         Response.Redirect "manage0.asp" 
      end if
   end if
end if
objrs.Close
set objrs=nothing
objconnect.Close
set objconnect=nothing
%>