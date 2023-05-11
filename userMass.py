import math
import time


userOne = {
	"userId": "123",
	"age": 1651033778,
	"isRestricted": False,
	"isSuspended": False,
	"isVerified": False,
	"hasValidDevice": True,
	"numFollowers": 700000,
	"numFollowings": 700000,
	"deactivated": False,
}

def getUserMass(userData):
	currentTimestamp = time.time()
	constantDivisionFactorGt_threshFriendsToFollowersRatioUMass = 5
	threshAbsNumFriendsUMass = 500
	threshFriendsToFollowersRatioMass = 0.6
	deviceWeightAdditive = 0.5
	ageWeightAdditive = 0.2
	restrictedWeightMultiplicative = 0.1

	age = currentTimestamp - userData["age"]

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

			if age > 30 * 86400:
				normalizedAge = 1
			else:
				normalizedAge = math.log(1 + (age / 15) * (1/86400))

			score *= normalizedAge

			if score < 0.01:
				score = 0.01

			if userData["isRestricted"] == True:
				score *= restrictedWeightMultiplicative

			score *= 100

			mass = score

			print("mass", mass)

		friendToFollowersRatio = (1 + userData["numFollowings"]) / (1 + userData["numFollowers"])
		print("friendToFollowersRatio", friendToFollowersRatio)

		adjustedMass = mass

		if userData["numFollowings"] > threshAbsNumFriendsUMass and friendToFollowersRatio > threshFriendsToFollowersRatioMass:
			adjustedMass = mass / math.exp(constantDivisionFactorGt_threshFriendsToFollowersRatioUMass * (friendToFollowersRatio - threshFriendsToFollowersRatioMass))

		return adjustedMass

returnedMass = getUserMass(userOne)
print("User", userOne) 
print("mass", returnedMass)
