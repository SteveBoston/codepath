	
def public_way_status():
	pw_status = raw_input("Is your building surrounded and adjoined by public ways or yards that are"
							" at least 60 feet wide? Enter yes or no.\n")

	valid_yes_no = ["yes", "no"]

	if pw_status not in valid_yes_no:
		print "You didn't enter yes or no. Let's try again.\n"

		print "\n"

		return public_way_status()

	if pw_status == "yes":
		return pw_status

	if pw_status == "no":
		pw_status = raw_input ("Okay, let's try this. Is your building surrounded and adjoined by public ways or yards that are"
				" at least 40 feet wide? Enter yes or no.\n")

		if pw_status not in valid_yes_no:
			print "You didn't enter yes or no. Let's try again.\n"
			return public_way_status

		print "\n"

		if pw_status == "no":
			return pw_status

		if pw_status == "yes":
			pw_status = raw_input("Your building might still qualify for the special case if it meets these requirements:\n"
									"1. The reduced width shall not be allowed for more than 75 percent of the perimeter of the building.\n"
									"2. The exterior walls facing the reduced width shall have a minimum fire-resistance rating of 3 hours.\n"
									"3. Openings in the exterior walls facing the reduced width shall have opening protectives "
									" with a minimum fire protection rating of 3 hours.\n"
									" Does your building meet all of these requirements? Enter yes or no.\n")

			if pw_status not in valid_yes_no:
				print "You didn't enter yes or no. Let's try again.\n"
				return public_way_status

			else:
				return pw_status




