# TD_211_Malerba_Fabio

A) Les différents moyens de production d’énergie en France

Toutes les sources d’électricité proviennent de la transformation d’énergies primaires, directement présentes dans la nature 
(pétrole, bois, gaz naturel, etc.) , en énergies secondaires produites par l’homme (comme la transformation de la chaleur en électricité 
dans les centrales thermiques). Une fois produite, l’énergie secondaire doit être transportée vers son lieu de consommation. L’électricité 
que reçoit le consommateur est appelée énergie finale. Il existe 4 grands types d'énergie : mécanique, photovoltaïque, thermoélectrique et gravitationnelle.
Certaines techniques de production sont anciennes de plus d'un siècle, comme les centrales au charbon, d'autres récentes, à l'instar de la géothermie pour 
de la biomasse. Certaines sont encore en cours de développement et pourraient bouleverser le paysage de la production d'électricité, comme les fours solaires, 
les usines marémotrices ou plus généralement les méthodes de gazéification de la biomasse. L'électricité produite provient pour 69 % du nucléaire ; pour 19 % 
des sources d'énergie renouvelables : production hydroélectrique : 11 %, éolien : 6 % et énergie solaire : 2 % ; et pour 11 % des centrales thermiques fossiles.


B) Les panneaux solaires

Un panneau solaire est un dispositif convertissant une partie du rayonnement solaire en énergie thermique ou électrique, grâce à des capteurs solaires 
thermiques ou photovoltaïques respectivement Le plus souvent, les panneaux solaires sont sur un support fixe dans l'orientation varie notamment de la position 
géographique de l'installation.


C) Objectifs

Dans le cadre de ce TP, il est question d'explorer l'efficacité d'une installation disposant d'un système de suivi du soleil par rapport à une installation fixe.
Les objectifs sont les suivants -Le montage du prototype -Le test de l'orientation du prototype -Compréhension du fonctionnement et utilisation du capteur 
de luminosité -Raccordement de la charge électrique sur le panneau solaire -Mesure et enregistrement de la puissance de sortie.


D) Cahier des charges

-Le prototype devait fonctionner dans un environnement "Circuit playground" de chez Adafruit. Ainsi, l'alimentation de tous les appareils, comme les servomoteurs 
et le microcontrôleur, doit donc se faire en 3.3 V. Par suite d’un problème approvisionnement, la tension d'alimentation doit impérativement passer de 3.3 V et 5 V.
Il a donc été inévitable de passer sur un environnement Arduino ce qui implique que la partie programmation informatique se fasse majoritairement en C++ plutôt
qu’en python.


-Des flowchart pour chacun des scénarios : https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Flowchart_scénarios_1_et_2
-Écrire les scripts qui correspondent à chacun des scénarios.

-Modifier le prototype afin de contrôler manuellement l'orientation du panneau solaire:
https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Code%20Arduino/AAM_TD_211_Malerba_Fabio_controle_manuel_des_servos -L'automatiser pour qu'il puisse decrire un arc de cercle (code disponible sur ce lien) : https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Code%20Python


-Intégrer le capteur de luminosité au fonctionnement du prototype pour ajuster la position du plateau (inclinaison et rotation),
afin de suivre le soleil, de façon que le panneau soit toujours en face du soleil:
https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Code%20Arduino/AAM_TD_211_MAlerba_Fabio_Suivre_la_lumière


-Le panneau solaire doit être équipé d'une charge électrique ainsi que d'un système de mesure de puissance. 
https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Code%20Arduino/AAM_TD_211_Malerba_Fabio_puissance_electrique


-Écrire les scripts qui correspondent à chacun des scénarios

-Enregistrement des données avec un dattaloger muni d’une carte SD, (dans la partie dattaloger): 
https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Code%20Arduino/Datalogger/AAM_TD_211_Malerba_Fabio_dattaloger

-Créer un compte rendu sous forme de PV de livraison et un rapport de projet: https://github.com/fabiglose/TD_211_Malerba_Fabio/tree/main/Compte-rendu%20final

E) Matériel nécessaire

-2 Cartes Arduino Uno 
-Capteurs de lumieres (photoresistances) 
-Dattalogger 
-Carte SD 
-Câbles Arduino 
-2 Potentiomètres
-2 Résistances de 25 Ω 
-1cellule photovoltaique 
-Pièces détachées du prototype en découpe laser 
-Quincailleries adéquat (vis, boulons)
