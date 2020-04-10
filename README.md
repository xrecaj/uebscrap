# UOC - Tipologia i Cicle de Vida de les dades
## Pràctica-01 Webscraping

## 1.Context
Per realitzar aquesta recol·lecció de dades es parteix de Wikipedia, concretament de la pàgina que mostra un índex dels Ministeris o Departaments d’Economia de la majoria de països del món.
> https://en.wikipedia.org/wiki/Ministry_of_Finance

A partir d’aquesta pàgina inicial, es possible filtrar la majoria països del G-7 (Estats Units, França, Alemania, Canada, Regne Unit, Italia, Japó i la Unió Europea*).

Respecte la Unió Europea, degut a la seva organització, no existeix un ministre d’economia, s’ha optat per incloure el link a la seva pàgina directament.

Adicionalment, per interès particular, també s’ha inclòs Espanya en aquest grup.

Per realitzar la cerca de noticies relacionades amb el Coronavirus, s’ha utilitzat google i les seves opcions avançades per filtrar els resultats:
-	**site:** retorna resultats d’un lloc web determinat
-	**allintext:**,**allintitle:** retorna resultats on la paraula es troba en el text o en el títol del document. 

## 2. Títol del Dataset
“Noticies econòmiques publicades pel G-7 i Espanya relacionades amb el Coronavirus (COVID-19)”

## 3. Descripció del Dataset
| Camp | Tipus | Descripció |
| --- | --- | --- |
| Moe | Text | Nom de Ministeri o Departament d&#39;Economia |
| Link | Text:URL | URL per navegar a la notícia |
| Titol | Text | Títol de la noticia |
| Data\_Publicacio | Text | Data de publicació de la notícia |
| Resum | Text | Breu resum de la notícia |

## 4. Representació Gràfica del Dataset
https://databasic.io/es/wtfcsv/results/5e9033dfb1220fa17977adec?submit=true

## 5. Contingut del Dataset
Aquest dataset conté un recull de notícies econòmiques relacionades amb el Coronavirus (COVID-19) obtingudes de les webs oficials dels Ministeris o Departaments d’Economia dels països i organitzacions que formen el G-7 més Espanya.

Es un recull de noticies en brut, o sigui que no presenta la informació detallada de tota la noticia sinó que presenta en format breu, un resultat de la cerca de noticies equivalent al resultat que s’obté de google utilitzant certs paràmetres de cerca avançada (idioma de la notícia, buscar només en el texte o en el títol, i periode de publicació).

La utilitat que preten aquests dataset es la d’agilitzar la cerca d’aquestes notícies en tot aquest conjunt de webs oficials.


## 6. Agraïments
(pendent)

## 7. Inspiració
En el moment de realitzar aquesta pràctica estava confinat a casa degut a la pàndemia provocada per el coronavirus. 

Cada dia la meva dona, per motius de feina, havia de recol·lectar noticies relacionades en l’àmbit econòmic sobre les mesures que aplicaven diferents goberns per mitigar els efectes del coronavirus. Per tant, vaig pensar que aquesta pràctica podria ser d’ajuda en el seu dia a dia.

## 8. Llicència
Aquest dataset té una llicència d’us CC BY-NC-SA 4.0, la qual permet i per aquests motius ha sigut escollida:

-	Compartir, copiar, modificar i distributir treballs realitzats a partir d’aquest dataset sempre i quan es faci amb una llicència idèntica o compatible
-	No es permet copiar, distribuir o utilitzar aquest dataset per un ús comercial.
-	Es obligat d’esmentar a l’autor i el link d’aquest tipus de llicència, així com indicar els canvis que s’hagin realitzat, per part de tercers que facin ús d’aquest dataset.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>
