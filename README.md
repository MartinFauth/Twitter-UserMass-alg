# Twitter-UserMass-alg

traduction en Python du code userMass.scala de twitter avec un objet modifiable pour pouvoir calculer sa masse ("réputation") (https://github.com/twitter/the-algorithm.git)
Ce code attribue un score de réputation à un utilisateur en fonction des paramètres par défault suivants :

userId | "123"      
age | 50        
isRestricted | False          
isSuspended | False     
isVerified | False      
hasValidDevice | True       
numFollowers | 1000     
numFollowings | 1000        
deactivated | False     

Ce score est utilisé pour savoir quels utilisateurs méritents d'être mis en avant plus que d'autres. 

En modifiant des paramètres on peut observer les comportements suivants:

- modification du nombre de followers (abonnées)(voir image1.png)

- modification du nombre de followings(abonnements) (voir image2.png)

- modification de l'age d'un compte(en jours) (voir image3.png)

- isSuspended donne une masse nulle

- isVerified permet de commencer avec une masse de 100

- isRestricted divise la masse par 10

- hasValidDevice fait commencer à 5 si faux 

- deactivated donne une masse nulle. 



Pour run le programme :
        python userMass.py