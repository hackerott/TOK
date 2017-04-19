O projeto possuirá as seguintes camadas:
- Camada WEB (PHP) usando APIS para devolução de dados;
- Camada de Modelos (Python);

#Camada python:
Dependencias para ubuntu 14.04:

			- Python 2.7
				-Numpy
				-Datetime
				-Sys
				-netCDF4
				-Math
				-Calendar
			- Netcdf4
			- Jasper
			- HDF5
			- CDM

#Estrutura:
Estara separada em 4 partes independentes, cada uma responsavel por um tipo de modelo (WRF, GFS de 1 e 3  hrs, CFS)
Cada um dos modelos esatara subdividido em 3 apps, sendo eles:
Tabela horaria ou detalhamento diario
- Valor do dia (max, min ou medio dependente da variavel)
- Localizador da lat e lon (cada modelo utiliza mecanismos diferentes de localizacao)
Alem destes um app para processar os ensambles sazonais, acompanhados dos scripts necessarios em bash

#Descriçao detalhada:
		WRF:
	    -Tabela:
			-Dia:
			-Localizador:
		
 		GFS1:
			-Tabela:
			-Dia:
			-Localizador:

		GFS3:
			-Tabela:
			-Dia:
			-Localizador:
		
		CFS:
			-Dia:
			-Localizador:
	

		Sazonal:
			Corte:
			CSV:

The project will have the following layers:
- WEB layer (PHP) using APIS for data return;
- Model Layer (Python);

#Python call:
Dependencies for ubuntu 14.04:

- Python 2.7
-Numpy
-Datetime
-Sys
-netCDF4
-Math
-Calendar
- Netcdf4
Jasper
- HDF5
- CDM

Google Translation.

#Structure:
It will be separated into 4 independent parts, each one responsible for a type of model (WRF, GFS of 1 and 3 hrs, CFS)
Each of the models is divided into 3 apps, which are:
Daily timetable or table
- Day value (max, min or medium dependent on the variable)
- lat and lon locator (each model uses different localization mechanisms)
Besides these an app to process the seasonal assemblies, accompanied by the necessary scripts in bash

#Detailed Description:
WRF:
-Table:
-Day:
-Localizer:

 GFS1:
-Table:
-Day:
-Localizer:

GFS3:
-Table:
-Day:
-Localizer:

CFS:
-Day:
-Localizer:


Seasonal:
Court:
CSV:
