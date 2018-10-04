<%@ Language=VBScript %>
<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>留言板系统管理界面</title>
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
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage1.asp">添加管理员帐户</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage2.asp">删除管理员帐户</td>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage3.asp">管理留言板</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">修改密码</a></td>
    </tr>
  </table>
  </center>
</div>
<p>　</p>
<div align="center">
  <center>
    <table border="1" width="80%" height="136">
       <tr>
          <td bgcolor=#E1ECE9 width="50%" align="center" height="16">添加管理员帐户</td>
         <td bgcolor=#F4FBF9 width="50%" height="16">该功能增加普通级别管理员帐户</td>
       </tr>
       <tr>
         <td bgcolor=#F4FBF9 width="50%" align="center" height="48">删除管理员帐户</td>
         <td bgcolor=#E1ECE9 width="50%" height="48">使用最高管理员帐户登陆后，可以删除其他管理员帐户，但最高管理员帐户不能删除</td>
       </tr>
       <tr>
         <td bgcolor=#E1ECE9 width="50%" align="center" height="32">管理留言板</td>
         <td bgcolor=#F4FBF9 width="50%" height="32">使用该功能，管理员可以删除任何人的留言</td>
       </tr>
       <tr>
         <td bgcolor=#F4FBF9 width="50%" align="center" height="16">修改密码</td>
         <td bgcolor=#E1ECE9 width="50%" height="16">使用该功能，可以修改管理员密码</td>
       </tr>
    </table>
 </center>
</div>

<form method="POST" action="exit.asp">
  
  <p align="center"><input type="submit" value="离 开" name="B1"></p>
</form>

</BODY>
</HTML>
