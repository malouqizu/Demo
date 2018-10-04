<HTML>
<HEAD>
<META NAME="GENERATOR" Content="Microsoft FrontPage 4.0">
<title>添加管理员用户</title>
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
      <td bgcolor=#F4FBF9 width=175 align="center">添加管理员帐户</td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage2.asp">删除管理员帐户</td>
      <td bgcolor=#F4FBF9 width=175 align="center"><a href="manage3.asp">管理留言板</a></td>
      <td bgcolor=#E1ECE9 width=175 align="center"><a href="manage4.asp">修改密码</a></td>
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
      <td bgcolor=#F4FBF9 width="51%" align="center">最高管理员用户名</td>
      <td bgcolor=#F4FBF9 width="55%" ><input type="text" name="admin" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#E1ECE9 width="51%" align="center">最高管理员密码</td>
      <td bgcolor=#E1ECE9 width="55%"><input type="password" name="adminpassword" size=24></td>
    </tr>
    <tr>
      <td bgcolor=#F4FBF9 width="51%" align="center">新管理员用户名</td>
      <td bgcolor=#F4FBF9 width="55%"><input type="text" name="newuser" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#E1ECE9 width="51%" align="center">新管理员密码</td>
      <td bgcolor=#E1ECE9 width="55%"><input type="password" name="newpassword" size="24"></td>
    </tr>
    <tr>
      <td bgcolor=#F4FBF9 width="51%" align="center">新管理员密码确认</td>
      <td bgcolor=#F4FBF9 width="55%"><input type="password" name="confirmpassword" size="24"></td>
    </tr>
    <tr>
      <td width="100%" colspan="2">
        <p align="center"><input type="submit" value="提 交" name="B1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
        <input type="reset" value="全 写" name="B2"></p>
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
    <p align="center">  <input type="submit" value="离 开" name="B1"></p>
</form>
<p align="center">　</p>

</BODY>
</HTML>
