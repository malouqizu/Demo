<!--#include file="datastore.asp"-->
<%
Response.Cookies("login")="off"
dim objconnect
set objconnect=server.CreateObject ("adodb.connection")
objconnect.Open strconnect
dim objrs
set objrs=server.CreateObject ("adodb.recordset")
objrs.Open "admin",objconnect,1,3
dim strname,strpassword
strname=Request.Form("username")
strpassword=Request.Form ("password")
while (not objrs.eof) and (not objrs.BOF )
 Response.Write objrs("name") & objrs("password")
 if strname=objrs("name") and strpassword=objrs("password") then
    Response.Cookies ("login")="ok"
    objrs("lastdate")=now()
    objrs("lastip")=Request.ServerVariables("remote_addr")
    objrs("usenumber")=objrs("usenumber")+1
    objrs.Update
    objrs.MoveNext  
 else 
    objrs.MoveNext
  end if
wend
objrs.Close
set objrs=nothing
objconnect.Close
set objconnect=nothing
if Request.Cookies("login")="ok" then 
   Response.Redirect "manage0.asp"
else 
   response.Redirect "login.asp"
end if
%>