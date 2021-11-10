# s-track.py 
from __future__ import unicode_literals
   
import frappe
#import re #for escape function

def applications(context):
	uid = frappe.session.user # UserID of logged in User
	#fuid = re.escape(uid) # For Escaping special characters
	context.uid = uid  # Passing userId to context to be printed on webpage
	uemail = frappe.get_value("User", uid, ["email"]) #fetching email id of logged in user
	
	if(uid=='principal@gndec.ac.in' or uid=='Administrator'):
		context.apps = frappe.get_all('Student Form', fields=["name", "student_name", "roll_no", "email", "branch", "application_text", "faculty_comments", "hod_comments", "dean_comments", "status"])
	else:
		context.apps = frappe.get_all('Student Form', filters={ 'email': uemail}, fields=["name", "student_name", "roll_no", "email", "branch", "application_text", "faculty_comments", "hod_comments", "dean_comments", "status"])
