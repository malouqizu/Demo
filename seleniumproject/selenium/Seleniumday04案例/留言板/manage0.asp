<%@ Language=VBScript %>
<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>���԰�ϵͳ�������</title>
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
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage2.asp">ɾ������Ա�ʻ�</td>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage3.asp">�������԰�</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">�޸�����</a></td>
    </tr>
  </table>
  </center>
</div>
<p>��</p>
<div align="center">
  <center>
    <table border="1" width="80%" height="136">
       <tr>
          <td bgcolor=#E1ECE9 width="50%" align="center" height="16">��ӹ���Ա�ʻ�</td>
         <td bgcolor=#F4FBF9 width="50%" height="16">�ù���������ͨ�������Ա�ʻ�</td>
       </tr>
       <tr>
         <td bgcolor=#F4FBF9 width="50%" align="center" height="48">ɾ������Ա�ʻ�</td>
         <td bgcolor=#E1ECE9 width="50%" height="48">ʹ����߹���Ա�ʻ���½�󣬿���ɾ����������Ա�ʻ�������߹���Ա�ʻ�����ɾ��</td>
       </tr>
       <tr>
         <td bgcolor=#E1ECE9 width="50%" align="center" height="32">�������԰�</td>
         <td bgcolor=#F4FBF9 width="50%" height="32">ʹ�øù��ܣ�����Ա����ɾ���κ��˵�����</td>
       </tr>
       <tr>
         <td bgcolor=#F4FBF9 width="50%" align="center" height="16">�޸�����</td>
         <td bgcolor=#E1ECE9 width="50%" height="16">ʹ�øù��ܣ������޸Ĺ���Ա����</td>
       </tr>
    </table>
 </center>
</div>

<form method="POST" action="exit.asp">
  
  <p align="center"><input type="submit" value="�� ��" name="B1"></p>
</form>

</BODY>
</HTML>
