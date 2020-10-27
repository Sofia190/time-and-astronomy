


from django.forms import ModelForm

from .models import Day, DaysInSearchEngine, Stars




class DaysTillaDateForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date', 'second_date']



class YearsWithAttributesEqualToaValueForm(ModelForm):


	class Meta:

		model = Day

		fields = ['date_for_years_with_attributes_equal_to_a_value', 'value_for_attributes']




class BisectYearsinaDecadeForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_year_of_decade', 'second_year_of_decade']





class BisectYearsinaCenturyForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_year_of_century', 'second_year_of_century']




class AttributesofnthDayForm(ModelForm):


	class Meta:

		model = Day

		fields = ['date_to_sum_attributes', "nth_day_value", "nth_month_value"]




class BisectYearsinCenturiesForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_bisect_years_in_centuries', "second_date_bisect_years_in_centuries"]




class MonthsandDaystillthenextSpringEquinoxForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_next_spring_equinox', "second_date_next_spring_equinox"]




class MonthsandDaystillthenextAutumnEquinoxForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_next_autumn_equinox', "second_date_next_autumn_equinox"]






class PeriodsbetweenDateswithTotalLunarEclipseForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_with_total_lunar_eclipse', "second_date_with_total_lunar_eclipse"]





class Find_the_equivalent_of_timezone_with_USA_Form(ModelForm):


	class Meta:

		model = Day

		fields = ['inTimeDelta_hours', "inTZObject_name", "datetime_instance_var",]






class Find_the_difference_of_timezone_with_USA_Form(ModelForm):


	class Meta:

		model = Day

		fields = ['inTimeDelta_hours_diff', "inTZObject_name_diff", "datetime_instance_var_diff",]




class Find_equivalent_with_timezone_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['inTimeDelta_hours', "inTZObject_name_field", "datetime_instance_var",]


	# def clean_inTimeDelta_hours(self):

	# 	inTimeDelta_hours = self.cleaned_data.get('inTimeDelta_hours')

	# 	return inTimeDelta_hours





class Find_difference_with_timezone_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['inTimeDelta_hours_diff', "inTZObject_name_diff_filed", "datetime_instance_var_diff",]







class Find_difference_of_timezone_from_UTC_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['your_address', "inTZObject_name_field", "datetime_instance_var",]




	
class find_difference_between_two_timezones_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['your_address', "address_to_search", ]


	
	
class display_date_for_the_next_n_days_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['n_days', "year_for_date_n_days", "month_for_date_n_days" ]


		

class attributes_of_time_equal_to_date_in_a_decade_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['first_year_in_a_decade_sum_attributes', 'second_year_in_a_decade_sum_attributes',

			'month_sum_attributes', 'day_sum_attributes', 'hour_sum_attributes',

			'minute_sum_attributes', 'second_sum_attributes']




	
class attributes_of_time_equal_to_date_in_a_century_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['first_year_in_a_century_sum_attributes', 'second_year_in_a_century_sum_attributes',

			'month_sum_attributes_in_a_century', 'day_sum_attributes_in_a_century', 'hour_sum_attributes_in_a_century',

			'minute_sum_attributes_in_a_century', 'second_sum_attributes_in_a_century']




class find_time_until_a_date_after_n_years_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['nth_day_time_until', 'n_years_time_until']



		
class calculate_date_and_time_until_next_solstice_Form(ModelForm):

	class Meta:

		model = Day

		fields = ['next_solstice']




class date_and_time_until_the_nth_day_in_the_next_n_years_Form(ModelForm):


		class Meta:

			model = Day

			fields = [ "year_one_next_n_years", "year_two_next_n_years",

						"day_next_n_years", "month_next_n_years" ]





class years_of_nth_century_have_more_than_n_days_with_attrs_Form(ModelForm):

	class Meta:

		model = Day


		fields = ['first_year_of_nth_century_attributes', 

		"second_year_of_nth_century_attributes"]
			




	
class  solstices_in_n_years_with_sum_attrs_even_number_Form(ModelForm):

	class Meta:

		model = Day


		fields = ["first_year_solstice_even_sum", "second_year_solstice_even_sum"]





class  solstices_in_n_years_with_sum_attrs_odd_number_Form(ModelForm):

	class Meta:

		model = Day


		fields = ["first_year_solstice_odd_sum", "second_year_solstice_odd_sum"]





	
class view_calendar_Form(ModelForm):

	class Meta:

		model = Day

		fields = [ "date_one_calendar", "date_two_calendar" ]




class create_Days_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['year_one_period', 'year_two_period']



class create_Days_712_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['year_one_period', 'year_two_period']




class delete_Days_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['year_one_period', 'year_two_period']




class determine_visibility_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['count']





class ref_magnitudes_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_ref_magnitudes', 'second_id_ref_magnitudes']




class determine_most_visible_periods_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_most_visible_periods', 'second_id_most_visible_periods']




class set_season_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_season', 'second_id_set_season']




class determine_most_visible_periods_seasons_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_most_visible_periods_seasons',

		 'second_id_most_visible_periods_seasons']





class set_spring_equinox_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_spring_equinox', 'second_id_set_spring_equinox']




class set_autumn_equinox_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_autumn_equinox', 'second_id_set_autumn_equinox']




class set_summer_solstice_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_summer_solstice', 'second_id_set_summer_solstice']




class set_winter_solstice_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_winter_solstice', 'second_id_set_winter_solstice']






class determine_stars_movement_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_determine_stars_movement', 

		'second_id_determine_stars_movement']




class determine_the_aparent_magnitude_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['absolute_magnitude_calculation', 'distance_from_Earth_calculation']




class determine_the_absolute_magnitude_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['aparent_magnitude_calculation', 'distance_from_Earth_calculation']





class delete_objects_used_in_calculations_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['count']




class determine_distance_from_Earth_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['aparent_magnitude_calculation', 'absolute_magnitude_calculation']




class ratio_in_brightness_between_two_stars_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['first_aparent_magnitude_ratio_brightness', 
		'second_aparent_magnitude_ratio_brightness']



class light_years_in_parsecs_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['light_years']





class calculate_the_annual_paralax_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['distance_from_Earth_paralax']






class SumofAttributesofnthDayForm(ModelForm):


	class Meta:

		model = Day

		fields = ['date_to_sum_all_attributes', "nth_day_value_all_attributes", "nth_month_value_all_attributes",

				  'hour_all_attributes', 'minute_all_attributes', 'second_all_attributes']





class Determine_the_visibility_of_a_star_in_seasons_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ["name"]




class calculate_the_flux_density_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ["absolute_magnitude_flux_density", "telescope_aperture"]




class stars_visible_in_equinox_dates_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_stars_equinoxes', 'second_id_stars_equinoxes']




class stars_visible_in_solstice_dates_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_stars_solstices', 'second_id_stars_solstices']




class display_stars_most_visible_in_equinox_dates_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['count']




class display_stars_most_visible_in_solstice_dates_Form(ModelForm):

	class Meta:

		model = Stars

		fields = ['count']




class set_total_lunar_eclipses_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['first_id_set_total_lunar_eclipses', 'second_id_set_total_lunar_eclipses']










class delete_the_DaysInSearchEngine_using_ids_Form(ModelForm):

	class Meta:

		model = DaysInSearchEngine

		fields = ['id_one_objs_to_delete', 'id_two_objs_to_delete']










