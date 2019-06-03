from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, FormField, FieldList, IntegerField, PasswordField, BooleanField
from werkzeug.datastructures import MultiDict

# some web forms and what not

class LoginForm(FlaskForm):
	email = StringField('Email', [validators.Email(message = 'Please Enter A Valid Email')])
	password = PasswordField('Password')
	remember_me = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
	email = StringField('Email', [validators.Email(message = 'Please Enter A Valid Email')])
	first_name = StringField('First Name', [validators.DataRequired(message = 'Please Enter Something')])
	last_name = StringField('Last Name', [validators.DataRequired(message = 'Please Enter Something')])
	password = PasswordField('Password')
	is_cardio = SelectField('Cardiologist?', choices=[('True', 'Yes'), ('False', 'No')])

class UserForm(FlaskForm):
	first_name = StringField('First Name', [validators.DataRequired(message = 'Please Enter Something')])
	last_name = StringField('Last Name', [validators.DataRequired(message = 'Please Enter Something')])
	email = StringField('Email', [validators.Email(message = 'Please Enter A Valid Email')])
	is_cardio = SelectField('Cardiologist?', choices=[('True', 'Yes'), ('False', 'No')])	
	is_admin = SelectField('Administrator? (can add/remove users)', choices=[('False', 'No'), ('True', 'Yes')])

class EmailForm(FlaskForm):
	email = StringField('Enter your email: ', [validators.DataRequired(message='Please Enter Something')])

class DeleteForm(FlaskForm):
	first_name = StringField('First Name', [validators.DataRequired(message = 'Please Enter Something')])
	last_name = StringField('Last Name')
	email = StringField('Email')

class SetPasswordForm(FlaskForm):
	password = PasswordField('Password', [validators.DataRequired(message = 'Please Enter Something')])

class ScheduleEntryForm(FlaskForm):
	first_name = StringField('First Name', [validators.DataRequired(message = 'Please Enter Something')])

class ScheduleForm(FlaskForm):
	userfirstNamesM1 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesT1 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesW1 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesTh1 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesF1 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesS1 = FieldList(FormField(ScheduleEntryForm), min_entries=1)
	userfirstNamesSu1 = FieldList(FormField(ScheduleEntryForm), min_entries=1)

	userfirstNamesM2 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesT2 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesW2 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesTh2 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesF2 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesS2 = FieldList(FormField(ScheduleEntryForm), min_entries=1)
	userfirstNamesSu2 = FieldList(FormField(ScheduleEntryForm), min_entries=1)

	userfirstNamesM3 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesT3 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesW3 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesTh3 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesF3 = FieldList(FormField(ScheduleEntryForm), min_entries=3, max_entries = 7)
	userfirstNamesS3 = FieldList(FormField(ScheduleEntryForm), min_entries=1)
	userfirstNamesSu3 = FieldList(FormField(ScheduleEntryForm), min_entries=1)

class NumberUsersForm(FlaskForm):
	NumberUsersM1 = IntegerField('# Working on first Monday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersT1 = IntegerField('# Working on first Tuesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersW1 = IntegerField('# Working on first Wednesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersTh1 = IntegerField('# Working on first Thursday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersF1 = IntegerField('# Working on first Friday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersS1 = IntegerField('# Working on first Saturday', [validators.DataRequired(message = 'Please Enter Something')], default=1)
	NumberUsersSu1 = IntegerField('# Working on first Sunday', [validators.DataRequired(message = 'Please Enter Something')], default=1)

	NumberUsersM2 = IntegerField('# Working on second Monday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersT2 = IntegerField('# Working on second Tuesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersW2 = IntegerField('# Working on second Wednesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersTh2 = IntegerField('# Working on second Thursday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersF2 = IntegerField('# Working on second Friday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersS2 = IntegerField('# Working on second Saturday', [validators.DataRequired(message = 'Please Enter Something')], default=1)
	NumberUsersSu2 = IntegerField('# Working on second Sunday', [validators.DataRequired(message = 'Please Enter Something')], default=1)

	NumberUsersM3 = IntegerField('# Working on third Monday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersT3 = IntegerField('# Working on third Tuesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersW3 = IntegerField('# Working on third Wednesday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersTh3 = IntegerField('# Working on third Thursday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersF3 = IntegerField('# Working on third Friday', [validators.DataRequired(message = 'Please Enter Something')], default=3)
	NumberUsersS3 = IntegerField('# Working on third Saturday', [validators.DataRequired(message = 'Please Enter Something')], default=1)
	NumberUsersSu3 = IntegerField('# Working on third Sunday', [validators.DataRequired(message = 'Please Enter Something')], default=1)
	
class RequestForm(FlaskForm):
	post_call = SelectField('Select when you want post call:', choices = [(None, 'No Preference'), ('M1', 'Monday Week 1'), ('T1', 'Tuesday Week 1'), ('W1', 'Wednesday Week 1'), ('Th1', 'Thursday Week 1'), ('F1', 'Friday Week 1'),('M2', 'Monday Week 2'), ('T2', 'Tuesday Week 2'), ('W2', 'Wednesday Week 2'), ('Th2', 'Thursday Week 2'), ('F2', 'Friday Week 2'),('M3', 'Monday Week 3'), ('T3', 'Tuesday Week 3'), ('W3', 'Wednesday Week 3'), ('Th3', 'Thursday Week 3'), ('F3', 'Friday Week 3')])
	third_call = SelectField('Select when you want weekend third call:', choices = [(None, 'No Preference'), ('Sat1', 'Saturday Week 1'), ('Sun1', 'Sunday Week 1'), ('Sat2', 'Saturday Week 2'), ('Sun2', 'Sunday Week 2'), ('Sat3', 'Saturday Week 3'), ('Sun3', 'Sunday Week 3')])