def building_area_increase(variables):

	#section 507 unlimited area buildings 

	#507.2

	unlimited_one_list = ["f2", "s2"]

	if variables["group"] in unlimited_one_list and variables["actual_stories"] < 2:
		print "You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
		result = public_way_status()

		if result == "yes":
			print "Great. Your building qualifies for the special exception, and has unlimited building area.\n"
			variables["max_area"] = "unlimited"
			return variables

		if result == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")


	#507.3

	unlimited_two_list = ["b", "f1", "f2", "m", "s1", "s2"]

	if variables["group"] in unlimited_two_list and variables["actual_stories"] < 2 and variables["has_sprinkler"] == "yes":
		print "You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
		result = public_way_status()
		

		if result == "yes":
			print "Great. Your building qualifies for the special exception, and has unlimited building area.\n"
			variables["max_area"] = "unlimited"

			# 507.3 exception 1

			unlimited_four_list = ["s1", "s2"]
			unlimited_five_list = ["ia", "ib", "iia", "iib"]

			if variables["group"] in unlimited_four_list and variables["cons_type"] in unlimited_five_list:
				rack_storage = raw_input("You might be eligible for a different special exception that gives your building unlimited height. We'll see if you qualify.\n"
											"Is your building used for rack storage facilities that do not have access by the public? Enter yes or no.\n")

				valid_yes_no = ["yes", "no"]

				if rack_storage not in valid_yes_no:
					print "You didn't enter yes or no. Let's try again.\n"

					print "\n"

					return building_area_increase()

				if rack_storage == "no":
					print ("Okay, you didn't qualify for that special exception.\n")
					return variables

				if rack_storage == "yes":
					print "Great. Your building qualifies for the special exception, and has unlimited building height.\n"
					variables["max_height"] = "unlimited"
					return variables

			else:
				return variables

		if result == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")



	unlimited_three_list = ["ia", "ib", "iia", "iib", "iiia", "iiib", "iv"]

	if variables["group"] == "a4" and variables["actual_stories"] < 2 and variables["cons_type"] in unlimited_three_list and variables["has_sprinkler"] == "yes":
		print "You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
		result = public_way_status()

		if result == "yes":
			print "Great. Your building qualifies for the special exception, and has unlimited building area.\n"
			variables["max_area"] = "unlimited"
			return variables

		if result == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")





	# 507.3 exception 2

	if variables["group"] == "a4" and variables["actual_stories"] < 2 and variables["cons_type"] in unlimited_three_list and variables["has_sprinkler"] == "no":

		indoor_sports = raw_input("You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
									"Here is a list of conditions:\n"
									"1. Building has areas used for indoor participant sports\n"
									"2. Building has exit doors directly to the outside in participant sports areas\n"
									"3. Building is equipped with an fire alarm system with manual fire alarm boxes installed in accordance with Section 907.\n"
									"\n"
									"Does your building meet all of these conditions? Enter yes or no.\n")

		valid_yes_no = ["yes", "no"]

		if indoor_sports not in valid_yes_no:
			print "You didn't enter yes or no. Let's try again.\n"

			print "\n"

			return building_area_increase()

		if indoor_sports == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")

		if indoor_sports == "yes":
			result = public_way_status()


			if result == "yes":
				print ("Great. Your building qualifies for the special exception, and has unlimited building area."
						" Note that sprinklers are not required in the areas used for indoor participant sports, but"
						" may be required in other areas of the building.\n")
				variables["max_area"] = "unlimited"
				return variables

			if result == "no":
				print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
						"allowable building area.\n")



	#add code for 507.3.1 mixed occupancy buildings


	# 507.4 


	unlimited_six_list = [ "b", "f1", "f2", "m", "s1", "s2"]

	if variables["group"] in unlimited_six_list and variables["actual_stories"] < 3 and variables["has_sprinkler"] == "yes":
		print "You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
		result = public_way_status()

		if result == "yes":
			print "Great. Your building qualifies for the special exception, and has unlimited building area.\n"
			variables["max_area"] = "unlimited"
			return variables

		if result == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")	

		

	# 507.6

	unlimited_seven_list = ["iia", "iib"]

	if variables["group"] == "a3" and variables["actual_stories"] < 2 and variables["cons_type"] in unlimited_seven_list and variables["has_sprinkler"] == "yes":
		religious_worship_etc= raw_input("You might be eligible for a special exception that gives your building unlimited area. We'll see if you qualify.\n"
									"Here are two conditions:\n"
									"1. Building is used as a place of religious worship, community hall, dance hall, exhibition hall, gymnasium,"
										" lecture hall, indoor swimming pool, or tennis court.\n"
									"2. Building has no stage other than a platform.\n"
									"\n"
									"Does your building meet each of these conditions? Enter yes or no.\n")

		valid_yes_no = ["yes", "no"]

		if religious_worship_etc not in valid_yes_no:
			print "You didn't enter yes or no. Let's try again.\n"

			print "\n"

			return building_area_increase()

		if religious_worship_etc == "no":
			print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")


		if religious_worship_etc == "yes":
			result = public_way_status()

			if result == "no":
				print ("Okay, you didn't qualify for the special exception. We'll try some other things to increase your"
					"allowable building area.\n")	

			if result == "yes":
				print "Great. Your building qualifies for the special exception, and has unlimited building area.\n"
				variables["max_area"] = "unlimited"
				return variables	



	# continue on from 507.7.....





	#Building Area increase from frontage

	print "First, we'll look at frontage."

	perimeter = raw_input("Please enter the length in feet of your building's perimeter.\n")

	print "\n"

	perimeter = float(perimeter)

	print "Okay, your building's perimeter length is %.1f feet.\n" % perimeter

	print "\n"




	frontage = raw_input("Your qualified frontage is the length of your building's perimeter"
							" that fronts on a public way, or on an open space with a minimum"
							" width of 20 feet. Please enter this length.\n")

	print "\n"


	frontage = float(frontage)

	if frontage > perimeter:
		print ("That can't be right... You've entered a frontage length that's larger than"
				" the overall perimeter length. Let's try for a building area increase again.\n")

		return building_area_increase(variables)

	print "Okay, your building's qualified frontage length is %.1f feet.\n" % frontage

	print "\n"

	min_frontage_percentage = .25

	actual_frontage_percentage = (float(frontage)/float(perimeter))

	if actual_frontage_percentage < min_frontage_percentage:
		frontage_increase_amount = 0
		print ("To qualify for a building area increase from frontage, at least"
				" 25 percent of your building's perimeter must have qualified frontage on a public way or"
				" qualified open space. Only %.1f percent of your building's perimeter has qualified frontage,"
				" so you won't get an increase.\n") % actual_frontage_percentage

		print "\n"

	else:

		width_consistent = raw_input("Is the frontage width consistent over the entire qualified frontage?"
				" Enter yes or no\n")

		print "\n"

		valid_yes_no = ["yes", "no"]

		if width_consistent not in valid_yes_no:
			print "You didn't enter yes or no. Let's try for a building area increase again.\n"

			print "\n"

			return building_area_increase(variables)


		if width_consistent == "yes":
			width = raw_input("Please enter the width of the qualified public way/open space"
							" along the building's frontage.\n")

			print "\n"

			width = float(width)

			if width < 20:
				print "This width must be at least 20 feet. Let's try for a building area increase again.\n"

				print "\n"

				return building_area_increase(variables)

			if 20 <= width <= 30:
				print "Okay, your width is %.1f.\n" % width

				print "\n"

			if 30 < width:
				width = 30
				print ("The maximum width we can use for the calculation is 30 feet, so that's what"
						" we'll use here.\n")

				print "\n"


		if width_consistent == "no":
			width = raw_input("Please enter the WEIGHTED AVERAGE width of the qualified public way/open space"
							" along the building's frontage. Use a width of 30 for any portion of the frontage"
							" whose width is greater than 30 feet.\n")

			print "\n"

			width = float(width)

			if width < 20:
				print ("That can't be right... all widths along the frontage must be at least 20 feet."
						" Let's try for a building area increase again.\n")

				print "\n"

				return building_area_increase(variables)

			if 20 <= width <= 30:
				print "Okay, your weighted average width is %s.\n" % width

				print "\n"

			if 30 < width:
				print ("That can't be right...you should use a width of 30 for any portion of the frontage"
						" whose width is greater than 30 feet. Let's try for a building area increase again.\n")

				print "\n"

				return building_area_increase(variables)



		frontage_area_increase = ((frontage/perimeter) - min_frontage_percentage) * (width/30)


		frontage_increase_amount = (variables["max_area"] * frontage_area_increase)

		print ("Great. The frontage calculation increased your allowable building"
				" area by %.1f square feet.\n") % frontage_increase_amount

		print "\n"


		# add 506.2.1 exception
		# additional info about open space in 506.2.2 - should be in final version
		





	# Building Area increase from sprinklers


	print "Next, we'll look at sprinklers.\n"

	print "\n"

	if variables["has_sprinkler"] == "no":
		sprinkler_increase_amount = 0
		print ("Your building isn't equipped throughout with an approved sprinkler system, so you won't get"
				"a building area increase from sprinklers.\n")

		print "\n"

	elif variables["has_sprinkler"] == "yes":
		if variables["group"] == "h1":
			sprinkler_increase_amount = 0
			print ("Your building has an H-1 occupancy. Buildings with H-1 occupancies"
					" don't get allowable building area increases from sprinklers.\n")

			print "\n"

			# fix this...the function continues to the next conditional rather than going to final calculation below.

		# 506.3 exception 2 for H-2 and H-3 occupancies. figure out and add this condition

		if variables["sprinkler_for_fire_resistance_rating"] == "yes":
			sprinkler_increase_amount = 0
			print ("You're using the sprinkler system to substitute for 1-hour rated construction, so "
					"you cannot use it to increase your allowable building area.\n")

			print "\n"


		else: 
			if variables["actual_stories"] < 2:
				sprinkler_area_increase = 3
			
			elif variables["actual_stories"] >= 2:
				sprinkler_area_increase = 2

			sprinkler_increase_amount = (variables["max_area"] * sprinkler_area_increase)

			print ("Great, your sprinkler system qualifies you for a building area increase."
					"Based on the information you've already entered, the sprinkler calculation increased"
					" your allowable building area by %s.\n") % sprinkler_increase_amount

			print "\n"





	# combined calculation

	initial_area_value = variables["max_area"]

	variables["max_area"] = variables["max_area"] + frontage_increase_amount + sprinkler_increase_amount

	if initial_area_value == variables["max_area"]:
		print ("You didn't qualify for either the sprinker or the frontage increase to your building area."
				"Your allowable building area remains %s square feet.\n") % variables["max_area"]

		print "\n"


	elif initial_area_value < variables["max_area"]:
		print ("Okay, based on the frontage and sprinkler calculations,"
				" your allowable building area increased to %.1f square feet.\n") % variables["max_area"]

		print "\n"


	return variables
			


























