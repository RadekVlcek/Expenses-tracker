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

selected_day_amount_label = None

list_first_day_amount_labels = []

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
            day_obj = Day(month_obj, top_right_section_obj.pass_top_right_section)
            day_obj.display_day(row, col)
            day_obj.populate_day_props(day_index, month)
            
            # Collect iitially selected "amount_spent" label inside of Day element
            temp = day_obj.return_current_day_amount_label(day_index, month)
            if temp is not None:
                selected_day_amount_label = temp

            # Collect only every month's first day's "amount_spent" labels inside of Day elements
            if day_index == 1:
                list_first_day_amount_labels.append(day_obj.return_first_day_amount_label())

            if day_index >= month_obj.days_count:
                break
            else:
                day_index += 1

window_obj.selected_day_amount_label = selected_day_amount_label

# Raise current month frame on startup
months_objects[window_obj.curr_month].frame3.tkraise()

month_obj.init_month_db(window_obj.curr_month, window_obj.selected_month)

# Pass currently selected selected_day_amount_label to Top_section
top_section_obj.pass_selected_day_amount_label(selected_day_amount_label)

# Pass list of collected "amount_spent" labels for only first days of each month
top_section_obj.pass_list_first_day_amount_labels(list_first_day_amount_labels)

# Display Top section
top_section_obj.display_frame2(window_obj.months.keys(), months_objects, top_right_section_obj.pass_top_right_section)

# Display Side section & data
side_section_obj.init_and_display_all()
side_section_obj.display_data_in_frame4()

# Display Bottom section
bottom_section_obj.display_frame9()

# Display window
window_obj.display_window()