<%@ Language=VBScript %>
<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft Visual Studio 6.0">
<title>�޸�����</title>
</HEAD>
<BODY>
<%
if Request.Cookies("login")="off" then
   Response.Redirect "login.asp"
end if
%>
<p align="center"><IMG height=60 src="banner1.gif" width=700 align=center border=0></p>
<div align="center">
  <center>
  <table border="1" width=700>
    <tr>
      <td bgcolor=#f4fbf9 width=175 align="middle"><A href="manage1.asp">��ӹ���Ա�ʻ�</a></td>
      <td bgcolor=#e1ece9 width=175 align="middle"><A href="manage2.asp">ɾ������Ա�ʻ�</a></td>
      <td bgcolor=#f4fbf9 width=175 align="middle"><A href="manage3.asp">�������԰�</a></td>
      <td bgcolor=#e1ece9 width=175 align="middle">�޸�����</td>
    </tr>
  </table>
  </center>
</div>
<div align="center">
 <form action="changepw.asp" method=post name="form2">
  <center>
  <div align="center">
    <center>
  <table border="1" width="58%">
    <tr>
      <td bgcolor=#f4fbf9 width="51%" align="middle">�û���</td>
      <td bgcolor=#f4fbf9 width="55%" ><input type="text" name="name" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#e1ece9 width="51%" align="middle">ԭ������</td>
      <td bgcolor=#e1ece9 width="55%"><input type="password" name="oldpassword" size=24></td>
    </tr>
    <tr>
      <td bgcolor=#f4fbf9 width="51%" align="middle">������</td>
      <td bgcolor=#f4fbf9 width="55%"><input type="password" name="newpassword" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#e1ece9 width="51%" align="middle">ȷ��������</td>
      <td bgcolor=#e1ece9 width="55%"><input type="password" name="confirmpassword" size="24"></td>
    </tr>
    <tr>
      <td width="100%" colspan="2">
        <p align="center"><input type="submit" value="�� ��" name="B1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
        <input type="reset" value="�� ��" name="B2"></p>
      </td>
    </tr>
  </table>
    </center>
  </div>
  </center>
 </form>
<form method="post" action="exit.asp" id=form1 name=form1>
  <p align="center"><input type="submit" value="�� ��" name="B1"></p>
</form></div>
</BODY>
</HTML>
