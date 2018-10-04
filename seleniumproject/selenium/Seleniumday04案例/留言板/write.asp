<%@ Language=VBScript %>
<!--#include file="datastore.asp"-->
<!--#include file="mailcheck.asp"-->
<%
 if request("name")="游客" or request("name")="" then
   Response.Write "请输入名字"
   Response.End 
 end if
 
 if mailcheck(trim(request("mail")))=false then
   Response.Write "请正确输入您的邮箱地址"
   Response.End
 end if
 if trim(request("text"))="" then
   Response.Write "请输入您的留言"
   Response.End
 end if 
 %>
<%
 dim name
 name=trim(request("name"))
 dim mail
 mail=trim(request("mail"))
 dim text
 text=left(trim(request("text")),255)
 dim objconnect
 set objconnect=server.CreateObject("adodb.connection")
 objconnect.Open strconnect
 dim objrs
 set objrs=server.CreateObject ("adodb.recordset")
 objrs.Open "content",objconnect,1 ,3
 objrs.MoveFirst 
 objrs.AddNew 
 objrs("name")=name
 objrs("mail")=mail
 objrs("date")= Now()
 objrs("text")=text
 objrs.Update
 objrs.Close 
 set objrs=nothing
 objconnect.close
 set objconnect=nothing
 Response.Redirect "main.asp?9"
 %>
 
 
 
 
