from automateCalendar import CalendarAutomation

mycalendar = CalendarAutomation()

def test_check_date():
    assert mycalendar.automate_calendar() == "03/19/2025"
    print("Test Case Passed")