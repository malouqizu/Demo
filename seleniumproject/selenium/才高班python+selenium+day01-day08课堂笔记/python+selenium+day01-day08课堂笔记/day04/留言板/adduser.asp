<!--#include file="datastore.asp"-->
<%
dim objconnect
set objconnect=server.CreateObject ("adodb.connection")
objconnect.Open strconnect
dim objrs
set objrs=server.CreateObject ("adodb.recordset")
objrs.Open "admin",objconnect,1,3
dim stradminname
stradminname=Request.Form("admin")
dim stradminpassword
stradminpassword=Request.Form("adminpassword")
dim strnewuser
strnewuser=Request.Form("newuser")
dim strnewpassword
strnewpassword=Request.Form ("newpassword")
dim strconfirmpassword
strconfirmpassword=Request.Form ("confirmpassword")
dim intflag
objrs.MoveFirst 
if stradminname<>objrs("name") or stradminpassword<>objrs("password") then
   Response.Write "请输入正确的最高管理员用户名和密码"
else
   intflag=0
   objrs.MoveFirst 
   while not objrs.EOF 
      if strnewuser=objrs("name") then intflag=1
      objrs.MoveNext 
   wend
   if intflag=0 then   
      if strcomp(strnewpassword,strconfirmpassword,1)=0 then
          objrs.AddNew 
          objrs("name")=strnewuser
          objrs("password")=strnewpassword
          objrs("creatdate")=now()
          objrs("usenumber")=0
          objrs.Update 
          objrs.MoveFirst
          objrs("usenumber")=objrs("usenumber")+1
          objrs("lastip")=Request.ServerVariables("remote_addr")
          objrs("lastdate")=now()
          objrs.Update 
      else 
          Response.Write "您两次输入的密码不匹配"
      end if
   else 
      Response.Write "该用户名已存在"
    end if
 end if
 objrs.Close
 set objrs=nothing
 objconnect.Close
 set objconnect=nothing
 Response.Redirect "manage0.asp"
         
%>