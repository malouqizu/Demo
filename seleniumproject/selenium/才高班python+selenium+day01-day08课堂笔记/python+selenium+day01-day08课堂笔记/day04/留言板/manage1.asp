<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>��ӹ���Ա�û�</title>
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
      <td bgcolor=#F4FBF9 width=175 align="center">��ӹ���Ա�ʻ�</td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage2.asp">ɾ������Ա�ʻ�</td>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage3.asp">�������԰�</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">�޸�����</a></td>
    </tr>
  </table>
  </center>
</div>
<p></p>
<div align="center">
 <form action="adduser.asp" method=post name="form2">
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
      <td bgcolor=#F4FBF9 width="51%" align="center">�¹���Ա�û���</td>
      <td bgcolor=#F4FBF9 width="55%"><input type="text" name="newuser" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#E1ECE9 width="51%" align="center">�¹���Ա����</td>
      <td bgcolor=#E1ECE9 width="55%"><input type="password" name="newpassword" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#F4FBF9 width="51%" align="center">�¹���Ա����ȷ��</td>
      <td bgcolor=#F4FBF9 width="55%"><input type="password" name="confirmpassword" size="24"></td>
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
