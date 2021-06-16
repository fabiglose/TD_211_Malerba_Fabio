# TD_211_Malerba_Fabio
 
A)	Les différents moyens de production d’énergie en France


Toutes les sources d’électricité proviennent de la transformation d’énergies primaires, directement présentes dans la nature (pétrole, bois, gaz naturel, etc.), en énergies secondaires produites par l’homme (comme la transformation de la chaleur en électricité dans les centrales thermiques). Une fois produite, l’énergie secondaire doit être transportée vers son lieu de consommation. L’électricité que reçoit le consommateur est appelée énergie finale.
 Il existe 4 grands types d'énergie : mécanique, photovoltaïque, thermoélectrique et gravitationnelle. Certaines techniques de production sont anciennes de plus d'un siècle, comme les centrales au charbon, d'autres récentes, à l'instar de la géothermie pour de la biomasse. Certaines sont encore en cours de développement et pourraient bouleverser le paysage de la production d'électricité, comme les fours solaires, les usines marémotrices ou plus généralement les méthodes de gazéification de la biomasse. L'électricité produite provient pour 69 % du nucléaire ; pour 19 % des sources d'énergie renouvelables : production hydroélectrique : 11 %, éolien : 6 % et énergie solaire : 2 % ; et pour 11 % des centrales thermiques fossiles.

B)	Les panneaux solaires


 Un panneau solaire est un dispositif convertissant une partie du rayonnement solaire en énergie thermique ou électrique, grâce à des capteurs solaires thermiques ou photovoltaïques respectivement
Le plus souvent, les panneaux solaires sont sur un support fixe dans l'orientation varie notamment de la position géographique de l'installation.


C)	Objectifs

Dans le cadre de ce TP, il est question d'explorer l'efficacité d'une installation disposant d'un système de suivi du soleil par rapport à une installation fixe. Les objectifs sont les suivants
-Le montage du prototype 
-Le test de l'orientation du prototype
-Compréhension du fonctionnement et utilisation du capteur de luminosité 
-Raccordement de la charge électrique sur le panneau solaire
-Mesure et enregistrement de la puissance de sortie.


D)	Cahier des charges


Le projet se décompose en deux scénarios : 

-Le prototype devait fonctionner dans un environnement "Circuit playground" de chez Adafruit. Ainsi, l'alimentation de tous les appareils, comme les servomoteurs et le microcontrôleur, doit donc se faire en 3.3 V. Par suite d’un problème approvisionnement, la tension d'alimentation doit impérativement passer de 3.3 V et 5 V.
Il a donc été inévitable de passer sur un environnement Arduino ce qui implique que la partie programmation informatique se fasse majoritairement en C++ plutôt qu’en python.

- Modifier le prototype afin de contrôler manuellement l'orientation du panneau solaire.
- Intégrer le capteur de luminosité au fonctionnement du prototype pour ajuster la position du plateau (inclinaison et rotation), afin de suivre le soleil, de façon que le panneau soit toujours en face du soleil.
		
- Le panneau solaire doit être équipé d'une charge électrique ainsi que d'un système de mesure de puissance.
-Écrire les scripts qui correspondent à chacun des scénarios

-Enregistrement des données avec un dattaloger muni d’une carte SD.



E)	Matériel nécessaire


-2 Cartes Arduino Uno
-Capteur de lumieres (photoresistances)
-Dattalogger
-Carte SD
-Câbles Arduino
-2 Potentiomètres
-2 Résistances de 25 Ω
- 1celleule photovoltaiques
-Pièces détachées du prototype en découpe laser
-Quincailleries adéquat (vis, boulons)

