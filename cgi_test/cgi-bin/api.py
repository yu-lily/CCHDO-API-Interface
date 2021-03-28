#!/usr/bin/python
# Import modules for CGI handling
import cgi, cgitb
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
if form.getvalue('API_key_input'):
   api_key = form.getvalue('API_key_input')
else:
   api_key = "Not entered"
if form.getvalue('expocode_input'):
   expocode = form.getvalue('expocode_input')
else:
   expocode = "Not entered"
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>";
print "<title>Text Area - Fifth CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Entered Text Content is %s</h2>" % api_key
print "</body>"