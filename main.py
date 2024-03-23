from window import Window
from month import Month
from day import Day
from components.top_section import Top_section
from components.top_right_section import Top_right_section
from components.side_section import Side_section
from components.bottom_section import Bottom_section
from components.init_window import Init_window
from database.database import Database
import os

def display_main_window():

    # Load up some components
    top_section_obj = Top_section()
    top_right_section_obj = Top_right_section()
    side_section_obj = Side_section(window_obj.selected_day, window_obj.selected_month, window_obj.selected_year)
    bottom_section_obj = Bottom_section()

    # Process Top right section
    top_right_section_obj.display_frame8()

    # Process months and days
    # Store pair of each "month name" with each "month object"
    months_objects = {}

    # Currently selected "amount_spent" label
    selected_day_amount_label = None

    # List for first day's "amount_spent" labels
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

    # Raise current month frame on startup
    months_objects[window_obj.curr_month].frame3.tkraise()

    month_obj.init_month_db(window_obj.curr_month, window_obj.selected_month)

    # Set and pass initial "monthly_spent" value for bottom section
    months_objects[window_obj.curr_month].fetch_bottom_section_figures(window_obj.curr_month)
    init_total_spent_this_month = months_objects[window_obj.curr_month].return_new_bottom_section_figures()[0]
    init_remaining_balance = months_objects[window_obj.curr_month].return_new_bottom_section_figures()[1]

    # Pass currently selected selected_day_amount_label to Top_section
    top_section_obj.pass_selected_day_amount_label(selected_day_amount_label)

    # Pass list of collected "amount_spent" labels for only first days of each month
    top_section_obj.pass_list_first_day_amount_labels(list_first_day_amount_labels)

    # Process Top section
    top_section_obj.display_frame2(window_obj.months.keys(), months_objects, top_right_section_obj.pass_top_right_section)

    # Process Side section & data
    side_section_obj.init_and_display_all()
    side_section_obj.display_frame4_data()
    side_section_obj.display_frame5_data()

    # Process Bottom section
    bottom_section_obj.initiate_frame9()
    bottom_section_obj.display_frame9()
    bottom_section_obj.pass_total_spent_this_month(init_total_spent_this_month, init_remaining_balance)

def display_init_window():
    # Process initial window for entering initial remaining balance
    init_window_obj = Init_window()
    init_window_obj.initialize_init_window()
    init_window_obj.display_init_window()

# Initiate main window
window_obj = Window()

# If DB file exists, run the main window, otherwise initial window
if os.path.isfile(window_obj.db_file):
    display_main_window()
else:
    display_init_window()

# Process window
window_obj.display_window()