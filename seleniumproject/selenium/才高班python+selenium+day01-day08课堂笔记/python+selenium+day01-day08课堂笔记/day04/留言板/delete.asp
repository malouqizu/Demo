<!--#include file="datastore.asp"-->
<%
dim strname
dim strmail
dim strdate
dim strquery

strquery=mid(Request.QueryString ,3)
strname=left(strquery,instr(1,strquery,"m=",1)-1)
strquery=mid(strquery,len(strname)+3)
strmail=left(strquery,instr(1,strquery,"t=",1)-1)
strdate=mid(strquery,len(strmail)+3)
dim objconnect
   set objconnect=server.CreateObject ("adodb.connection")
   objconnect.Open strconnect
   dim objrs
   set objrs=server.CreateObject ("adodb.recordset")
   dim strkey
   if strname="所有"  then
      strkey="select * from content"
      if strmail="所有" then
         strkey=strkey
         select case strdate
            case "最近一天发表的留言" 
               strkey=strkey & " where (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " where (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " where (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " where (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      else
         strkey=strkey & " where mail='" & strmail & "'"
         select case strdate
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      end if
    else
        strkey="select * from content where name='" & strname & "' "
        if strmail="所有" then
         strkey=strkey
         select case strdate
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      else
         strkey=strkey & " and mail='" & strmail & "'"
         select case strdate
            case "最近一天发表的留言" 
               strkey=strkey & " and (now()-date<1) "
            case "最近三天发表的留言"
               strkey=strkey & " and (now()-date<3) "
            case "最近一周发表的留言"
               strkey=strkey & " and (now()-date<7) "
            case "最近一月发表的留言"
               strkey=strkey & " and (now()-date<30) "
            case "所有留言"
               strkey=strkey
         end select
      end if
 end if
 
   strkey=strkey & " order by date asc "
 objrs.Open strkey,objconnect,1,3
 dim intrscount
 intrscount=objrs.RecordCount
  while intrscount>0
    if Request.Form(cstr(intrscount))="on" then
      objrs.Move intrscount-1,1
      objrs.Delete
   end if
   intrscount=intrscount-1
 wend
 objrs.Update
 objrs.Close
 set objrs=nothing
 objconnect.Close
 set objconnect=nothing
 Response.Redirect "manage3.asp"
%>