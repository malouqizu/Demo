<!--#include file="datastore.asp"-->

<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>ɾ������Ա�ʻ�</title>
</HEAD>
<BODY>
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
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage1.asp">��ӹ���Ա�ʻ�</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center">ɾ������Ա�ʻ�</td>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage3.asp">�������԰�</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">�޸�����</a></td>
    </tr>
  </table>
  </center>
</div>
<p></p>
<div align="center">
 <form action="deleteuser.asp" method=post name="form2">
  <center>
  <div align="center">
    <center>
  <table border="1" width="58%">
    <tr>
      <td bgcolor=#F4FBF9 width="51%" align="center">��߹���Ա�û���</td>
      <td bgcolor=#F4FBF9 width="55%" ><input type="text" name="admin" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#E1ECE9 width="51%" align="center">��߹���Ա����</td>
      <td bgcolor=#E1ECE9 width="55%"><input type="password" name="adminpassword" size=24></td>
    </tr>
    <tr>
      <td bgcolor=#F4FBF9 width="51%" align="center">��ɾ����Ա�û���</td>
      <td bgcolor=#F4FBF9 width="55%"><select size="1" name="D1">
<%
dim objconnect
set objconnect=server.CreateObject ("adodb.connection")
objconnect.Open strconnect
dim objrs
set objrs=server.CreateObject ("adodb.recordset")
objrs.Open "admin",objconnect,1,2
objrs.MoveNext
while not objrs.EOF
  Response.Write "<option>" & objrs("name") & "</option>"
  objrs.MoveNext
wend
objrs.Close
set objrs=nothing
objconnect.Close 
set objconnect=nothing
%>       
 </select></td>
    </tr>
    <tr>
      <td width="100%" colspan="2">
        <p align="center"><input type="submit" value="�� ��" name="B1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
        <input type="reset" value="ȫ д" name="B2"></p>
      </td>
    </tr>
  </table>
    </center>
  </div>
  </center>
 </form>
</div>
<p></p>
<form method="POST" action="exit.asp" id=form1 name=form1>
    <p align="center">  <input type="submit" value="�� ��" name="B1"></p>
</form>
<p align="center">��</p>

</BODY>
</HTML>
