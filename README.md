### DRF TEMPLATE

Dependencies

*	Python >= 3.3
*	Django >= 2.0

How to test at local server

   * Setup a Virtual Environment

        Create a virtual environment <env name>:

            python -m venv project_env	

        Now activate your environment by :

            project_env\Scripts\activate (Windows)
            source project_env/bin/activate (Linux / Mac)

      This creates and activates your virtual environment

   * Clone the repository

          git clone https://github.com/apaar97/Upchaar.git

   * Install python packages

        In your commandline, change directory to the project root :

            cd .\Upchaar\

        Now install the requirements :

            pip install -r requirements.txt

   * Django Setup

        Initialise django application and database :

            python manage.py makemigrations
            python manage.py migrate

        Create admin superuser :

            python manage.py createsuperuser

        This will prompt to create a username, email and password credentials. This is local to your development server

        Run local server :

            python manage.py runserver

      This starts the development server at localhost / 127.0.0.1:8000. Use your browser to view the local site
        Access admin interface at 127.0.0.1:8000/admin by logging in with the created credentials
