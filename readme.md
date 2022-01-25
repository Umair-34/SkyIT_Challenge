* Instruction to Run the Project:
    * Unzip the folder
    * Create Virtual environment inside the project
    * Activate the virtual environment
    * Install the project requirements using following command \
           -> pip install -r requirements.txt
    * To make migrations use the following command\
           -> python manage.py makemigrations
    * To push migrations on db\
           -> python manage.py migrate
    * To create superuser run the following command\
           -> python manage.py createsuperuser (and follow the instructions)
    * To run the server run following command
           -> python manage.py runserver 

* Access the Url of the project
  * For list and create Vehicle:
        http://127.0.0.1:8000/api/vehicle/
  * for update a specific vehicle:
        http://127.0.0.1:8000/api/updateVehicle/1/  ( /1/ is the vehicle id)
  * for creating mileage of specific vehicle:
        http://127.0.0.1:8000/api/createMileage/    (select vehicle and add mileage)
  * for calculating mileage coverage of vehicle:
        http://127.0.0.1:8000/api/calculateMileage/1/2022-01-03/   (/1/ is vehicle id and /2022-01-03/ is date)