from window import Window
from month import Month
from day import Day
from components.top_section import Top_section
from components.top_right_section import Top_right_section
from components.side_section import Side_section
from components.bottom_section import Bottom_section
from database.database import Database

# Load up all components
window_obj = Window()
top_section_obj = Top_section()
top_right_section_obj = Top_right_section()
side_section_obj = Side_section(window_obj.selected_day, window_obj.selected_month, window_obj.selected_year)
bottom_section_obj = Bottom_section()

# Display Top right section
top_right_section_obj.display_frame8()

# Display months and days
# Store pair of each "month name" with each "month object"
months_objects = {}
days_objects = {}

for month, days_count in window_obj.months.items():
    # Create separate m object for each month
    month_obj = Month(month, days_count)

    # Display each month
    month_obj.display_month()

    # Add each month object to dictionary
    months_objects[month] = month_obj

    # Display each day
    day_index = 1
    for row in range(5):
        for col in range(7):
            day_obj = Day(month_obj, row, col, top_right_section_obj.pass_top_right_section)
            day_obj.display_day()
            day_obj.populate_day_props(day_index)

            if day_index >= month_obj.days_count:
                break
            else:
                day_index += 1

# Raise current month frame on startup
months_objects[window_obj.curr_month].frame3.tkraise()

month_obj.init_month_db(window_obj.curr_month, window_obj.selected_month)

# Display Top section
top_section_obj.display_frame2(window_obj.months.keys(), months_objects, top_right_section_obj.pass_top_right_section)

# Display Side section
side_section_obj.display_frame7()

side_section_obj.display_data()

# Display Bottom section
bottom_section_obj.display_frame9()

# Display window
window_obj.display_window()
