pay_per_hour = 15
hours_worked_in_week = 90

# if hours_worked_in_week <= 0 or hours_worked_in_week > 84:
#     print ( "Error, please reenter the correct number of hours")

overtime_pay = ( pay_per_hour * 1.5) * hours_worked_in_week


if hours_worked_in_week > 0 or hours_worked_in_week <= 40:
    regular_pay = pay_per_hour * hours_worked_in_week
    round ( regular_pay, 2)
    print ( "$" + str(regular_pay))
else:
    hours_worked_in_week < 84 or hours_worked_in_week > 40
    round ( overtime_pay, 2)
    print ( "$" + str(overtime_pay))

if hours_worked_in_week <= 0 or hours_worked_in_week > 84:
    print ( "Error, please reenter the correct number of hours")








