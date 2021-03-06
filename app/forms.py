from flask_wtf import Form
from wtforms import TextField, DateField, SelectField, RadioField, BooleanField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, length, ValidationError, NumberRange, Regexp
import pandas as pd

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class AddTransactionForm(Form):
    date = DateField('date', format='%d/%m/%Y', validators=[DataRequired()])
    amount = TextField('amount', validators=[Regexp(regex='[-+]*\d+[\.\d*]*', 
                                                    message='Should be a numerical value using . as a separator'), 
                                             DataRequired()])
    description = TextField('description', validators=[DataRequired(), length(max=30)])
    category = SelectField('category', validators=[DataRequired()])
    note = TextField('note')
    operation_type = RadioField('operation type', validators=[DataRequired()])
    cheque_number = TextField('cheque_number', validators=[Regexp('\d*')])


class AddScheduledTransactionForm(Form):
    date = DateField('date', format='%d/%m/%Y', validators=[DataRequired()])
    amount = TextField('amount', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired(), length(max=30)])
    category = SelectField('category', validators=[DataRequired()])
    note = TextField('note')
    every_nb = TextField('every', default=1, validators=[DataRequired()])
    every_type = RadioField('every_type', default='months', choices=zip(['months', 'weeks', 'days'],
                                                       ['months', 'weeks', 'days']), 
                             validators=[DataRequired()])
    ends = DateField('date', format='%d/%m/%Y')


class AddTransferForm(Form):
    date = DateField('date', format='%d/%m/%Y', validators=[DataRequired()])
    amount = TextField('amount', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired(), length(max=30)])
    note = TextField('note')
    account_to = SelectField('account_to', validators=[DataRequired()])


class SelectDateRangeForm(Form):
    start = TextField('start', validators=[DataRequired()])
    end = TextField('end', validators=[DataRequired()])


class AddAccount(Form):
    name = TextField('name', validators=[DataRequired()])
    currency = RadioField('every_type', default='months', choices=zip(['months', 'weeks', 'days'],
                                                       ['months', 'weeks', 'days']), 
                             validators=[DataRequired()])
    initial_balance = TextField('initial balance', default=0, validators=[DataRequired()])


class ReconcileTransactionsForm(Form):
    previous_date_statement = DateField('date', format='%d/%m/%Y')
    previous_reconciled_amount = TextField('amount', validators=[DataRequired()])

    new_date_statement = DateField('date', format='%d/%m/%Y')
    new_reconciled_amount = TextField('amount', validators=[DataRequired()])


class ReconcileCheckTransactionsForm(Form):

    reconciled_transactions = MultiCheckboxField('reconciled')
