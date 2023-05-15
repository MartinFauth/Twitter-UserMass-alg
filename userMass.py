import math
import time


userOne = {
	"userId": "123",
	"age": 50,
	"isRestricted": False,
	"isSuspended": False,
	"isVerified": False,
	"hasValidDevice": True,
	"numFollowers": 1000,
	"numFollowings": 1000,
	"deactivated": False,
}

def getUserMass(userData):

	constantDivisionFactorGt_threshFriendsToFollowersRatioUMass = 5
	threshAbsNumFriendsUMass = 500
	threshFriendsToFollowersRatioMass = 0.6
	deviceWeightAdditive = 0.5
	ageWeightAdditive = 0.2
	restrictedWeightMultiplicative = 0.1

	age = userData["age"]

	if userData["userId"] == "" or userData["deactivated"] == True:
		return None
	else:
		if userData["isSuspended"] == True:
			mass = 0
		elif userData["isVerified"] == True:
			mass = 100
		else:
			score = deviceWeightAdditive * 0.1

			if userData["hasValidDevice"] == True:
				score += deviceWeightAdditive
			else:
				score += 0

			if age > 25:
				normalizedAge = 1
			else:
				normalizedAge = (math.log(1 + (age / 15)))

			score *= normalizedAge

			if score < 0.01:
				score = 0.01

			if userData["isRestricted"] == True:
				score *= restrictedWeightMultiplicative

			score *= 100

			mass = score


		friendToFollowersRatio = (1 + userData["numFollowings"]) / (1 + userData["numFollowers"])

		adjustedMass = mass

		if userData["numFollowings"] > threshAbsNumFriendsUMass and friendToFollowersRatio > threshFriendsToFollowersRatioMass:
			adjustedMass = mass / math.exp(constantDivisionFactorGt_threshFriendsToFollowersRatioUMass * (friendToFollowersRatio - threshFriendsToFollowersRatioMass))

		return adjustedMass


returnedMass = getUserMass(userOne)
print("User", userOne) 
print("mass", returnedMass)