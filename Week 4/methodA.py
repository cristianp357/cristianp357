pay_per_hour = 90
hours_worked_in_week = 90


# if hours_worked_in_week <= 0:
#     print ( "Error, negative hours" )
# elif hours_worked_in_week > 84:
#     print ( "Error, Impossible hours")

if hours_worked_in_week <= 0:
    print ( "Error, negative hours" )
elif hours_worked_in_week > 84:
    print ( "Error, Impossible hours")
elif hours_worked_in_week <= 40:
    regular_pay = pay_per_hour * hours_worked_in_week
    round ( regular_pay, 2)
    print ( "$" + str(regular_pay))
elif hours_worked_in_week > 40:
    overtime_pay = ( pay_per_hour * 1.5) * hours_worked_in_week
    round ( overtime_pay, 2)
    print ( "$" + str(overtime_pay))


# elif hours_worked_in_week <= 0:
#     print ( "Error, negative hours" )
# elif hours_worked_in_week > 84:
#     print ( "Error, Impossible hours")
