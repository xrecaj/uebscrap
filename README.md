# UOC - Tipologia i Cicle de Vida de les dades
## Pràctica-01 Webscraping

## 1.Context
Per realitzar aquesta recol·lecció de dades es parteix de Wikipedia, concretament de la pàgina que mostra un índex dels Ministeris o Departaments d’Economia de la majoria de països del món.
> https://en.wikipedia.org/wiki/Ministry_of_Finance

A partir d’aquesta pàgina inicial, es possible filtrar la majoria països del G-7 (Estats Units, França, Alemanya, Canada, Regne Unit, Itàlia, Japó i la Unió Europea*).

Respecte la Unió Europea, degut a la seva organització, no existeix un ministre d’economia, s’ha optat per incloure el link a la seva pàgina directament.

Addicionalment, per interès particular, també s’ha inclòs Espanya en aquest grup.

Per realitzar la cerca de noticies relacionades amb el Coronavirus, s’ha utilitzat google i les seves opcions avançades per filtrar els resultats:
-	**site:** retorna resultats d’un lloc web determinat
-	**allintext:**,**allintitle:** retorna resultats on la paraula es troba en el text o en el títol del document. 

## 2. Títol del Data set
“Noticies econòmiques publicades pel G-7 i Espanya relacionades amb el Coronavirus (COVID-19)”

## 3. Descripció del Data set
| Camp | Tipus | Descripció |
| --- | --- | --- |
| Moe | Text | Nom de Ministeri o Departament d&#39;Economia |
| Link | Text: URL | URL per navegar a la notícia |
| Titol | Text | Títol de la noticia |
| Data\_Publicacio | Text | Data de publicació de la notícia |
| Resum | Text | Breu resum de la notícia |
| Noticia | Text | Text de la notícia |

## 4. Representació Gràfica del Data set
![Visualització G7 Moe Dataset](https://github.com/xrecaj/uebscrap/blob/master/Figure_1_eda.png)
https://databasic.io/es/wtfcsv/results/5e9033dfb1220fa17977adec?submit=true

## 5. Contingut del Data set
Aquest data set conté un recull de notícies econòmiques relacionades amb el Coronavirus (COVID-19) obtingudes de les webs oficials dels Ministeris o Departaments d’Economia dels països i organitzacions que formen el G-7 més Espanya.

Es un recull de noticies en brut, o sigui que no presenta la informació detallada de tota la noticia sinó que presenta en format breu, un resultat de la cerca de noticies equivalent al resultat que s’obté de google utilitzant certs paràmetres de cerca avançada (idioma de la notícia, buscar només en el text o en el títol, i període de publicació).

La utilitat que pretén aquests data set es la d’agilitzar la cerca d’aquestes notícies en tot aquest conjunt de webs oficials.


## 6. Agraïments
Per les dades que s’han obtingut del:
-	Federal Ministry of Finance (Germany). https://www.bundesfinanzministerium.de/
-	Ministry of Economy and Finance (Italy). http://www.mef.gov.it
-	Ministry of Finance (Japan). https://www.mof.go.jp
-	Ministerio de Asuntos Económicos y Transformación (Spain). https://www.mineco.gob.es/
-	Ministry of Public Action and Accounts (France). https://www.economie.gouv.fr/
-	European Commission (EU). https://ec.europa.eu
-	U.S. Departament of Commerce. https://www.commerce.gov
-	Department of Finance (Canada). https://www.canada.ca/en/department-finance/
-	UK Department for Business, Innovation & Skills. https://www.gov.uk/business-asset-disposal-relief

## 7. Inspiració
En el moment de realitzar aquesta pràctica estava confinat a casa degut a la pandèmia provocada per el coronavirus. 

Cada dia la meva dona, per motius de feina, havia de recol·lectar noticies relacionades en l’àmbit econòmic sobre les mesures que aplicaven diferents governs per mitigar els efectes del coronavirus. Per tant, vaig pensar que aquesta pràctica podria ser d’ajuda en el seu dia a dia.

## 8. Llicència
Aquest data set té una llicència d’us CC BY-NC-SA 4.0, la qual permet i per aquests motius ha sigut escollida:

-	Compartir, copiar, modificar i distribuir treballs realitzats a partir d’aquest data set sempre i quan es faci amb una llicència idèntica o compatible
-	No es permet copiar, distribuir o utilitzar aquest data set per un ús comercial.
-	Es obligat d’esmentar a l’autor i el link d’aquest tipus de llicència, així com indicar els canvis que s’hagin realitzat, per part de tercers que facin ús d’aquest data set.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>

## 9.DOI
<a href="https://doi.org/10.5281/zenodo.3747299"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3747299.svg" alt="DOI"></a>

