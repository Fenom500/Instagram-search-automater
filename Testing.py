import InstaBot

# Logging In:
User = InstaBot.IGBot()

# User.quick_analysis()
# User.go_to_profile()
# User.check_private()

# User.username = "patientzzero"

User.go_to_profile()
User.check_private()

User.shutdown(delay=60)
